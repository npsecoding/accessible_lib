"""MSAA"""

from ctypes import oledll, create_string_buffer
from .NsIAccessible import NsIAccessible
from ..scripts.constants import CHILDID_SELF, FULL_CHILD_TREE

class MSAA(NsIAccessible):
    """MSAA windows protocol"""
    def __init__(self, acc_id, child_depth):
        super(MSAA, self).__init__()
        # Find accessible object associated with ID
        self._target = self._util.get_target_accessible(acc_id)
        if self._target is None:
            self.found = False
            self.error = "No accessible found with an id of " + acc_id
            return
        self.found = True
        # IAccessible interface have name, role, state and value
        self.name = self.get_acc_name()
        self.role = self.get_acc_role()
        self.state = self.get_acc_state()
        self.value = self.get_acc_value()
        self.parent = self.get_acc_parent()
        child_tree = {'children': ""}
        self.children = self.get_acc_children(self._target, child_tree, child_depth, True)
        self.childcount = self.get_acc_child_count()
        self.defaultaction = self.get_acc_default_action()
        self.focused = self.get_acc_focus()

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
            tree = map(pointer_wrap, children_ptr)
        else:
            tree['children'] = map(pointer_wrap, children_ptr)

        for index, child_ptr in enumerate(children_ptr):
            if first:
                self.get_acc_children(child_ptr, tree[index], child_depth, False)
            else:
                self.get_acc_children(child_ptr, tree['children'][index], child_depth, False)

        return tree

    def get_acc_child_count(self):
        """Get number of children"""
        return self._target.accChildCount

    def get_acc_focus(self):
        """Get focus"""
        focused_obj = None
        if self._target.accFocus is not None:
            # Only want semantic information from focused
            focused_obj = pointer_wrap(self._target.accFocus)
        return focused_obj

    def get_acc_default_action(self):
        """Get default action associated with accessible"""
        return self._target.accDefaultAction(CHILDID_SELF)

    def get_acc_name(self):
        """Get computed name"""
        return self._target.accName(CHILDID_SELF)

    def get_acc_parent(self):
        """Get parent accessible"""
        # Only want semantic information from parent
        parent = pointer_wrap(self._target.accParent)
        return parent

    def get_acc_role(self):
        """Get localized & computed role"""
        dw_role = self._target.accRole(CHILDID_SELF)
        return localized_role(dw_role)

    def get_acc_state(self):
        """Get computed state"""
        dw_state = self._target.accState(CHILDID_SELF)
        return localized_state(dw_state)

    def get_acc_value(self):
        """Get computed value"""
        return self._target.accValue(CHILDID_SELF)

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

def pointer_wrap(acc_ptr):
    """Convert pointer to object for serialization"""
    return {
        # Not returning parent field or children field unless specified
        'name': acc_ptr.accName(CHILDID_SELF),
        'childcount': acc_ptr.accChildCount,
        'defaultaction': acc_ptr.accDefaultAction(CHILDID_SELF),
        'role': localized_role(acc_ptr.accRole(CHILDID_SELF)),
        'state': localized_state(acc_ptr.accState(CHILDID_SELF)),
        'value': acc_ptr.accValue(CHILDID_SELF)
    }
