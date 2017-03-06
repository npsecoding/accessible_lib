"""ATK"""

from .NsIAccessible import NsIAccessible

class ATK(NsIAccessible):
    """ATK linux protocol"""
    def __init__(self, identifiers):
        super(ATK, self).__init__()
    def serialize(self, child_depth):
        """Convert pointer to object for serialization"""
