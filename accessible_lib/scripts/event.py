"Represent WINEVENTS"

from threading import Thread, Timer
from ctypes import byref, wintypes, windll, oledll, POINTER, WINFUNCTYPE
from comtypes.automation import VARIANT
from constants import *

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

# Callback function
def win_callback(hWinEventHook, event, hwnd, idObject, idChild, dwEventThread, dwmsEventTime):
        acc_ptr = POINTER(IAccessible_t)()
        var_child = VARIANT()
        result = oledll.oleacc.AccessibleObjectFromEvent(
            hwnd, idObject, idChild, byref(acc_ptr), byref(var_child))
        if S_OK != result:
            return
        print "Name: " + str(acc_ptr.accName(CHILDID_SELF)).encode('ascii', 'ignore')

class EventHandler(object):
    winproc_type = WINPROC_TYPE(win_callback)

    def register_event(self, event_start, event_end):
        print "Set hook for event"
        hook_result = windll.user32.SetWinEventHook(
            event_start,
            event_end,
            None,
            self.winproc_type,
            0,
            0,
            WINEVENT_OUTOFCONTEXT
        )
        return hook_result

    def __init__(self):
        self.hook = None

    def register_event_hook(self, event):
        event_index = WIN_EVENT_NAMES.values().index(event)
        event_type = WIN_EVENT_NAMES.keys()[event_index]
        self.hook = self.register_event(event_type, event_type)

    def unregesiter_event_hook(self):
        result = windll.user32.UnhookWinEvent(self.hook)
        return result




