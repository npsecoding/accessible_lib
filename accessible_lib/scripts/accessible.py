"""Create Accessible object"""

from ..wrappers.atk import ATK
from ..wrappers.atspi import ATSPI
from ..wrappers.ia2 import IA2
from ..wrappers.IAccessible import IAccessible

def accessible(atp, acc_id):
    """Instantiate the accessible object"""
    protocol = {
        'ATK': ATK,
        'ATSPI': ATSPI,
        'IA2': IA2,
        'IAccessible': IAccessible
    }
    return protocol[atp](acc_id)
    