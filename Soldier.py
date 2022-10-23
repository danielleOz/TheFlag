import Consts
import MineField
import main


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
