"""Create Accessible object"""

from ctypes import POINTER
from ..scripts.constants import IAccessible_t, IAccessible2_t, IATK_t, IATSPI_t
from ..wrappers.atk import ATK
from ..wrappers.atspi import ATSPI
from ..wrappers.IAccessible2 import IAccessible2
from ..wrappers.IAccessible import IAccessible

def interface_ptr_types():
    """Return supported interface pointer types"""
    return [POINTER(IATK_t), POINTER(IATSPI_t), POINTER(IAccessible_t), POINTER(IAccessible2_t)]

def accessible(interface_t, identifiers):
    """Instantiate the accessible object"""
    protocol = {
        'ATK': ATK,
        'ATSPI': ATSPI,
        'IAccessible2': IAccessible2,
        'IAccessible': IAccessible
    }
    return protocol[interface_t](identifiers)
    