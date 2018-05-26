from string import Template
import game
from helpers import print_matrix
from constants import Status

menu = {}
menu['1'] = "New game"
menu['2'] = "Continue"
menu['3'] = "Quit"


def print_options():
    options = menu.keys()
    options = sorted(options)

    for entry in options:
        template = Template("$entry - $value")
        string = template.substitute(entry=entry, value=menu[entry])
        print(string)


def run():
    game_instance = None
    game_running = False

    while True:
        print_options()
        selection = input("Please Select:")
        if selection == '1':
            game_instance = game.start()
            result = game_instance.play()
            game_running = result['status'] == Status.PAUSED
        elif selection == '2':
            if game_running:
                result = game_instance.play()
                game_running = result['status'] == Status.PAUSED
        elif selection == '3':
            break
        else:
            print("Unknown Option Selected!")
