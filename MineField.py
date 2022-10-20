import Consts
import random


def is_flag_or_soldier():
    return False


def random_mine():
    for i in range(Consts.MINE_NUM):
        row = random.randint(0, Consts.FIELD_ROWS)
        col = random.randint(0, Consts.FIELD_COLS)
        if not is_flag_or_soldier():
            mine_location.append([row, col])
        else:
            i -= 1


mine_field = []
mine_location = []
random_mine()
print(mine_location)


def create():
    global mine_field
    mine_field = [[Consts.EMPTY for i in range(Consts.FIELD_ROWS)] for j in range(Consts.FIELD_COLS)]
    pass


def move_soldier():
    pass


def find_soldier():
    for row in range(Consts.FIELD_ROWS):
        for col in range(Consts.FIELD_COLS):
            if mine_field[row][col] == Consts.SOLDIER:
                return [row, col]
