""" Service requests for accessible objects """

from BaseHTTPServer import BaseHTTPRequestHandler
import re
from urlparse import urlsplit, parse_qsl
from json import dumps
from SocketServer import TCPServer
from comtypes import CoInitialize
from accessible_lib.scripts.accessible import accessible
from accessible_lib.scripts.event import event
from accessible_lib.scripts.commands import execute_command

class AccessibleRequestHandler(BaseHTTPRequestHandler):
    def _successful_response(self, json):
        self.send_response(200)
        self.send_header('Content-Type', 'application/json')
        self.end_headers()
        self.wfile.write(json)

    def _bad_response(self, message):
        self.send_response(400, message)
        self.send_header('Content-Type', 'application/json')
        self.end_headers()

    def _set_identifiers(self, params):
        name = params.get('name')
        role = params.get('role')

        identifiers = {}
        if name is not None:
            identifiers["Name"] = name
        if role is not None:
            identifiers["Role"] = role

        return identifiers

    def do_GET(self):
        if re.search('/accessible', self.path) != None:
            params = dict(parse_qsl(urlsplit(self.path).query))

            _interface = params.get('interface')
            _identifiers = self._set_identifiers(params)
            _depth = params.get('depth')
            _acc_obj = accessible(_interface, _identifiers)

            if _acc_obj.found:
                _json = _acc_obj.serialize(_depth)
                self._successful_response(dumps({_interface : _json}))
            else:
                self._bad_response('Bad Request: Accessible does not exist')

        elif re.search('/event', self.path) != None:
            params = dict(parse_qsl(urlsplit(self.path).query))
            _interface = params.get('interface')
            _identifiers = self._set_identifiers(params)
            _event = params.get('type')

            if _event is None:
                self._bad_response('Bad Request: No event type specified')
                return

            _event_handler = event(_interface, _event, _identifiers)
            event_result = _event_handler.event_found

            if event_result is not None:
                self._successful_response(dumps(event_result))
            else:
                self._bad_response('Bad Request: No event occurred')

        elif re.search('/cmd', self.path) != None:
            params = {}
            params['param'] = []
            for pair in parse_qsl(urlsplit(self.path).query):
                key = pair[0]
                value = pair[1]

                if key in params:
                    params['param'].append(value)
                else:
                    params[key] = value

            _interface = params.get('interface')
            _identifiers = self._set_identifiers(params)
            _function = params.get('function')
            _function_params = params.get('param')

            if _function is None:
                self._bad_response('Bad Request: No command specified')
                return

            _value = execute_command(_interface, _identifiers, _function, _function_params)

            if _value is not "ERROR":
                self._successful_response(dumps(_value))
            else:
                self._bad_response('Bad Request: Command can not be executed on accessible')
        else:
            self.send_response(403, 'Invalid Request')
            self.send_header('Content-Type', 'application/json')
            self.end_headers()
        return

class AccessibleService:
    def __init__(self, ip, port):
        CoInitialize()
        handler = AccessibleRequestHandler
        self.server = TCPServer((ip, port), handler)
        print '.............SERVICE RUNNING...............'
        self.server.serve_forever()

if __name__ == '__main__':
    print '.............SETTING UP SERVICE............'
    SERVER = AccessibleService("", 5000)

    try:
        while True:
            pass
    except KeyboardInterrupt:
        print '.............SERVICE STOPPED...........'
