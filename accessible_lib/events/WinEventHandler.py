"Represent WINEVENTS"

from ctypes import byref, wintypes, windll, oledll, POINTER, WINFUNCTYPE
from comtypes.automation import VARIANT
from ..scripts.accessible import accessible
from ..events.IEventHandler import IEventHandler
from ..scripts.constants import *

class WinEventHandler(IEventHandler):
    """Handle Windows Events"""
    # Store information about event used between callback and handler
    INFO = {}

    # Helper function to find matching accessible from EVENT_CONSOLE_START_APPLICATION
    @staticmethod
    def _match_criteria(acc_ptr, search_criteria, child_id=CHILDID_SELF):
        for criteria in search_criteria:
            prefix = 'acc'
            print criteria
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

        _identifiers = WinEventHandler.INFO['TARGET']
        if WinEventHandler._match_criteria(acc_ptr, _identifiers, idChild):
            windll.user32.PostQuitMessage(0x0012)
            _interface = WinEventHandler.INFO['INTERFACE']
            WinEventHandler.INFO['FOUND'] = {
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
        super(WinEventHandler, self).__init__()
        self.info['INTERFACE'] = interface_t
        self.info['TARGET'] = _identifiers
        WinEventHandler.INFO = self.info

        self.hook = self.register_event_hook(event_t)
        self.listen_events()

    def register_event_hook(self, event):
        """Register callback for event type"""
        event_index = WIN_EVENT_NAMES.values().index(event)
        event_type = WIN_EVENT_NAMES.keys()[event_index]
        return self.register_event(event_type, event_type)

    def unregesiter_event_hook(self):
        """Unregister callback for event type"""
        result = windll.user32.UnhookWinEvent(self.hook)
        return result

    def listen_events(self):
        """Get registered events and trigger callback"""
        timer_id = windll.user32.SetTimer(None, None, TIMEOUT, None)
        msg = wintypes.MSG()
        lpmsg = byref(msg)
        windll.user32.GetMessageA(lpmsg, None, 0, 0)
        windll.user32.KillTimer(None, timer_id)

        self.unregesiter_event_hook()
