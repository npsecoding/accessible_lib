"""MSAA"""

from .NsIAccessible import NsIAccessible
from ..scripts.util import util

class MSAA(NsIAccessible):
    """MSAA windows protocol"""
    def __init__(self):
        super(MSAA, self).__init__()
        _util = util()
        self.root = _util.get_root_accessible()
        self.target = _util.get_target_accessible()
    def get_acc_child(self):
        """Get child accessible"""
        """TODO"""
    def get_acc_focus(self):
        """Get focus"""
        """TODO"""
    def get_acc_name(self):
        """Get computed name"""
        """TODO"""
    def get_acc_parent(self):
        """Get parent accessible"""
        """TODO"""
    def get_acc_role(self):
        """Get computed role"""
        """TODO"""
    def get_acc_state(self):
        """Get computed state"""
        """TODO"""
    def get_acc_value(self):
        """Get computed value"""
        """TODO"""
