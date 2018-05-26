from ast import literal_eval
import xmlrpc.client

from datetime import datetime
import json

ENCODE = "UTF-8"

proxy = xmlrpc.client.ServerProxy('http://localhost:5000', allow_none=True)


def request(action):

    type = action['type']

    if(type == 'new_game'):
        proxy.new_game()
        response = proxy.get_status()
    else:
        execute = getattr(proxy, type)

        response = None

        state = proxy.get_status()

        if ('game_board' in state):
            response = state
            proxy.new_game()
        elif 'payload' in action:
            response = execute(action['payload']['x'], action['payload']['y'])
        else:
            response = execute()

    return response
