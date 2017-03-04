"""Create Accessible object"""

from ..wrappers.atk import ATK
from ..wrappers.atspi import ATSPI
from ..wrappers.IAccessible2 import IAccessible2
from ..wrappers.IAccessible import IAccessible

def accessible(atp, acc_id):
    """Instantiate the accessible object"""
    protocol = {
        'ATK': ATK,
        'ATSPI': ATSPI,
        'IAccessible2': IAccessible2,
        'IAccessible': IAccessible
    }
    return protocol[atp](acc_id)
    