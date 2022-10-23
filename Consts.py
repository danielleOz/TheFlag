import random
import MineField

FIELD_ROWS = 25
FIELD_COLS = 50
GREEN = (85, 107, 47)
BACKGROUND_COLOR = GREEN
SQUARE_SIZE = 25
WINDOW_HEIGHT = FIELD_ROWS * SQUARE_SIZE
WINDOW_WIDTH = FIELD_COLS * SQUARE_SIZE
MINE_NUM = 20
GRASS_NUM = 20
EMPTY = "EMPTY"
SOLDIER = "SOLDIER"
MINE = "MINE"
FLAG = "FLAG"

LOSE_MESSAGE = "You Lost!"
LOSE_FONT_SIZE = int(0.15 * WINDOW_WIDTH)
BLACK = (0, 0, 0)
LOSE_COLOR = BLACK
LOSE_LOCATION = \
    (0.2 * WINDOW_WIDTH, WINDOW_HEIGHT / 2 - (LOSE_FONT_SIZE / 2))

WIN_MESSAGE = "You Won!"
WIN_FONT_SIZE = LOSE_FONT_SIZE
WIN_COLOR = (89, 89, 89)
WIN_LOCATION = \
    (0.2 * WINDOW_WIDTH, WINDOW_HEIGHT / 2 - (WIN_FONT_SIZE / 2))
FONT_NAME = "Calibri"
TEXT_COLOR = BLACK
TEXT_TEXT = f"Welcome to The Flag game. \n Have Fun!"
TEXT_FONT_SIZE = 20
TEXT_LOCATION = (10, WINDOW_HEIGHT - TEXT_FONT_SIZE - 10)

SOLDIER_IMG = "soldier.png"
SOLDIER_HEIGHT = 4 * SQUARE_SIZE
SOLDIER_WIDTH = 2 * SQUARE_SIZE
SOLDIER_X = WINDOW_WIDTH / 2 - (SOLDIER_WIDTH / 2)
SOLDIER_Y = WINDOW_HEIGHT * 0.8

SOLDIER_NIGHT_IMG = "soldier_nigth.png"

GRASS_IMG = "grass.png"
GRASS_HEIGHT = 2.5 * SQUARE_SIZE
GRASS_WIDTH = 2.5 * SQUARE_SIZE
GRASS_X = WINDOW_WIDTH / 2 - (GRASS_WIDTH / 2)
GRASS_Y = WINDOW_HEIGHT * 0.8

FLAG_IMG = "flag.png"
FLAG_HEIGHT = 3 * SQUARE_SIZE
FLAG_WIDTH = 4 * SQUARE_SIZE
FLAG_X = WINDOW_WIDTH / 2 - (FLAG_WIDTH / 2)
FLAG_Y = WINDOW_HEIGHT * 0.8

MINE_IMG = "mine.png"
MINE_HEIGHT = 3 * SQUARE_SIZE
MINE_WIDTH = SQUARE_SIZE
MINE_X = WINDOW_WIDTH / 2 - (MINE_WIDTH / 2)
MINE_Y = WINDOW_HEIGHT * 0.8

RUNNING_STATE = 1
LOSE_STATE = 2
WIN_STATE = 3

DOWN = 'DOWN'
UP = 'UP'
LEFT = 'LEFT'
RIGHT = 'RIGHT'


def random_mine():
    mine_location = []
    for i in range(MINE_NUM):
        row = random.randrange(FIELD_ROWS)
        col = random.randrange(FIELD_COLS)
        if MineField.is_empty(row, col):
            mine_location.append([row, col])
        else:
            i -= 1
    return mine_location


MINE_LOCATION = random_mine()


def grass_loc():
    grass_locations = []
    for i in range(GRASS_NUM):
        x = random.randint(0, FIELD_COLS)
        y = random.randint(0, FIELD_ROWS)
        loc = (x, y)
        grass_locations.append(loc)
    return grass_locations


GRASS_LOCATIONS = grass_loc()
