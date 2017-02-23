""" Issue commands to accessible"""

from .accessible import accessible
from .constants import CHILDID_SELF

def execute_command(acc_id, cmd):
    value = None
    try:
        acc_obj = accessible('MSAA', acc_id, -1)
        value = getattr(acc_obj._target, cmd)(CHILDID_SELF)
    except AttributeError:
        value = "error"
    return value



