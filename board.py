import random


def create_board(x_size, y_size):
    def x_columns(): return [False] * x_size
    return [x_columns() for i in range(y_size)]


def sort_position(item):
    return bool(random.randint(0, 1))


def sort_column(column):
    return [*map(sort_position, column)]


def prepare_board(board):
    return [*map(sort_column, board)]
