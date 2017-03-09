"""Create platform utility object"""

import sys
from ..utils.WinUtil import WinUtil
from ..utils.LinuxUtil import LinuxUtil
from ..utils.MacUtil import MacUtil

def util():
    """Instantiate the platform utility"""
    platform = sys.platform
    os_t = {
        'win32': WinUtil,
        'linux': LinuxUtil,
        'darwin': MacUtil,
    }
    return os_t[platform]()
    