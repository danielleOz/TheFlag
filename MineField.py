import Consts

mine_field = []


def create():
    global mine_field
    mine_field = [[Consts.EMPTY for i in range(Consts.FIELD_ROWS)] for j in range(Consts.FIELD_COLS)]
    pass


def move_soldier():
    pass


def is_flag():
    pass


def random_mine():
    pass


def find_soldier():
    for row in range(Consts.FIELD_ROWS):
        for col in range(Consts.FIELD_COLS):
            if mine_field[row][col] == Consts.SOLDIER:
                return [row, col]

