"""IA2"""

from .NsIAccessible import NsIAccessible

class IA2(NsIAccessible):
    """IA2 windows protocol"""
    def __init__(self, acc_id, child_depth):
        super(IA2, self).__init__(acc_id)
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
