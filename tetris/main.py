import pygame,sys
from grid import Grid
from blocks import *

pygame.init()
game_color = (80, 4, 110)

screen = pygame.display.set_mode((300, 600))
pygame.display.set_caption("Tetris")

clock = pygame.time.Clock()

game_grid = Grid()

block = IBlock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    #Drawing
    screen.fill(game_color)
    game_grid.draw(screen)
    block.draw(screen)

    pygame.display.update()
    clock.tick(60)

