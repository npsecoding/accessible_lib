"""MSAA"""

from .NsIAccessible import NsIAccessible
from ..scripts.util import util
from ..scripts.constants import CHILDID_SELF

class MSAA(NsIAccessible):
    """MSAA windows protocol"""
    def __init__(self, acc_id):
        super(MSAA, self).__init__(acc_id)
        _util = util()
        self._target = _util.get_target_accessible(acc_id)
    def get_acc_child(self):
        """Get child accessible"""
        """TODO"""
    def get_acc_focus(self):
        """Get focus"""
        """TODO"""
    def get_acc_name(self):
        """Get computed name"""
        return self._target.accName(CHILDID_SELF)
    def get_acc_parent(self):
        """Get parent accessible"""
        return self._target.accParent
    def get_acc_role(self):
        """Get computed role"""
        return self._target.accRole(CHILDID_SELF)
    def get_acc_state(self):
        """Get computed state"""
        return self._target.accState(CHILDID_SELF)
    def get_acc_value(self):
        """Get computed value"""
        return self._target.accValue(CHILDID_SELF)
