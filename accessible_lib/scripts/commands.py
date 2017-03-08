""" Issue commands to accessible"""

from .accessible import accessible

def execute_command(interface_t, identifiers, cmd):
    """Execute command on accessible object and returns value"""
    value = None
    acc_obj = accessible(interface_t, identifiers)
    _json = acc_obj.serialize()

    if cmd in _json:
        value = _json[cmd]
    elif str(cmd).capitalize() in _json:
        value = _json[str(cmd).capitalize()]
    else:
        value = "ERROR"

    return value


