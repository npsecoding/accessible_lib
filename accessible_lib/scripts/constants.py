"""Accessibility Constants"""

from comtypes import IServiceProvider
from comtypes.gen.Accessibility import IAccessible
from comtypes.gen.IAccessible2Lib import IAccessible2

TIMEOUT = 10

CHILDID_SELF = 0x0
S_OK = 0x0

VT_I4 = 0x3
VT_DISPATCH = 0x9

FULL_CHILD_TREE = -1

IServiceProvider_t = IServiceProvider
IID_IServiceProvider = IServiceProvider._iid_

IAccessible_t = IAccessible
IID_IAccessible = IAccessible._iid_

IAccessible2_t = IAccessible2
IID_IAccessible2 = IAccessible2._iid_

#TODO
IATK_t = None
IATSPI_t = None

OBJID_WINDOW = 0x00000000
OBJID_SELF = 0x00000000
OBJID_SYSMENU = 0xFFFFFFFF
OBJID_TITLEBAR = 0xFFFFFFFE
OBJID_MENU = 0xFFFFFFFD
OBJID_CLIENT = 0xFFFFFFFC
OBJID_VSCROLL = 0xFFFFFFFB
OBJID_HSCROLL = 0xFFFFFFFA
OBJID_SIZEGRIP = 0xFFFFFFF9
OBJID_CARET = 0xFFFFFFF8
OBJID_CURSOR = 0xFFFFFFF7
OBJID_ALERT = 0xFFFFFFF6
OBJID_SOUND = 0xFFFFFFF5
OBJID_QUERYCLASSNAMEIDX = 0xFFFFFFF4
OBJID_NATIVEOM = 0xFFFFFFF0

ROLE_SYSTEM_TITLEBAR = 0x00000001
ROLE_SYSTEM_MENUBAR = 0x00000002
ROLE_SYSTEM_SCROLLBAR = 0x00000003
ROLE_SYSTEM_GRIP = 0x00000004
ROLE_SYSTEM_SOUND = 0x00000005
ROLE_SYSTEM_CURSOR = 0x00000006
ROLE_SYSTEM_CARET = 0x00000007
ROLE_SYSTEM_ALERT = 0x00000008
ROLE_SYSTEM_WINDOW = 0x00000009
ROLE_SYSTEM_CLIENT = 0x0000000A
ROLE_SYSTEM_MENUPOPUP = 0x0000000B
ROLE_SYSTEM_MENUITEM = 0x0000000C
ROLE_SYSTEM_TOOLTIP = 0x0000000D
ROLE_SYSTEM_APPLICATION = 0x0000000E
ROLE_SYSTEM_DOCUMENT = 0x0000000F
ROLE_SYSTEM_PANE = 0x00000010
ROLE_SYSTEM_CHART = 0x00000011
ROLE_SYSTEM_DIALOG = 0x00000012
ROLE_SYSTEM_BORDER = 0x00000013
ROLE_SYSTEM_GROUPING = 0x00000014
ROLE_SYSTEM_SEPARATOR = 0x00000015
ROLE_SYSTEM_TOOLBAR = 0x00000016
ROLE_SYSTEM_STATUSBAR = 0x00000017
ROLE_SYSTEM_TABLE = 0x00000018
ROLE_SYSTEM_COLUMNHEADER = 0x00000019
ROLE_SYSTEM_ROWHEADER = 0x0000001A
ROLE_SYSTEM_COLUMN = 0x0000001B
ROLE_SYSTEM_ROW = 0x0000001C
ROLE_SYSTEM_CELL = 0x0000001D
ROLE_SYSTEM_LINK = 0x0000001E
ROLE_SYSTEM_HELPBALLOON = 0x0000001F
ROLE_SYSTEM_CHARACTER = 0x00000020
ROLE_SYSTEM_LIST = 0x00000021
ROLE_SYSTEM_LISTITEM = 0x00000022
ROLE_SYSTEM_OUTLINE = 0x00000023
ROLE_SYSTEM_OUTLINEITEM = 0x00000024
ROLE_SYSTEM_PAGETAB = 0x00000025
ROLE_SYSTEM_PROPERTYPAGE = 0x00000026
ROLE_SYSTEM_INDICATOR = 0x00000027
ROLE_SYSTEM_GRAPHIC = 0x00000028
ROLE_SYSTEM_STATICTEXT = 0x00000029
ROLE_SYSTEM_TEXT = 0x0000002A
ROLE_SYSTEM_PUSHBUTTON = 0x0000002B
ROLE_SYSTEM_CHECKBUTTON = 0x0000002C
ROLE_SYSTEM_RADIOBUTTON = 0x0000002D
ROLE_SYSTEM_COMBOBOX = 0x0000002E
ROLE_SYSTEM_DROPLIST = 0x0000002F
ROLE_SYSTEM_PROGRESSBAR = 0x00000030
ROLE_SYSTEM_DIAL = 0x00000031
ROLE_SYSTEM_HOTKEYFIELD = 0x00000032
ROLE_SYSTEM_SLIDER = 0x00000033
ROLE_SYSTEM_SPINBUTTON = 0x00000034
ROLE_SYSTEM_DIAGRAM = 0x00000035
ROLE_SYSTEM_ANIMATION = 0x00000036
ROLE_SYSTEM_EQUATION = 0x00000037
ROLE_SYSTEM_BUTTONDROPDOWN = 0x00000038
ROLE_SYSTEM_BUTTONMENU = 0x00000039
ROLE_SYSTEM_BUTTONDROPDOWNGRID = 0x0000003A
ROLE_SYSTEM_WHITESPACE = 0x0000003B
ROLE_SYSTEM_PAGETABLIST = 0x0000003C
ROLE_SYSTEM_CLOCK = 0x0000003D

STATE_SYSTEM_FLOATING = 0x00001000
STATE_SYSTEM_FOCUSED = 0x4
STATE_SYSTEM_MOVEABLE = 0x00040000
STATE_SYSTEM_CHECKED = 0x10
STATE_SYSTEM_MIXED = 0x20
STATE_SYSTEM_UNAVAILABLE = 0x0001
STATE_SYSTEM_INVISIBLE = 0x8000
STATE_SYSTEM_OFFSCREEN = 0x010000
STATE_SYSTEM_PRESSED = 0x8
STATE_SYSTEM_SIZEABLE = 0x00020000
STATE_SYSTEM_HOTTRACKED = 0x00000080
STATE_SYSTEM_BUSY = 0x00000800

SELFLAG_NONE = 0
SELFLAG_TAKEFOCUS = 0x1
SELFLAG_TAKESELECTION = 0x2
SELFLAG_EXTENDSELECTION = 0x4
SELFLAG_ADDSELECTION = 0x8
SELFLAG_REMOVESELECTION = 0x10

WINEVENT_OUTOFCONTEXT = 0x0
WINEVENT_SKIPOWNTHREAD = 0x1
WINEVENT_SKIPOWNPROCESS = 0x2
WINEVENT_INCONTEXT = 0x4

EVENT_MIN = 0x00000001
EVENT_MAX = 0x7FFFFFFF
EVENT_SYSTEM_SOUND = 0x1
EVENT_SYSTEM_ALERT = 0x2
EVENT_SYSTEM_FOREGROUND = 0x3
EVENT_SYSTEM_MENUSTART = 0x4
EVENT_SYSTEM_MENUEND = 0x5
EVENT_SYSTEM_MENUPOPUPSTART = 0x6
EVENT_SYSTEM_MENUPOPUPEND = 0x7
EVENT_SYSTEM_CAPTURESTART = 0x8
EVENT_SYSTEM_CAPTUREEND = 0x9
EVENT_SYSTEM_MOVESIZESTART = 0xa
EVENT_SYSTEM_MOVESIZEEND = 0xb
EVENT_SYSTEM_CONTEXTHELPSTART = 0xc
EVENT_SYSTEM_CONTEXTHELPEND = 0xd
EVENT_SYSTEM_DRAGDROPSTART = 0xe
EVENT_SYSTEM_DRAGDROPEND = 0xf
EVENT_SYSTEM_DIALOGSTART = 0x10
EVENT_SYSTEM_DIALOGEND = 0x11
EVENT_SYSTEM_SCROLLINGSTART = 0x12
EVENT_SYSTEM_SCROLLINGEND = 0x13
EVENT_SYSTEM_SWITCHSTART = 0x14
EVENT_SYSTEM_SWITCHEND = 0x15
EVENT_SYSTEM_MINIMIZESTART = 0x16
EVENT_SYSTEM_MINIMIZEEND = 0x17
EVENT_OBJECT_CREATE = 0x8000
EVENT_OBJECT_DESTROY = 0x8001
EVENT_OBJECT_SHOW = 0x8002
EVENT_OBJECT_HIDE = 0x8003
EVENT_OBJECT_REORDER = 0x8004
EVENT_OBJECT_FOCUS = 0x8005
EVENT_OBJECT_SELECTION = 0x8006
EVENT_OBJECT_SELECTIONADD = 0x8007
EVENT_OBJECT_SELECTIONREMOVE = 0x8008
EVENT_OBJECT_SELECTIONWITHIN = 0x8009
EVENT_OBJECT_STATECHANGE = 0x800a
EVENT_OBJECT_LOCATIONCHANGE = 0x800b
EVENT_OBJECT_NAMECHANGE = 0x800c
EVENT_OBJECT_DESCRIPTIONCHANGE = 0x800d
EVENT_OBJECT_VALUECHANGE = 0x800e
EVENT_OBJECT_PARENTCHANGE = 0x800f
EVENT_OBJECT_HELPCHANGE = 0x8010
EVENT_OBJECT_DEFACTIONCHANGE = 0x8011
EVENT_OBJECT_ACCELERATORCHANGE = 0x8012
EVENT_CONSOLE_CARET = 0x4001
EVENT_CONSOLE_UPDATE_REGION = 0x4002
EVENT_CONSOLE_UPDATE_SIMPLE = 0x4003
EVENT_CONSOLE_UPDATE_SCROLL = 0x4004
EVENT_CONSOLE_LAYOUT = 0x4005
EVENT_CONSOLE_START_APPLICATION = 0x4006
EVENT_CONSOLE_END_APPLICATION = 0x4007

WIN_EVENT_NAMES = {}
for _sym, _val in locals().items():
    if _sym.startswith('EVENT_'):
        WIN_EVENT_NAMES[_val] = _sym
