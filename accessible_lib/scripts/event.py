"Represent WINEVENTS"

from ctypes import byref, wintypes, windll, oledll, POINTER, WINFUNCTYPE
from comtypes.automation import VARIANT
from comtypes.client import PumpEvents
from constants import *

EVENT_INFO = {
    'TARGET' : None,
    'FOUND' : False
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

# Callback function
def win_callback(hWinEventHook, event, hwnd, idObject, idChild, dwEventThread, dwmsEventTime):
    acc_ptr = POINTER(IAccessible_t)()
    var_child = VARIANT()
    result = oledll.oleacc.AccessibleObjectFromEvent(
        hwnd, idObject, idChild, byref(acc_ptr), byref(var_child))
    if S_OK != result:
        return
    acc_name = acc_ptr.accName(idChild)
    if acc_name:
        print acc_name
    if acc_name == EVENT_INFO['TARGET']:
        windll.user32.PostQuitMessage(0x0012)
        EVENT_INFO['FOUND'] = True

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

    def __init__(self, event_type, event_object):
        EVENT_INFO['TARGET'] = event_object
        EVENT_INFO['FOUND'] = False

        self.hook = self.register_event_hook(event_type)
        self.get_events()

    def register_event_hook(self, event):
        event_index = WIN_EVENT_NAMES.values().index(event)
        event_type = WIN_EVENT_NAMES.keys()[event_index]
        return self.register_event(event_type, event_type)

    def unregesiter_event_hook(self):
        result = windll.user32.UnhookWinEvent(self.hook)
        return result

    def get_events(self):
        timer_id = windll.user32.SetTimer(None, None, TIMEOUT, None)
        msg = wintypes.MSG()
        lpmsg = byref(msg)
        windll.user32.GetMessageA(lpmsg, None, 0, 0)
        windll.user32.KillTimer(None, timer_id)

        self.unregesiter_event_hook()

