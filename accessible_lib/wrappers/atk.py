"""ATK"""

from .NsIAccessible import NsIAccessible

class ATK(NsIAccessible):
    """ATK linux protocol"""
    def __init__(self, acc_id):
        super(ATK, self).__init__()
    def serialize(self):
        """Convert pointer to object for serialization"""
