import Consts
import random

mine_field = []


def is_empty(row, col):
    for r in range(4):  # מקום של חייל שלא נמצא במטריצה
        for c in range(2):
            if row == r and col == c:
                return False

    if mine_field[row][col] == Consts.EMPTY:
        return True

    return False


def create():
    global mine_field
    mine_field = [[Consts.EMPTY for i in range(Consts.FIELD_COLS)] for j in
                  range(Consts.FIELD_ROWS)]
    mine_field[0][0] = Consts.SOLDIER
    for row in range(21, 24):
        for col in range(46, 50):
            mine_field[row][col] = Consts.FLAG
    add_mines()
    print()


def random_mine():
    mine_location = []
    for i in range(Consts.MINE_NUM):
        row = random.randrange(Consts.FIELD_ROWS)
        col = random.randrange(Consts.FIELD_COLS)
        if is_empty(row, col):
            mine_location.append([row, col])
        else:
            i -= 1
    return mine_location


def add_mines():
    for mine in random_mine():
        mine_field[mine[0]][mine[1]] = Consts.MINE


def find_mines():
    mine_location = []
    for row in range(Consts.FIELD_ROWS):
        for col in range(Consts.FIELD_COLS):
            if mine_field[row][col] == Consts.MINE:
                mine_location.append([row, col])
    return mine_location


def move_soldier(movement):
    soldier_place = find_soldier()
    row = soldier_place[0]
    col = soldier_place[1]
    mine_field[row][col] = Consts.EMPTY
    if movement == Consts.DOWN:
        mine_field[row + 1][col] = Consts.SOLDIER
    if movement == Consts.UP:
        mine_field[row - 1][col] = Consts.SOLDIER
    if movement == Consts.LEFT:
        mine_field[row][col - 1] = Consts.SOLDIER
    if movement == Consts.RIGHT:
        mine_field[row][col + 1] = Consts.SOLDIER


def find_soldier():
    for row in range(Consts.FIELD_ROWS):
        for col in range(Consts.FIELD_COLS):
            if mine_field[row][col] == Consts.SOLDIER:
                return [row, col]
