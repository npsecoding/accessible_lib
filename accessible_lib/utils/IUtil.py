"""Interface for Platform Utilities"""

class IUtil(object):
    """Utility Inteface Definition"""
    def __init__(self):
        pass

    def get_root_accessible(self):
        """Gets the root accessible object"""
        raise NotImplementedError

    def get_target_accessible(self):
        """Gets the target accessible object"""
        raise NotImplementedError

    def traverse_accessible(self):
        """Helper to traverse accessible tree"""
        """TODO"""
