""" Service requests for accessible objects """

from flask import Flask, render_template, jsonify
import jsonpickle
from accessible_lib.scripts.accessible import accessible

APP = Flask(__name__)

@APP.route('/')
def api_root():
    """
    Welcome page for Accessible Wrapper Service
    """
    return render_template('index.html')

@APP.route("/MSAA/<key>")
def retrieve_msaa_accessible(key):
    """
    Retrieve accessible through MSAA API with given ID
    """
    msaa_json = jsonpickle.encode(accessible('MSAA', key), unpicklable=False)
    return jsonify(msaa_json)

# @APP.route("/IA2/<key>")
# def retrieve_ia2_accessible(key):
#     """
#     Retrieve accessible through IA2 API with given ID
#     """
#     jsonpickle.encode(accessible('IA2', key), unpicklable=False)

# @APP.route("/ATK/<key>")
# def retrieve_atk_accessible(key):
#     """
#     Retrieve accessible through ATK API given ID
#     """
#     jsonpickle.encode(accessible('ATK', key), unpicklable=False)

# @APP.route("/ATSPI/<key>")
# def retrieve_atspi_accessible(key):
#     """
#     Retrieve accessible through ATSPI API with given ID
#     """
#     jsonpickle.encode(accessible('ATSPI', key), unpicklable=False)

if __name__ == '__main__':
    APP.run()

#--------------------------------------------
# FOR TESTING
#--------------------------------------------
# Retrieve the corresponding Accessible Object
# ACC_OBJ = accessible('MSAA', "Browser tabs")
# print ACC_OBJ.get_acc_name()
# print ACC_OBJ.get_acc_role()
# print ACC_OBJ.get_acc_value()

# Serialize Accessible Object to JSON
# ACC_JSON = jsonpickle.encode(ACC_OBJ)
# print ACC_JSON
