""" Service requests for accessible objects """

from flask import Flask, render_template, request, jsonify
from accessible_lib.scripts.accessible import accessible
from accessible_lib.scripts.commands import execute_command
from accessible_lib.scripts.event import EventHandler

APP = Flask(__name__)

@APP.route('/')
def api_root():
    """
    Welcome page for Accessible Wrapper Service
    """
    return render_template('index.html')

@APP.route("/accessible")
def retrieve_accessible():
    """
    Retrieve accessible through API with given ID
    """
    # Get id and depth paramaters
    _at = request.args.get('type')
    _id = request.args.get('id')
    _depth = int(request.args.get('depth'))
    _acc_obj = accessible(_at, _id)

    # Display serialized object or error if not found
    if _acc_obj.found:
        json = _acc_obj.serialize(_depth)
        return jsonify(json), 200
    else:
        return jsonify({'ERROR' : _acc_obj.error}), 404

@APP.route("/event")
def retrieve_event():
    """
    Retrieve event associated with accessible
    """
    # Get id and type paramaters
    _id = request.args.get('id')
    _type = request.args.get('type')
    _event = request.args.get('event')

    EventHandler(_type, _event, _id)
    event_result = EventHandler.INFO['FOUND']

    if event_result is not None:
        return jsonify(event_result), 200
    else:
        return jsonify({'ERROR:': 'TIMEOUT'}), 404

@APP.route("/cmd")
def retrieve_command():
    """
    Execute command on accessible
    """
     # Get id and function paramaters
    _at = request.args.get('type')
    _id = request.args.get('id')
    _function = request.args.get('function')
    _value = execute_command(_at, _id, _function)
    _field = _function.replace('acc', '')

    # Display value returned from command or error
    if _value is not "ERROR":
        return jsonify({_field : _value}), 200
    else:
        return jsonify({'ERROR' : "No Command Found"}), 404

if __name__ == '__main__':
    APP.run()

#--------------------------------------------
# FOR TESTING
#--------------------------------------------
# Retrieve the corresponding Accessible Object
# ACC_OBJ = accessible('MSAA', "Navigation Toolbar")
# print ACC_OBJ.get_acc_name()
# print ACC_OBJ.get_acc_role()
# print ACC_OBJ.get_acc_value()

