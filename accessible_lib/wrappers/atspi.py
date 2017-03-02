"""ATSPI"""

from .NsIAccessible import NsIAccessible

class ATSPI(NsIAccessible):
    """ATSPI linux protocol"""
    def __init__(self, acc_id):
        super(ATSPI, self).__init__()
    def serialize(self):
        """Convert pointer to object for serialization"""
