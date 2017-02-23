""" Service requests for accessible objects """

from flask import Flask, render_template, request, jsonify, abort, make_response
from marshmallow import pprint
from accessible_lib.scripts.serialize import MSAA_Schema
from accessible_lib.scripts.accessible import accessible

APP = Flask(__name__)

@APP.route('/')
def api_root():
    """
    Welcome page for Accessible Wrapper Service
    """
    return render_template('index.html')

@APP.route("/accessible")
def retrieve_msaa_accessible():
    """
    Retrieve accessible through MSAA API with given ID
    """
    # Get id and depth paramaters
    _id = request.args.get('id')
    _depth = int(request.args.get('depth'))
    _acc_obj = accessible('MSAA', _id, _depth)

    # Display serialized object or error if not found
    if _acc_obj.found:
        msaa_json = MSAA_Schema().dump(_acc_obj)
        pprint(msaa_json.data, indent=2)
        return jsonify(msaa_json.data)
    else:
        error = make_response(_acc_obj.error, 404)
        return abort(error)

@APP.route("/event")
def retrieve_event():
    """
    Retrieve event associated with accessible
    """
    return "HI"

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

