""" Service requests for accessible objects """

from flask import Flask, render_template, request, jsonify
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

@APP.route("/MSAA")
def retrieve_msaa_accessible():
    """
    Retrieve accessible through MSAA API with given ID
    """
    _id = request.args.get('id')
    _depth = int(request.args.get('depth'))
    msaa_json = MSAA_Schema().dump(accessible('MSAA', _id, _depth))
    pprint(msaa_json.data, indent=2)
    return jsonify(msaa_json.data)

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

# Serialize Accessible Object to JSON
# ACC_JSON = jsonpickle.encode(ACC_OBJ)
# print ACC_JSON
