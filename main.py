import pygame
import MineField
import Screen

import Consts

state = {
    "screen_open": True,
    "is_enter": False,
    "is_moving": False,
    "state": Consts.RUNNING_STATE
}


def main():

    MineField.create()

    while state["screen_open"]:

        handle_user_events()

        if state["is_moving"] and not state["is_enter"]:
            pass

        if state["is_enter"]:
            pass

        Screen.draw_game(state)



def handle_user_events():
    pass


if __name__ == '__main__':
    main()
