"""Utility for Windows Platform"""

from ctypes import windll, oledll, byref, POINTER
from ctypes.wintypes import c_char_p, c_long
from comtypes.automation import VARIANT
from ..scripts.constants import *
from ..scripts.debug import *
from ..utils.IUtil import IUtil

class WinUtil(IUtil):
    """
    Utility definition for Windows Platform
    """

    def __init__(self):
        super(WinUtil, self).__init__()
        self._root = None
        self._target = None
        self._simple_elements = dict()
        self.get_root_accessible()

    def _accessible_object_from_window(self, hwnd):
        """
        Get the accessible object for window
        """
        acc_ptr = POINTER(IAccessible_t)()
        res = oledll.oleacc.AccessibleObjectFromWindow(
            hwnd, OBJID_WINDOW, byref(IID_IAccessible), byref(acc_ptr))

        if res == S_OK:
            acc_ptr.children = self._accessible_children(acc_ptr)
            return acc_ptr
        else:
            raise ValueError("Can't get accessible from window")

    def _accessible_children(self, accptr):
        """
        Get the children of an accessible object
        """
        ichild_start = 0
        cc_children = accptr.accChildCount
        pc_obtained = c_long()
        variant_array_type = VARIANT * cc_children
        rgvar_children = variant_array_type()
        res = oledll.oleacc.AccessibleChildren(
            accptr, ichild_start, cc_children, byref(rgvar_children), byref(pc_obtained))

        if res == S_OK:
            acc_objs = []
            for child in rgvar_children:
                # Child is IAccessible
                if child.vt == VT_DISPATCH:
                    acc = child.value.QueryInterface(IAccessible_t)
                    acc_objs.append(acc)
                # Child is Simple Element
                elif child.vt == VT_I4:
                    self._wrap_simple_element(accptr, child.value)
            return acc_objs
        else:
            raise ValueError("Can't get accessible children")

    def _wrap_simple_element(self, accptr, childid):
        """
        Associate simple element and parent accessible object
        """
        if accptr not in self._simple_elements:
            self._simple_elements[accptr] = [childid]
        else:
            self._simple_elements[accptr].append(childid)

    def _traverse(self, node, acc_id, visited):
        """
        Traverse through accessible tree looking for node with the given ID
        """
        if node.accName(CHILDID_SELF) == acc_id:
            self._target = node
            return

        # print_accessible(node)

        # Traverse through simple elements of accessible object
        # if node in self._simple_elements:
        #     for childid in self._simple_elements[node]:
        #         print_simple(node, childid)

        # Traverse through each accessible object's children
        for child in self._accessible_children(node):
            if child not in visited:
                visited.add(node)
                self._traverse(child, acc_id, visited)

    def _get_test_window(self):
         # Get the window for browser
        test_class = c_char_p("MozillaWindowClass")
        current_hwnd = windll.user32.FindWindowA(test_class, None)
        name = self._accessible_object_from_window(current_hwnd).accName(CHILDID_SELF)

        # Iterate through windows
        while name is None or 'Nightly' not in name:
            current_hwnd = windll.user32.FindWindowExA(None, current_hwnd, test_class, None)
            name = self._accessible_object_from_window(current_hwnd).accName(CHILDID_SELF)

        return current_hwnd

    def get_root_accessible(self):
        """
        Set root accessible object to test window
        """
        test_window = self._get_test_window()
        print 'Test Window: %d' %test_window
        self._root = self._accessible_object_from_window(test_window)
        return self._root

    def get_target_accessible(self, acc_id):
        """
        Retrieve the accessible object for the given ID
        """
        visited = set()
        visited.add(self._root)
        self._traverse(self._root, acc_id, visited)
        return self._target
