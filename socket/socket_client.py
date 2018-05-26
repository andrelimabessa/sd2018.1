from ast import literal_eval
from socket import socket, AF_INET, SOCK_DGRAM
from datetime import datetime
import json

ENCODE = "UTF-8"
HOST = '127.0.0.1'
PORT = 5000
MAX_BYTES = 65535


def request(obj):

    dest = (HOST, PORT)
    sock = socket(AF_INET, SOCK_DGRAM)

    message = json.dumps(obj)
    data = message.encode(ENCODE)
    sock.sendto(data, dest)

    data, address = sock.recvfrom(MAX_BYTES)
    response = data.decode(ENCODE)
    sock.close()

    return json.loads(response)
