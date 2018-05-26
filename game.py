from string import Template
from helpers import print_matrix
from core import start_game
from constants import Status

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


def game_on(game, state, options):
    print_status(state, options)
    selection = input("Please Select:")
    if selection == '1':
        game.play(**play(state['user_board_history'][-1]))
    elif selection == '2':
        game.pause()
    elif selection == '3':
        game.quit()
    else:
        print("Unknown Option Selected!")


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


def start():
    game = start_game()

    class Game:
        def play(self):
            options = menu.keys()
            options = sorted(options)

            state = game.get_status()
            status = state['status']
            game_on(game, state, options)

            while True:
                state = game.get_status()
                status = state['status']
                print(status)
                if status == Status.PLAYING:
                    game_on(game, state, options)
                else:
                    return game_off(state)

    return Game()
