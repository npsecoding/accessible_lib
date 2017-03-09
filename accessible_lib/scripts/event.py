"""Create EventHandler object"""

from platform import system
from ..events.WinEventHandler import WinEventHandler
from ..events.LinuxEventHandler import LinuxEventHandler
from ..events.MacEventHandler import MacEventHandler

def event(interface_t, event_t, _identifiers):
    """Instantiate EventHandler object"""
    protocol = {
        'Windows': WinEventHandler,
        'Linux': LinuxEventHandler,
        'Mac': MacEventHandler
    }
    return protocol[system()](interface_t, event_t, _identifiers)
    