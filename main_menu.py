import pygame
import sys
import subprocess 
from main_colors import Colors

pygame.init()

screen = pygame.display.set_mode((500, 620))
pygame.display.set_caption("Main Menu")
title_font = pygame.font.Font(None, 60)
button_font = pygame.font.Font(None, 40)
clock = pygame.time.Clock()

play_2048_button_rect = pygame.Rect(150, 200, 200, 80)
play_tetris_button_rect = pygame.Rect(150, 320, 200, 80)
exit_button_rect = pygame.Rect(150, 440, 200, 80)
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            if play_tetris_button_rect.collidepoint(event.pos):
                subprocess.Popen(["python", "tetris/main.py"])
                pygame.quit()
                sys.exit()
            if play_2048_button_rect.collidepoint(event.pos):
                subprocess.Popen(["python", "2048game/game.py"])
                pygame.quit()
                sys.exit()
            if exit_button_rect.collidepoint(event.pos):
                pygame.quit()
                sys.exit()
    
    screen.fill(Colors.dark_violet)
    
    title_surface = title_font.render("CHOOSE THE GAME!", True, Colors.white)
    screen.blit(title_surface, (50, 100))
    
    pygame.draw.rect(screen, Colors.light_violet, play_2048_button_rect, 0, 10)
    pygame.draw.rect(screen, Colors.light_violet, play_tetris_button_rect, 0, 10)

    pygame.draw.rect(screen, Colors.light_violet, exit_button_rect, 0, 10)
    
    play_2048_surface = button_font.render("2048", True, Colors.white)
    play_tetris_surface = button_font.render("TETRIS", True, Colors.white)
    exit_button_surface = button_font.render("EXIT", True, Colors.white)
    screen.blit(play_2048_surface, (play_2048_button_rect.x + 70, play_2048_button_rect.y + 28))
    screen.blit(play_tetris_surface, (play_tetris_button_rect.x + 50, play_tetris_button_rect.y + 28))

    screen.blit(exit_button_surface, (exit_button_rect.x + 70, exit_button_rect.y + 28))
    pygame.display.update()
    clock.tick(60)