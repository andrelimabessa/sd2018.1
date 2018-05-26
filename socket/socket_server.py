import socket
from datetime import datetime
from ast import literal_eval
import json
from core import start_game

ENCODE = "UTF-8"
MAX_BYTES = 65535
PORT = 5000
HOST = ''


orig = (HOST, PORT)
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind(orig)

game = None

while True:
    data, address = sock.recvfrom(MAX_BYTES)

    message = data.decode(ENCODE)
    action = json.loads(message)

    type = action['type']

    if(type == 'new_game'):
        game = start_game()
        response = json.dumps(game.get_status())
    else:
        execute = getattr(game, type)

        response = None

        state = game.get_status()

        if ('game_board' in state):
            response = json.dumps(state)
            game = start_game()
        elif 'payload' in action:
            response = json.dumps(execute(**action['payload']))
        else:
            response = json.dumps(execute())

    sock.sendto(response.encode(ENCODE), address)
