"""IAccessible2"""

from .NsIAccessible import NsIAccessible

class IAccessible2(NsIAccessible):
    """IA2 windows protocol"""
    def __init__(self, identifiers):
        super(IAccessible2, self).__init__()
        # Find accessible object associated with ID
        self._target = self._util.get_target_accessible(identifiers)
        ia2 = self._util.IAccessible_to_IAccessible2(self._target)
        print ia2

    def serialize(self, child_depth=-1):
        """Convert pointer to object for serialization"""
