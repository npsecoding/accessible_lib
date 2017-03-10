"""Utility for Linux Platform"""

from .IUtil import IUtil

class LinuxUtil(IUtil):
    """Utility definition for Linux Platform"""
    def __init__(self):
        super(LinuxUtil, self).__init__()

    def get_root_accessible(self):
        """TODO"""

    def get_target_accessible(self, search_criteria):
        """TODO"""
