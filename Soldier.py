import Consts
import MineField
import main

soldier_field = [[Consts.EMPTY for i in range(Consts.FIELD_COLS)] for j in
                 range(Consts.FIELD_ROWS)]
mine_field[0][0] = Consts.SOLDIER


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


def is_lose():  # אם רגלי החייל נוגעות במקש
    soldier_sqr = MineField.find_soldier()
    row = soldier_sqr[0]
    col = soldier_sqr[1]
    for c in range(1):
        if MineField.mine_field[row + 3][col + c] == Consts.MINE:
            main.state["state"] = Consts.LOSE_STATE


def is_win():  # אם החייל נוגע בדגל
    soldier_sqr = MineField.find_soldier()
    row = soldier_sqr[0]
    col = soldier_sqr[1]
    for r in range(4):
        for c in range(2):
            if MineField.mine_field[row + r][col + c] == Consts.FLAG:
                main.state["state"] = Consts.WIN_STATE
