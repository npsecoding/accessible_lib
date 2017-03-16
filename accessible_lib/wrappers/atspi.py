"""ATSPI"""

from .NsIAccessible import NsIAccessible

class ATSPI(NsIAccessible):
    """ATSPI linux protocol"""
    def __init__(self, identifiers):
        super(ATSPI, self).__init__()
    def serialize(self, child_depth):
        """Convert pointer to object for serialization"""
