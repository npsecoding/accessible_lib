""" Issue commands to accessible"""

from .accessible import accessible, interface_ptr_types

def execute_command(interface_t, identifiers, cmd, params):
    """Execute command on accessible object and returns value"""
    value = None
    acc_obj = accessible(interface_t, identifiers)
    if not acc_obj.found:
        value = "ERROR"
        return value

    _json = acc_obj.serialize()

    # Get accessible field from JSON
    if cmd in _json:
        value = _json[cmd]
    # Call accessible method
    else:
        # Localize paramaters
        localized_params = []
        for param in params:
            lparam = param.encode('UTF8')
            if lparam.isdigit():
                localized_params.append(int(lparam))
            else:
                localized_params.append(lparam)
        params = []
        params = localized_params

        try:
            prefix = 'acc'
            value = getattr(acc_obj._target, prefix + cmd)(*params)
        except:
            value = "ERROR"

    # Handles case when value is pointer by wrapping for serialization
    if type(value) in interface_ptr_types():
        return acc_obj.semantic_wrap(value)
    else:
        return value
