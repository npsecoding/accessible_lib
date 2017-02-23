"""Interface for Accessible Object"""

from ..scripts.util import util

class NsIAccessible(object):
    """Accessible Object Interface Definition"""
    def __init__(self):
        self._util = util()
    def get_acc_children(self, acc_ptr, tree, child_depth, first):
        """Get child accessible"""
        raise NotImplementedError
    def get_acc_focus(self):
        """Get focus"""
        raise NotImplementedError
    def get_acc_name(self):
        """Get computed name"""
        raise NotImplementedError
    def get_acc_parent(self):
        """Get parent accessible"""
        raise NotImplementedError
    def get_acc_role(self):
        """Get computed role"""
        raise NotImplementedError
    def get_acc_state(self):
        """Get computed state"""
        raise NotImplementedError
    def get_acc_value(self):
        """Get computed value"""
        raise NotImplementedError
