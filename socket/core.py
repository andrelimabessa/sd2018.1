from copy import deepcopy
from constants import Status
from helpers import print_matrix
import board


def report_end(status, history, game_board):
    return {'status': status, 'user_board_history': history, 'game_board': game_board}


def report_status(status, history, game_board):
    return {'status': status, 'user_board_history': history}


def mount_result(status, board):
    return {'status': status, 'board': board}


def apply_coords(x, y, game_board, user_board):
    user_board[x][y] = True
    return mount_result(game_board[x][y] == False, user_board)


def create_game():
    game_board = board.prepare_board(board.create_board(5, 5))

    history = [board.create_board(5, 5)]

    status_history = [report_status(Status.PLAYING, history, game_board)]

    class Game:
        def get_status(self):
            return deepcopy(status_history[-1])

        def get_state(self):
            return deepcopy(history[-1])

        def get_history(self):
            return deepcopy(history)

        def get_game_board(self):
            return deepcopy(game_board)

        def set_status(self, status, reporter):
            status_history.append(reporter(status, history, game_board))

        def set_user_board(self, board):
            history.append(deepcopy(board))

    return Game()


def start_game():
    game = create_game()
    print('Current game board:')
    print_matrix(game.get_game_board())

    class Running:
        def get_status(self):
            return game.get_status()

        def play(self, x, y):
            result = apply_coords(
                x, y, game.get_game_board(), game.get_state())

            game.set_user_board(result['board'])

            if result['status'] == False:
                game.set_status(Status.LOSE, report_end)
            else:
                game.set_status(Status.PLAYING, report_status)

        def pause(self):
            game.set_status(Status.PAUSED, report_status)

        def quit(self):
            game.set_status(Status.LOSE, report_end)

    return Running()
