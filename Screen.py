import pygame
import Consts
screen = pygame.display.set_mode(
    (Consts.WINDOW_WIDTH, Consts.WINDOW_HEIGHT))

def draw_field():
    pass

def draw_night_field():
    pass

def draw_message(message, font_size, color, location):
    font = pygame.font.SysFont(Consts.FONT_NAME, font_size)
    text_img = font.render(message, True, color)
    screen.blit(text_img, location)
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

