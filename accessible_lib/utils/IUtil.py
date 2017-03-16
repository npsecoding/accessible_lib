"""Interface for Platform Utilities"""

class IUtil(object):
    """Utility Inteface Definition"""
    def __init__(self):
        pass

    def get_root_accessible(self):
        """Gets the root accessible object"""
        raise NotImplementedError

    def get_target_accessible(self, search_criteria):
        """Gets the target accessible object"""
        raise NotImplementedError

