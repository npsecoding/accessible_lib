"""IAccessible"""

from ctypes import oledll, create_string_buffer
from .NsIAccessible import NsIAccessible
from ..scripts.constants import CHILDID_SELF, FULL_CHILD_TREE
from ..scripts.debug import DEBUG_ENABLED

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

    def serialize(self, child_depth=-1):
        """
        Serialize accessible into json
        """

        # Set child depth to full tree if none specified
        if child_depth is None:
            child_depth = -1
        else:
            child_depth = int(child_depth)

        child_tree = {'Children': None}
        attributes = [
            'accChildCount', 'accChildren', 'accDefaultAction', 'accDescription',
            'accFocus', 'accHelp', 'accHelpTopic', 'accKeyboardShortcut', 'accLocation',
            'accName', 'accParent', 'accRole', 'accSelection', 'accState', 'accValue']
        not_callable = ['accChildCount', 'accSelection']
        custom_callable = {
            'accChildren': self.get_acc_children(self._target, child_tree, child_depth, True),
            'accParent': self.semantic_wrap(getattr(self._target, 'accParent')),
            'accFocus' : self.get_acc_focus(self._target)
            # Localized role and state
            # 'accRole': localized_role(getattr(self._target, 'accRole')(CHILDID_SELF)),
            # 'accState': localized_state(getattr(self._target, 'accState')(CHILDID_SELF))
        }
        node = self._target

        # If object is simple element remove irrelevant children fields
        if node.isSimpleElement:
            attributes.remove('accChildren')
            del custom_callable['accChildren']
            return self.parsed_json(node, attributes, custom_callable, not_callable, node.childId)

        return self.parsed_json(node, attributes, custom_callable, not_callable)

    def semantic_wrap(self, acc_ptr, child_id=CHILDID_SELF):
        "Wrap children and parent pointers exposing semantics"

        # Handle cases when accessible object doesn't have:
        # keyboard focus
        # parent accessible
        if acc_ptr is None:
            return None

        attributes = ['accName', 'accChildCount', 'accRole', 'accState', 'accValue']
        not_callable = ['accChildCount', 'accSelection']
        custom_callable = {
            # Localized role and state
            # 'accRole': localized_role(getattr(acc_ptr, 'accRole')(child_id)),
            # 'accState': localized_state(getattr(acc_ptr, 'accState')(child_id))
        }

        return self.parsed_json(acc_ptr, attributes, custom_callable, not_callable, child_id)

    def parsed_json(self, acc_ptr, attribs, custom_callable, not_callable, child_id=CHILDID_SELF):
        "Does parsing of fields and determines call type for value"
        json = {}
        prefix = "acc"

        # Add field to show child is simple element
        if DEBUG_ENABLED:
            if child_id != CHILDID_SELF:
                json['SimpleElement'] = True
            else:
                json['SimpleElement'] = False

        for attribute in attribs:
            field = attribute[len(prefix):]
            if attribute in custom_callable.keys():
                json[field] = custom_callable[attribute]
            elif attribute in not_callable:
                # Simple elements don't have children
                if field == 'ChildCount' and child_id != CHILDID_SELF:
                    json[field] = 0
                    continue

                json[field] = getattr(acc_ptr, attribute)
            else:
                try:
                    json[field] = getattr(acc_ptr, attribute)(child_id)
                except:
                    json[field] = "Attribute Not Supported"

        return json

    def get_acc_focus(self, acc_ptr):
        """Get focused object"""
        focus_val = getattr(acc_ptr, 'accFocus')
        if focus_val is None:
            return None
        elif isinstance(focus_val, int):
            return self.semantic_wrap(acc_ptr.accChild(focus_val))
        else:
            return self.semantic_wrap(focus_val)

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

        # Check if children are simple elements
        if acc_ptr in self._util._simple_elements:
            tree['Children'] = [self.semantic_wrap(acc_ptr, i)
                                for i in range(1, acc_ptr.accChildCount + 1)]
            return

        if first:
            tree = map(self.semantic_wrap, children_ptr)
        else:
            tree['Children'] = map(self.semantic_wrap, children_ptr)

        for index, child_ptr in enumerate(children_ptr):
            if first:
                self.get_acc_children(child_ptr, tree[index], child_depth, False)
            else:
                self.get_acc_children(child_ptr, tree['Children'][index], child_depth, False)

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
