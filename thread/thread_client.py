from ast import literal_eval
import xmlrpc.client
from datetime import datetime
import initial_menu
from threading import Thread

def client_thread(queue):
    return Thread(target=initial_menu.run, args=(queue,))