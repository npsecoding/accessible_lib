"""Utility for Windows Platform"""

from ctypes import windll, oledll, byref, POINTER
from ctypes.wintypes import c_char_p, c_void_p, c_long
from comtypes.automation import VARIANT
from ..scripts.constants import *
from ..utils.IUtil import IUtil

class WinUtil(IUtil):
    """Utility definition for Windows Platform"""

    def __init__(self):
        super(WinUtil, self).__init__()
        self._root = None
        self._target = None
        self._simple_elements = dict()
        self._set_test_window()

    def _set_test_window(self):
        """Get the window for the browser"""
        test_class = c_char_p("MozillaWindowClass")
        self._test_window = windll.user32.FindWindowA(test_class, None)
        print 'Test Window: %d' %self._test_window

    def _get_desktop_window(self):
        """Get the accessible object for the desktop window"""
        desktop_window = windll.user32.GetDesktopWindow()
        return desktop_window

    def _window_from_accessible_object(self, acc_ptr):
        """Get window of accessible object"""
        hwnd = c_long()
        oledll.oleacc.WindowFromAccessibleObject(acc_ptr, byref(hwnd))
        return hwnd.value

    def _accessible_object_from_window(self, hwnd):
        """Get the accessible object for window"""
        acc_ptr = POINTER(IAccessible_t)()
        res = oledll.oleacc.AccessibleObjectFromWindow(
            hwnd, OBJID_WINDOW, byref(IID_IAccessible), byref(acc_ptr))
        if res == S_OK:
            acc_ptr.children = self._accessible_children(acc_ptr)
            return acc_ptr
        else:
            raise ValueError("Can't get accessible from window")

    def _accessible_children(self, accptr):
        """Get the children of an accessible object"""
        ichild_start = 0
        cc_children = accptr.accChildCount
        pc_obtained = c_long()
        variant_array_type = VARIANT * cc_children
        rgvar_children = variant_array_type()
        res = oledll.oleacc.AccessibleChildren(
            accptr, ichild_start, cc_children, byref(rgvar_children), byref(pc_obtained))

        # Get IAccessible objects
        acc_objs = []
        for child in rgvar_children:
            if child.vt == VT_DISPATCH:
                acc = child.value.QueryInterface(IAccessible_t)
                acc_objs.append(acc)
            elif child.vt == VT_I4:
                acc_objs.append(accptr)
                self._wrap_simple_element(accptr, child.value)
        return acc_objs

    def _wrap_simple_element(self, accptr, childid):
        if accptr not in self._simple_elements:
            self._simple_elements[accptr] = [childid]
        else:
            self._simple_elements[accptr].append(childid)

    def _traverse(self, node, acc_id, visited):
        if node.accName(CHILDID_SELF) == acc_id:
            self._target = node
            return

        print '--------------------------'
        print 'Accessible Object'
        print node
        print 'Name: %s' %node.accName(CHILDID_SELF)
        print 'Role: %s' %node.accRole(CHILDID_SELF)
        print '--------------------------'

        if node in self._simple_elements:
            for childid in self._simple_elements[node]:
                print '--------------------------'
                print 'Simple Element'
                print 'Owner:%s' %node
                print 'Name: %s' %node.accName(childid)
                print 'Role: %s' %node.accRole(childid)
                print '--------------------------'

        for child in self._accessible_children(node):
            if child not in visited:
                visited.add(node)
                self._traverse(child, acc_id, visited)

    def get_root_accessible(self):
        self._root = self._accessible_object_from_window(self._test_window)
        return self._root

    def get_target_accessible(self, acc_id):
        visited = set()
        visited.add(self._root)
        self._traverse(self._root, acc_id, visited)
        return self._target

