""" Issue commands to accessible"""

from .accessible import accessible
from .constants import CHILDID_SELF

def execute_command(interface_t, identifiers, cmd):
    """Execute command on accessible object and returns value"""
    value = None
    acc_obj = accessible(interface_t, identifiers)
    _json = acc_obj.serialize()

    # Get childid for object or simple element
    childid = CHILDID_SELF
    if acc_obj._target.isSimpleElement:
        childid = acc_obj._target.childId

    if cmd in _json:
        value = _json[cmd]
    elif str(cmd).capitalize() in _json:
        value = _json[str(cmd).capitalize()]
    else:
        try:
            prefix = 'acc'
            value = getattr(acc_obj._target, prefix + cmd)(childid)
        except AttributeError:
            value = "ERROR"

    return value
