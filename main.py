import pygame
import MineField
import Screen
import Consts
import Soldier
import time
import datetime

state = {
    "screen_open": True,
    "is_enter": False,
    "is_moving": False,
    "state": Consts.RUNNING_STATE,
    "is_message": True
}


def main():
    pygame.init()
    MineField.create()

    while state["screen_open"]:

        handle_user_events()

        if state["is_moving"] and not state["is_enter"]:
            pass

        if state["is_enter"]:
            pass

        if is_lose():
            state["state"] = Consts.LOSE_STATE
        elif is_win():
            state["state"] = Consts.WIN_STATE

        Screen.draw_game(state)


def handle_user_events():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            state['screen_open'] = False

        elif state["state"] != Consts.RUNNING_STATE:
            continue

        if not state['is_enter']:

            if event.type == pygame.KEYDOWN:
                state['is_message'] = False
                if event.key == pygame.K_RETURN:
                    state['is_enter'] = True
                if event.key == pygame.K_UP:
                    Soldier.move_soldier(Consts.UP)
                if event.key == pygame.K_DOWN:
                    Soldier.move_soldier(Consts.DOWN)
                if event.key == pygame.K_LEFT:
                    Soldier.move_soldier(Consts.LEFT)
                if event.key == pygame.K_RIGHT:
                    Soldier.move_soldier(Consts.RIGHT)
                for i in range(1, 10):
                    if pygame.key.name(event.key) == str(i):
                        global start
                        start = datetime.datetime.now()

            if event.type == pygame.KEYUP:
                for i in range(1, 10):
                    if pygame.key.name(event.key) == str(i):
                        end = datetime.datetime.now()
                        t = end - start
                        if t.seconds < 1:
                            print("save")
                        else:
                            print('upload')

            Screen.draw_game(state)


def is_lose():  # אם רגלי החייל נוגעות במקש
    soldier_sqr = Soldier.find_soldier()
    row = soldier_sqr[0]
    col = soldier_sqr[1]
    for c in range(1):
        if MineField.mine_field[row + 3][col + c] == Consts.MINE:
            state["state"] = Consts.LOSE_STATE


def is_win():  # אם החייל נוגע בדגל
    soldier_sqr = Soldier.find_soldier()
    row = soldier_sqr[0]
    col = soldier_sqr[1]
    for r in range(4):
        for c in range(2):
            if MineField.mine_field[row + r][col + c] == Consts.FLAG:
                state["state"] = Consts.WIN_STATE


if __name__ == '__main__':
    main()
