"Represent WINEVENTS"

from ctypes import byref, wintypes, windll, oledll, POINTER, WINFUNCTYPE
from comtypes.automation import VARIANT
from .accessible import accessible
from constants import *

class EventHandler(object):

    # Store information about event used between callback and handler
    INFO = {}

    # Callback function
    @staticmethod
    def accessible_from_event(hWinEventHook, event, hwnd, idObject, idChild, dwEventThread, dwmsEventTime):
        acc_ptr = POINTER(IAccessible_t)()
        var_child = VARIANT()
        result = oledll.oleacc.AccessibleObjectFromEvent(
            hwnd, idObject, idChild, byref(acc_ptr), byref(var_child))
        if S_OK != result:
            return
        acc_name = acc_ptr.accName(idChild)
        if acc_name:
            print acc_name
        if acc_name == EventHandler.INFO['TARGET']:
            windll.user32.PostQuitMessage(0x0012)
            EventHandler.INFO['FOUND'] = {
                'child_id' : idChild,
                'accessible' : accessible(EventHandler.INFO['PLATFORM'], acc_name).serialize(0)
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

    def __init__(self, platform, event_type, event_target):
        EventHandler.INFO = {
            'PLATFORM' : platform,
            'TARGET' : event_target,
            'FOUND' : None
        }

        self.hook = self.register_event_hook(event_type)
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
