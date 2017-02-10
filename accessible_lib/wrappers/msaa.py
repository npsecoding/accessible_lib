"""MSAA"""

from .NsIAccessible import NsIAccessible
from ..scripts.constants import CHILDID_SELF

class MSAA(NsIAccessible):
    """MSAA windows protocol"""
    def __init__(self, acc_id):
        super(MSAA, self).__init__(acc_id)
        self.parent = self.get_acc_parent()
        self.children = self.get_acc_children()
    def get_acc_children(self):
        """Get child accessible"""
        parent = self._target
        children_ptr = self._util._accessible_children(parent)
        children = map(pointer_wrap_child, children_ptr)
        return children
    def get_acc_focus(self):
        """Get focus"""
        """TODO"""
    def get_acc_name(self):
        """Get computed name"""
        return self._target.accName(CHILDID_SELF)
    def get_acc_parent(self):
        """Get parent accessible"""
        return pointer_wrap_parent(self._target.accParent)
    def get_acc_role(self):
        """Get computed role"""
        return self._target.accRole(CHILDID_SELF)
    def get_acc_state(self):
        """Get computed state"""
        return self._target.accState(CHILDID_SELF)
    def get_acc_value(self):
        """Get computed value"""
        return self._target.accValue(CHILDID_SELF)

def pointer_wrap_parent(acc_ptr):
    """Convert pointer to object for serialization"""
    return {
        # Not returning parent field in parent pointer
        'name': acc_ptr.accName(CHILDID_SELF),
        'role': acc_ptr.accRole(CHILDID_SELF),
        'state': acc_ptr.accState(CHILDID_SELF),
        'value': acc_ptr.accValue(CHILDID_SELF)
    }

def pointer_wrap_child(acc_ptr):
    """Convert pointer to object for serialization"""
    print acc_ptr
    return {
        # Not returning parent field
        'name': acc_ptr.accName(CHILDID_SELF),
        'children': "",
        'role': acc_ptr.accRole(CHILDID_SELF),
        'state': acc_ptr.accState(CHILDID_SELF),
        'value': acc_ptr.accValue(CHILDID_SELF)
    }
