"""IA2"""

from .NsIAccessible import NsIAccessible

class IA2(NsIAccessible):
    """IA2 windows protocol"""
    def __init__(self, acc_id):
        super(IA2, self).__init__()
    def serialize(self, child_depth):
        """Convert pointer to object for serialization"""
