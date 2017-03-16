"""Serve HTML Test Files"""

import os
import SimpleHTTPServer
import SocketServer
from threading import Thread

DEBUG = False

class FileServer(object):
    def __init__(self):
        self.port = 8000
        directory = 'www'

        if DEBUG:
            directory = "tests/www"

        path = os.path.join(os.getcwd(), directory)
        os.chdir(path)

        handler = SimpleHTTPServer.SimpleHTTPRequestHandler
        httpd = SocketServer.TCPServer(("", self.port), handler)

        thread = Thread(target=httpd.serve_forever)
        thread.daemon = True
        thread.start()
