""" Service requests for accessible objects """

from flask import Flask, render_template, request, jsonify
from accessible_lib.scripts.accessible import accessible
from accessible_lib.scripts.commands import execute_command
from accessible_lib.scripts.event import event

APP = Flask(__name__)

@APP.route("/accessible")
def retrieve_accessible():
    """
    Retrieve accessible through API with given ID
    """
    # Get id and depth paramaters
    _name = request.args.get('name')
    _role = request.args.get('role')
    _identifiers = {}
    if _name is not None:
        _identifiers["Name"] = _name
    if _role is not None:
        _identifiers["Role"] = _role

    _inteface = request.args.get('interface')
    _depth = request.args.get('depth')
    _acc_obj = accessible(_inteface, _identifiers)

    # Display serialized object or error if not found
    if _acc_obj.found:
        _json = _acc_obj.serialize(_depth)
        return jsonify({_inteface : _json}), 200
    else:
        error = {
            'Message' : 'No accessible found with given parameters',
            'Query Params': _identifiers
            }
        return jsonify({'ERROR': error}), 404

@APP.route("/event")
def retrieve_event():
    """
    Retrieve event associated with accessible
    """
    # Get id and event paramaters
    _name = request.args.get('name')
    _role = request.args.get('role')
    _identifiers = {}
    if _name is not None:
        _identifiers["Name"] = _name
    if _role is not None:
        _identifiers["Role"] = _role

    _interface = request.args.get('interface')
    _event = request.args.get('event')
    _event_handler = event(_interface, _event, _identifiers)
    event_result = _event_handler.event_found

    if event_result is not None:
        return jsonify(event_result), 200
    else:
        _query_params = {
            'Interface': _interface,
            'Props': _identifiers,
            'Event': _event
        }
        error = {
            'Message' : "Event not found on Accessible",
            'Query Params': _query_params
        }
        return jsonify({'ERROR': error}), 404

@APP.route("/cmd")
def retrieve_command():
    """
    Execute command on accessible
    """
    # Get id and function paramaters
    _name = request.args.get('name')
    _role = request.args.get('role')
    _identifiers = {}
    if _name is not None:
        _identifiers["Name"] = _name
    if _role is not None:
        _identifiers["Role"] = _role

    _interface = request.args.get('interface')
    _function = request.args.get('function')
    _params = request.args.getlist('param')
    _value = execute_command(_interface, _identifiers, _function, _params)

    # Display value returned from command or error
    if _value is not "ERROR":
        return jsonify({_function : _value}), 200
    else:
        _query_params = {
            'Interface': _interface,
            'Props': _identifiers,
            'Function': _function,
            'Function Params': _params
        }
        error = {
            'Message' : "Function couldn't be executed with given parameters",
            'Query Params': _query_params
            }
        return jsonify({'ERROR': error}), 404

if __name__ == '__main__':
    APP.run()

