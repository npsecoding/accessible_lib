"""Create platform utility object"""

import sys
from ..utils.win import WinUtil
from ..utils.linux import LinuxUtil
from ..utils.mac import MacUtil

def util():
    """Instantiate the platform utility"""
    platform = sys.platform
    os_t = {
        'win32': WinUtil,
        'linux': LinuxUtil,
        'darwin': MacUtil,
    }
    return os_t[platform]()
    