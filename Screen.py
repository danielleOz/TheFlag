import pygame
import Consts

screen = pygame.display.set_mode(
    (Consts.WINDOW_WIDTH, Consts.WINDOW_HEIGHT))


def draw_field():

    draw_start_message()
    pass


def draw_night_field():
    pass

def create_solider():
    solider = pygame.image.load(Consts.SOLDIER_IMG)
    sized_solider = pygame.transform.scale(solider, (
        Consts.SOLDIER_WIDTH, Consts.SOLDIER_HEIGHT))
    return sized_solider

def create_night_solider():
    night_solider = pygame.image.load(Consts.SOLDIER_NIGHT_IMG)
    sized_night_solider = pygame.transform.scale(night_solider, (
        Consts.SOLDIER_WIDTH, Consts.SOLDIER_HEIGHT))
    return sized_night_solider
def create_flag():
    flag = pygame.image.load(Consts.FLAG_IMG)
    sized_flag = pygame.transform.scale(flag, (
        Consts.FLAG_WIDTH, Consts.FLAG_HEIGHT))
    return sized_flag
def create_mine():
    mine = pygame.image.load(Consts.MINE_IMG)
    sized_mine = pygame.transform.scale(mine, (
        Consts.MINE_WIDTH, Consts.MINE_HEIGHT))
    return sized_mine

def draw_message(message, font_size, color, location):
    font = pygame.font.SysFont(Consts.FONT_NAME, font_size)
    text_img = font.render(message, True, color)
    screen.blit(text_img, location)


def draw_start_message():
    draw_message(Consts.TEXT_TEXT, Consts.TEXT_FONT_SIZE,
                 Consts.TEXT_COLOR, Consts.TEXT_LOCATION)


def draw_lose_message():
    draw_message(Consts.LOSE_MESSAGE, Consts.LOSE_FONT_SIZE,
                 Consts.LOSE_COLOR, Consts.LOSE_LOCATION)


def draw_win_message():
    draw_message(Consts.WIN_MESSAGE, Consts.WIN_FONT_SIZE,
                 Consts.WIN_COLOR, Consts.WIN_LOCATION)


def draw_game(game_state):
    screen.fill(Consts.BACKGROUND_COLOR)
    draw_field()

    if game_state["is_enter"]:
        draw_night_field()

    if game_state["is_moving"]:
        pass

    elif game_state["state"] == Consts.LOSE_STATE:
        draw_lose_message()

    elif game_state["state"] == Consts.WIN_STATE:
        draw_win_message()

    pygame.display.flip()
