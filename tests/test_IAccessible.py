"""Test out accessible service features"""

import json
import urllib
from pprint import pprint
from marionette_driver import By
from marionette_driver.marionette import Marionette
from www.fileserver import FileServer

# Start services
FILE_SERVER = FileServer()

SERVICE_PORT = str(5000)
FILE_PORT = str(FILE_SERVER.port)
HOST = "http://localhost:"
ENDPOINT_PREFIX = HOST + SERVICE_PORT
TEST_HTML = HOST + FILE_PORT + "/"+ 'test_IAccessible.html'

CLIENT = Marionette(host='localhost', port=2828)
CLIENT.start_session()
CLIENT.navigate(TEST_HTML)

EVENT_PARAMS = urllib.urlencode({'type': 'IAccessible', 'id': 'MSAA Checkbox', 'event' : 'EVENT_OBJECT_STATECHANGE'})
EVENT_ENDPOINT = ENDPOINT_PREFIX + "/event?%s"
CMD_PARAMS = urllib.urlencode({'type': 'IAccessible', 'id': 'MSAA Checkbox', 'function': 'accState'})
CMD_ENPOINT = ENDPOINT_PREFIX + "/cmd?%s"
ACCESSSIBLE_PARAMS = urllib.urlencode({'type': 'IAccessible', 'id': 'MSAA Checkbox', 'depth': -1})
ACCESSIBLE_ENDPOINT = ENDPOINT_PREFIX + "/accessible?%s"

RESPONSE = json.load(urllib.urlopen(ACCESSIBLE_ENDPOINT % ACCESSSIBLE_PARAMS))
assert RESPONSE['IAccessible']['Role'] == 'check box'
print "-----------------ACCESSIBLE------------------"
pprint(RESPONSE)

CHECKBOX = CLIENT.find_element(By.CSS_SELECTOR, "input[type='checkbox']")
CHECKBOX.click()

RESPONSE = json.load(urllib.urlopen(EVENT_ENDPOINT % EVENT_PARAMS))
print "-----------------EVENT-----------------------"
pprint(RESPONSE)

RESPONSE = json.load(urllib.urlopen(CMD_ENPOINT % CMD_PARAMS))
print "-----------------CMD-----------------------"
pprint(RESPONSE)
