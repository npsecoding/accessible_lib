"""Create Accessible object"""

from ..wrappers.atk import ATK
from ..wrappers.atspi import ATSPI
from ..wrappers.ia2 import IA2
from ..wrappers.msaa import MSAA

def accessible(atp, acc_id, child_depth):
    """Instantiate the accessible object"""
    protocol = {
        'ATK': ATK,
        'ATSPI': ATSPI,
        'IA2': IA2,
        'MSAA': MSAA
    }
    return protocol[atp](acc_id, child_depth)
    