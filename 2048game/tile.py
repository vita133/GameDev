import pygame
import math

from constants import RECT_WIDTH, RECT_HEIGHT, FONT_COLOR

class Tile:
    COLORS = [
    (255, 85, 128),
    (255, 223, 0),
    (0, 204, 204),
    (255, 51, 51),
    (102, 255, 102),
    (255, 153, 51),
    (102, 204, 255),
    (255, 102, 178),
    (255, 255, 255),
    (80, 4, 110),
    (141, 88, 163),  
]



    def __init__(self, value, row, col):
        self.value = value
        self.row = row
        self.col = col
        self.x = col * RECT_WIDTH
        self.y = row * RECT_HEIGHT

    def get_color(self):
        color_index = int(math.log2(self.value)) - 1
        return self.COLORS[color_index]

    def draw(self, window):
        FONT = pygame.font.SysFont("comicsans", 60, bold=True)
        color = self.get_color()
        pygame.draw.rect(window, color, (self.x, self.y, RECT_WIDTH, RECT_HEIGHT))

        text = FONT.render(str(self.value), 1, FONT_COLOR)
        window.blit(
            text,
            (self.x + (RECT_WIDTH / 2 - text.get_width() / 2),
             self.y + (RECT_HEIGHT / 2 - text.get_height() / 2)),
        )

    def set_pos(self, ceil=False):
        if ceil:
            self.row = math.ceil(self.y / RECT_HEIGHT)
            self.col = math.ceil(self.x / RECT_WIDTH)
        else:
            self.row = math.floor(self.y / RECT_HEIGHT)
            self.col = math.floor(self.x / RECT_WIDTH)

    def move(self, delta):
        self.x += delta[0]
        self.y += delta[1]
