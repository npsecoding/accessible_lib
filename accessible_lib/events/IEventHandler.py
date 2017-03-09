"""Interface for EventHandler Object"""

class IEventHandler(object):
    """EventHandler Object Interface Definition"""
    def __init__(self):
        self.info = {
            'INTERFACE' : None,
            'TARGET' : None,
            'FOUND' : None
        }

    def register_event_hook(self):
        """Track specific event"""
        raise NotImplementedError

    def unregesiter_event_hook(self):
        """Untrack specific event"""
        raise NotImplementedError

    def listen_events(self):
        """Listen for tracked events"""
        raise NotImplementedError

