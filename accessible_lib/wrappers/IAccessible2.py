"""IAccessible2"""

from .NsIAccessible import NsIAccessible

class IAccessible2(NsIAccessible):
    """IA2 windows protocol"""
    def __init__(self, acc_id):
        super(IAccessible2, self).__init__()
    def serialize(self, child_depth):
        """Convert pointer to object for serialization"""
