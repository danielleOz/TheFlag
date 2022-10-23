import Consts
import random

mine_field = []


def is_empty(row, col):
    for r in range(4):  # מקום של חייל שלא נמצא במטריצה
        for c in range(2):
            if row == r and col == c:
                return False
    if col + 2 >= Consts.FIELD_COLS:
        return False
    for i in range(3):
        if mine_field[row][col + i] != Consts.EMPTY:
            return False
    return True


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


def add_mines():
    i = 0
    limit = Consts.MINE_NUM
    while i < limit:
        row = random.randrange(Consts.FIELD_ROWS)
        col = random.randrange(Consts.FIELD_COLS)

        if is_empty(row, col):
            insert_mine(row, col)
            i += 1


def insert_mine(row, col):
    for i in range(3):
        mine_field[row][col + i] = Consts.MINE


def count_mines():
    count = 0
    for row in mine_field:
        for item in row:
            if item == Consts.MINE:
                count += 1
    return count


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
    if movement == Consts.DOWN and row + 1 < Consts.FIELD_ROWS:
        mine_field[row + 1][col] = Consts.SOLDIER
        mine_field[row][col] = Consts.EMPTY
    if movement == Consts.UP and row - 1 > -1:
        mine_field[row - 1][col] = Consts.SOLDIER
        mine_field[row][col] = Consts.EMPTY
    if movement == Consts.LEFT and col - 1 > -1:
        mine_field[row][col - 1] = Consts.SOLDIER
        mine_field[row][col] = Consts.EMPTY
    if movement == Consts.RIGHT and col + 1 < Consts.FIELD_COLS:
        mine_field[row][col + 1] = Consts.SOLDIER
        mine_field[row][col] = Consts.EMPTY


def find_soldier():
    for row in range(Consts.FIELD_ROWS):
        for col in range(Consts.FIELD_COLS):
            if mine_field[row][col] == Consts.SOLDIER:
                return [row, col]
