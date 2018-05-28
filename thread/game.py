from string import Template
from helpers import print_matrix
from core import start_game
from constants import Status
from client_request import request
import time

menu = {}
menu['1'] = "Play"
menu['2'] = "Pause"
menu['3'] = "Quit"


def get_coordinate(coord):
    template = Template("Please select $coordinate: ")
    string = template.substitute(coordinate=coord)
    value = input(string)
    return value if value.isdigit() else get_coordinate(coord)


def play(user_board):
    x = int(get_coordinate("x"))
    y = int(get_coordinate("y"))

    if user_board[x][y]:
        print("Already tried this position")
        return play(user_board)

    return {'x': x, 'y': y}


def print_status(state, options):
    if 'game_board' in state:
        print('Game board:')
        print_matrix(state['game_board'])
    print('Your board:')
    print_matrix(state['user_board_history'][-1])

    for entry in options:
        template = Template("$entry - $value")
        string = template.substitute(entry=entry, value=menu[entry])
        print(string)


def game_on(queue, state, options):
    print_status(state, options)
    selection = input("Please Select:")
    if selection == '1':
        request(queue, {'type': 'play', 'payload': play(
            state['user_board_history'][-1])})
    elif selection == '2':
        request(queue, {'type': 'pause'})
    elif selection == '3':
        request(queue, {'type': 'quit'})
    else:
        print("Unknown Option Selected!")
        game_on(queue, state, options)


def game_off(state):
    print('Game history:')
    for idx, item in enumerate(state['user_board_history']):
        print(idx)
        print(print_matrix(item))

    status = state['status']
    if(status != Status.PAUSED):
        print('Game board:')
        print_matrix(state['game_board'])

    return state


def start(queue):
    request(queue, {'type': 'new_game'})
    queue.get_from_client_queue()
    queue.client_task_done()

    class Game:
        def play(self):
            options = menu.keys()
            options = sorted(options)
            request(queue, {'type': 'get_status'})
            state = queue.get_from_client_queue()
            queue.client_task_done()
            game_on(queue, state, options)

            while True:
                state = queue.get_from_client_queue()
                queue.client_task_done()
                status = state['status']

                if status == Status.PLAYING:
                    game_on(queue, state, options)
                else:
                    return game_off(state)

    return Game()
