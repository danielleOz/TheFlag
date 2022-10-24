import Consts
import MineField
import main

soldier_field = [[Consts.EMPTY for i in range(Consts.FIELD_COLS)] for j in
                 range(Consts.FIELD_ROWS)]
soldier_field[0][0] = Consts.SOLDIER


def find_soldier():
    for row in range(Consts.FIELD_ROWS):
        for col in range(Consts.FIELD_COLS):
            if soldier_field[row][col] == Consts.SOLDIER:
                return [row, col]


def move_soldier(movement):
    soldier_place = find_soldier()
    row = soldier_place[0]
    col = soldier_place[1]
    if movement == Consts.DOWN and row + 4 < Consts.FIELD_ROWS:
        soldier_field[row + 1][col] = Consts.SOLDIER
        soldier_field[row][col] = Consts.EMPTY
    if movement == Consts.UP and row - 1 > -1:
        soldier_field[row - 1][col] = Consts.SOLDIER
        soldier_field[row][col] = Consts.EMPTY
    if movement == Consts.LEFT and col - 1 > -1:
        soldier_field[row][col - 1] = Consts.SOLDIER
        soldier_field[row][col] = Consts.EMPTY
    if movement == Consts.RIGHT and col + 2 < Consts.FIELD_COLS:
        soldier_field[row][col + 1] = Consts.SOLDIER
        soldier_field[row][col] = Consts.EMPTY


def change_soldier_field(new_field):
    for row in range(Consts.FIELD_ROWS):
        for col in range(Consts.FIELD_COLS):
            soldier_field[row][col] = new_field[row][col]
