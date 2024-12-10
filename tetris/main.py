import pygame,sys

pygame.init()
game_color = (80, 4, 110)

screen = pygame.display.set_mode((300, 600))
pygame.display.set_caption("Tetris")

clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    screen.fill(game_color)
    pygame.display.update()
    clock.tick(60)

