import Consts
import MineField
import main

def is_lose():
    soldier_sqr = MineField.find_soldier()
    #
    main.state["state"]  = Consts.LOSE_STATE
    pass
def is_win():
    soldier_sqr = MineField.find_soldier()
    #
    main.state["state"] = Consts.WIN_STATE
    pass