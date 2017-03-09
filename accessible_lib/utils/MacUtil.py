"""Utility for Mac Platform"""

from .IUtil import IUtil

class MacUtil(IUtil):
    """Utility definition for Mac Platform"""
    def __init__(self):
        super(MacUtil, self).__init__()

    def get_root_accessible(self):
        """TODO"""

    def get_target_accessible(self, search_criteria):
        """TODO"""
