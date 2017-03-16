"Represent WINEVENTS"

from ctypes import byref, wintypes, windll, oledll, POINTER, WINFUNCTYPE
from comtypes.client import PumpEvents
from comtypes.automation import VARIANT
from ..scripts.accessible import accessible
from ..events.IEventHandler import IEventHandler
from ..scripts.constants import *
from ..scripts.debug import DEBUG_ENABLED

INVALID_EVENT = -1

class WinEventHandler(IEventHandler):
    """Handle Windows Events"""
    # Store information about event used between callback and handler
    info = {}
    event_found = None

    # Helper function to find matching accessible from EVENT_CONSOLE_START_APPLICATION
    @staticmethod
    def _match_criteria(acc_ptr, search_criteria, child_id=CHILDID_SELF):
        for criteria in search_criteria:
            prefix = 'acc'
            prop_value = getattr(acc_ptr, prefix + criteria)(child_id)
            search_value = search_criteria[criteria]

            # If value is a number convert from unicode to int
            if isinstance(prop_value, int):
                search_value = int(search_value)

            if prop_value != search_value:
                return False

        return True

    # Callback function
    @staticmethod
    def accessible_from_event(hWinEventHook, event, hwnd, idObject, idChild, dwEventThread, dwmsEventTime):
        acc_ptr = POINTER(IAccessible_t)()
        var_child = VARIANT()
        result = oledll.oleacc.AccessibleObjectFromEvent(
            hwnd, idObject, idChild, byref(acc_ptr), byref(var_child))
        if S_OK != result:
            return

        if DEBUG_ENABLED:
            print acc_ptr.accName(idChild)

        _identifiers = WinEventHandler.info['IDENTIFIERS']
        if WinEventHandler._match_criteria(acc_ptr, _identifiers, idChild):
            _interface = WinEventHandler.info['INTERFACE']
            WinEventHandler.event_found = {
                'Child_Id' : idChild,
                _interface : accessible(_interface, _identifiers).serialize(0)
            }

    # Callback type
    WINPROC_TYPE = WINFUNCTYPE(
        None,
        wintypes.HANDLE,
        wintypes.DWORD,
        wintypes.HWND,
        wintypes.LONG,
        wintypes.LONG,
        wintypes.DWORD,
        wintypes.DWORD
    )

    # Declare callback function
    WINEVENT_PROC = WINPROC_TYPE(accessible_from_event.__func__)

    def register_event(self, event_start, event_end):
        """Set hook for event"""
        hook_result = windll.user32.SetWinEventHook(
            event_start,
            event_end,
            None,
            self.WINEVENT_PROC,
            0,
            0,
            WINEVENT_OUTOFCONTEXT
        )
        return hook_result

    def __init__(self, interface_t, event_t, _identifiers):
        super(WinEventHandler, self).__init__(interface_t, _identifiers)
        WinEventHandler.info = self.info
        WinEventHandler.event_found = None

        self.hook = self.register_event_hook(event_t)
        print 'Registed ' + event_t + ' hook'
        if self.hook != INVALID_EVENT:
            self.listen_events()

    def register_event_hook(self, event):
        """Register callback for event type"""

        if event in WIN_EVENT_NAMES.values():
            event_index = WIN_EVENT_NAMES.values().index(event)
            event_type = WIN_EVENT_NAMES.keys()[event_index]
            return self.register_event(event_type, event_type)
        else:
            return INVALID_EVENT

    def unregesiter_event_hook(self):
        """Unregister callback for event type"""
        result = windll.user32.UnhookWinEvent(self.hook)
        return result

    def listen_events(self):
        """Get registered events and trigger callback"""
        PumpEvents(TIMEOUT)
        self.unregesiter_event_hook()
