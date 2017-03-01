import json, urllib
from pprint import pprint
from marionette_driver import By
from marionette_driver.marionette import Marionette

localhost = "http://localhost:"
serverPort = str(5000)
filePort = str(8000)

client = Marionette(host='localhost', port=2828)
client.start_session()

test_html = localhost + filePort + "/"+ 'test_msaa_role.html'
client.navigate(test_html)

event_params = urllib.urlencode({'id': 'MSAA Checkbox', 'type' : 'EVENT_OBJECT_STATECHANGE'})
event_endpoint = localhost + serverPort + "/event?%s"
event_register_params = urllib.urlencode({'type' : 'EVENT_OBJECT_STATECHANGE'})
event_register_endpoint = localhost + serverPort + "/event_register?%s"
accessible_params = urllib.urlencode({'id': 'MSAA Checkbox', 'depth': -1})
accessible_endpoint = localhost + serverPort + "/accessible?%s"

response = json.load(urllib.urlopen(accessible_endpoint % accessible_params))
assert response['role'] == 'check box'
pprint(response)

response = json.load(urllib.urlopen(event_register_endpoint % event_register_params))
print response

checkbox = client.find_element(By.CSS_SELECTOR, "input[type='checkbox']")
checkbox.click()

response = json.load(urllib.urlopen(event_endpoint % event_params))
print response



