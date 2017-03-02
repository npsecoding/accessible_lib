"""Interface for Accessible Object"""

from ..scripts.util import util

class NsIAccessible(object):
    """Accessible Object Interface Definition"""
    def __init__(self):
        self._util = util()
    def serialize(self):
        """Accessible Object to JSON"""
        raise NotImplementedError

