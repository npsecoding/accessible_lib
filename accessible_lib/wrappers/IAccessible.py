"""IAccessible"""

from ctypes import oledll, create_string_buffer
from .NsIAccessible import NsIAccessible
from ..scripts.constants import CHILDID_SELF, FULL_CHILD_TREE

class IAccessible(NsIAccessible):
    """IAccessible windows interface"""
    def __init__(self, identifiers):
        super(IAccessible, self).__init__()
        # Find accessible object associated with ID
        self._target = self._util.get_target_accessible(identifiers)
        if self._target is None:
            self.found = False
        else:
            self.found = True

    def serialize(self, child_depth):
        """Convert pointer to object for serialization"""
        child_tree = {'children': ""}
        attributes = [
            'accChildCount', 'accChildren', 'accDefaultAction', 'accDescription',
            'accFocus', 'accHelp', 'accHelpTopic', 'accKeyboardShortcut', 'accLocation',
            'accName', 'accParent', 'accRole', 'accSelection', 'accState', 'accValue']
        not_callable = ['accChildCount', 'accFocus', 'accSelection']
        custom_callable = {
            'accChildren': self.get_acc_children(self._target, child_tree, child_depth, True),
            'accParent': self.semantic_wrap(getattr(self._target, 'accParent')),
            'accRole': localized_role(getattr(self._target, 'accRole')(CHILDID_SELF)),
            'accState': localized_state(getattr(self._target, 'accState')(CHILDID_SELF))
        }

        return self.parsed_json(self._target, attributes, custom_callable, not_callable)

    def semantic_wrap(self, acc_ptr):
        "Wrap children and parent pointers exposing semantics"
        attributes = ['accName', 'accChildCount', 'accRole', 'accState', 'accValue']
        not_callable = ['accChildCount', 'accFocus', 'accSelection']
        custom_callable = {
            'accRole': localized_role(getattr(acc_ptr, 'accRole')(CHILDID_SELF)),
            'accState': localized_state(getattr(acc_ptr, 'accState')(CHILDID_SELF))
        }

        return self.parsed_json(acc_ptr, attributes, custom_callable, not_callable)

    def parsed_json(self, acc_ptr, attributes, custom_callable, not_callable):
        "Does parsing of fields and determines call type for value"
        json = {}
        prefix = "acc"

        for attribute in attributes:
            field = attribute[len(prefix):]
            if attribute in custom_callable.keys():
                json[field] = custom_callable[attribute]
            elif attribute in not_callable:
                json[field] = getattr(acc_ptr, attribute)
            else:
                json[field] = getattr(acc_ptr, attribute)(CHILDID_SELF)

        return json

    def get_acc_children(self, acc_ptr, tree, child_depth, first):
        """Get child accessible"""
        # Check if there are children
        if acc_ptr.accChildCount is 0:
            return

        # Determine depth of children
        if (child_depth is not FULL_CHILD_TREE) and (child_depth is 0):
            return
        child_depth -= 1

        # First is used to determine if a children field should wrap list
        parent = acc_ptr
        children_ptr = self._util._accessible_children(parent)

        if first:
            tree = map(self.semantic_wrap, children_ptr)
        else:
            tree['children'] = map(self.semantic_wrap, children_ptr)

        for index, child_ptr in enumerate(children_ptr):
            if first:
                self.get_acc_children(child_ptr, tree[index], child_depth, False)
            else:
                self.get_acc_children(child_ptr, tree['children'][index], child_depth, False)

        return tree

def localized_role(dw_role):
    """Get localized role from role constant"""
    cch_role_max = 50
    lpsz_role = create_string_buffer(cch_role_max)
    oledll.oleacc.GetRoleTextA(dw_role, lpsz_role, cch_role_max)
    return lpsz_role.value

def localized_state(dw_state):
    """Get localized state from state constant"""
    states = []
    # Retrieve state text
    for shift in xrange(64):
        state_bit = 1 << shift
        if state_bit & dw_state:
            states.append(_get_state_text(state_bit & dw_state))
    return states

def _get_state_text(state_bit):
    cch_role_max = 100
    lpsz_state_bit = create_string_buffer(cch_role_max)
    oledll.oleacc.GetStateTextA(state_bit, lpsz_state_bit, cch_role_max)
    return lpsz_state_bit.value
