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
    pygame.init()
    MineField.create()
    MineField.count_mines()

    while state["screen_open"]:

        handle_user_events()

        if state["is_moving"] and not state["is_enter"]:
            pass

        if state["is_enter"]:
            pass

        Screen.draw_game(state)


def handle_user_events():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            state['scree_open'] = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                MineField.move_soldier(Consts.UP)
            if event.key == pygame.K_DOWN:
                MineField.move_soldier(Consts.DOWN)
            if event.key == pygame.K_LEFT:
                MineField.move_soldier(Consts.LEFT)
            if event.key == pygame.K_RIGHT:
                MineField.move_soldier(Consts.RIGHT)
            if event.key == pygame.K_KP_ENTER:
                state['is_enter'] = True

        Screen.draw_game(state)



if __name__ == '__main__':
    main()
