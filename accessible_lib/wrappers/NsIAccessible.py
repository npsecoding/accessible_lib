"""Interface for Accessible Object"""

from ..scripts.util import util

class NsIAccessible(object):
    """Accessible Object Interface Definition"""
    def __init__(self, acc_id):
        _util = util()
        self._target = _util.get_target_accessible(acc_id)
        self.name = self.get_acc_name()
        self.role = self.get_acc_role()
        self.state = self.get_acc_state()
        self.value = self.get_acc_value()
    def get_acc_child(self):
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
