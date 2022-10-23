import pygame
import Consts
import MineField
import Soldier

screen = pygame.display.set_mode(
    (Consts.WINDOW_WIDTH, Consts.WINDOW_HEIGHT))


def draw_field():
    draw_grass()
    soldier = create_solider()
    soldier_loc = Soldier.find_soldier()
    screen.blit(soldier, (
        soldier_loc[1] * Consts.SQUARE_SIZE,
        soldier_loc[0] * Consts.SQUARE_SIZE))
    flag = create_flag()
    screen.blit(flag, (Consts.WINDOW_WIDTH - Consts.FLAG_WIDTH,
                       Consts.WINDOW_HEIGHT - Consts.FLAG_HEIGHT))
    pygame.display.update()
    draw_start_message()
    pygame.display.flip()


def draw_night_field(game_state):
    screen.fill(Consts.BLACK)
    draw_grid()
    soldier = create_night_solider()
    soldier_loc = MineField.find_soldier()
    screen.blit(soldier, (
        soldier_loc[1] * Consts.SQUARE_SIZE,
        soldier_loc[0] * Consts.SQUARE_SIZE))
    mine_loc = MineField.find_mines()
    mine = create_mine()
    for i in mine_loc:
        screen.blit(mine,
                    (i[1] * Consts.SQUARE_SIZE, i[0] * Consts.SQUARE_SIZE))

    pygame.display.flip()
    pygame.time.wait(1000)
    game_state["is_enter"] = False


def draw_grass():
    grass = create_grass()
    loc = Consts.GRASS_LOCATIONS
    for i in loc:
        screen.blit(grass,
                    ((i[0]) * Consts.SQUARE_SIZE, (i[1]) * Consts.SQUARE_SIZE))


def draw_grid():
    for i in range(Consts.FIELD_COLS + 1):
        pygame.draw.line(screen, Consts.GRID_LINE_COLOR,
                         (Consts.SQUARE_SIZE * i, 0),
                         (Consts.SQUARE_SIZE * i, Consts.WINDOW_HEIGHT), 1)
    for i in range(Consts.FIELD_ROWS + 1):
        pygame.draw.line(screen, Consts.GRID_LINE_COLOR,
                         (0, Consts.SQUARE_SIZE * i),
                         (Consts.WINDOW_WIDTH, Consts.SQUARE_SIZE * i),
                         1)


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


def create_grass():
    grass = pygame.image.load(Consts.GRASS_IMG)
    sized_grass = pygame.transform.scale(grass, (
        Consts.GRASS_WIDTH, Consts.GRASS_HEIGHT))
    return sized_grass


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
    # draw_field()
    # draw_night_field()

    if not game_state["is_enter"]:
        draw_field()
    if game_state["is_enter"]:
        draw_night_field(game_state)

    if game_state["state"] == Consts.LOSE_STATE:
        draw_lose_message()

    if game_state["state"] == Consts.WIN_STATE:
        draw_win_message()

    pygame.display.flip()
