""" Service requests for accessible objects """

from BaseHTTPServer import BaseHTTPRequestHandler
import re
from urlparse import urlsplit, parse_qsl
from SocketServer import TCPServer
from threading import Thread
from comtypes import CoInitialize
from accessible_lib.scripts.accessible import accessible

class AccessibleRequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        if re.search('/accessible', self.path) != None:
            params = dict(parse_qsl(urlsplit(self.path).query))
            _name = params.get('name')
            _role = params.get('role')
            _interface = params.get('interface')
            _depth = params.get('depth')

            _identifiers = {}
            if _name is not None:
                _identifiers["Name"] = _name
            if _role is not None:
                _identifiers["Role"] = _role

            _acc_obj = accessible(_interface, _identifiers)

            if _acc_obj.found:
                _json = _acc_obj.serialize(_depth)

                self.send_response(200)
                self.send_header('Content-Type', 'application/json')
                self.end_headers()
                self.wfile.write({_interface : _json})
            else:
                self.send_response(400, 'Bad Request: record does not exist')
                self.send_header('Content-Type', 'application/json')
                self.end_headers()
        else:
            self.send_response(403)
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
    SERVER = AccessibleService("", 8000)

    try:
        while True:
            pass
    except KeyboardInterrupt:
        print '.............SERVICE STOPPED...........'
