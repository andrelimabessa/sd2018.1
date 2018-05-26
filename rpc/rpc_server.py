from xmlrpc.server import SimpleXMLRPCServer
from xmlrpc.server import SimpleXMLRPCRequestHandler
from datetime import datetime
from ast import literal_eval
import json
from core import start_game

ENCODE = "UTF-8"
PORT = 5000


class RequestHandler(SimpleXMLRPCRequestHandler):
    rpc_paths = ('/RPC2',)


with SimpleXMLRPCServer(("localhost", PORT),
                        requestHandler=RequestHandler, allow_none=True) as server:
    server.register_introspection_functions()

    def new_game():
        server.register_instance(start_game())

    server.register_function(new_game)

    server.serve_forever()
