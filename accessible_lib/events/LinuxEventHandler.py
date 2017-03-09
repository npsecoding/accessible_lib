from ..events.IEventHandler import IEventHandler

class LinuxEventHandler(IEventHandler):
    """Handle Linux Events"""

    def __init__(self, interface_t, event_t, _identifiers):
        # TODO
        super(LinuxEventHandler, self).__init__(interface_t, _identifiers)
        raise NotImplementedError

    def register_event_hook(self):
        """Track specific event"""
        # TODO
        raise NotImplementedError

    def unregesiter_event_hook(self):
        """Untrack specific event"""
        # TODO
        raise NotImplementedError

    def listen_events(self):
        """Listen for tracked events"""
        # TODO
        raise NotImplementedError
