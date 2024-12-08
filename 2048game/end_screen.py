import pygame
import sys
from constants import WIDTH, HIGHT, BACKGROUND_COLOR, FONT_COLOR

pygame.init()
WINDOW = pygame.display.set_mode((WIDTH, HIGHT))
FONT = pygame.font.SysFont("comicsans", 30, bold=True)

def draw_button(text, x, y, width, height, color, font_color):
    button_rect = pygame.Rect(x, y, width, height)
    #pygame.draw.rect(WINDOW, color, button_rect)
    text_surface = FONT.render(text, True, font_color)
    text_rect = text_surface.get_rect(center=button_rect.center)
    WINDOW.blit(text_surface, text_rect)
    return button_rect

def show_end_screen(points):
    WINDOW.fill(BACKGROUND_COLOR)
    FONT_COLOR_BTN = (255, 255, 255)
    
    text = FONT.render("Game over", True, FONT_COLOR)
    points_text = FONT.render(f"Score: {points}", True, FONT_COLOR)

    WINDOW.blit(
        text, 
        (
            WIDTH // 2 - text.get_width() // 2, 
            HIGHT // 4 - text.get_height() // 2
        )
    )

    WINDOW.blit(
        points_text, 
        (
            WIDTH // 2 - points_text.get_width() // 2, 
            HIGHT // 4 * 2 - points_text.get_height() // 2
        )
    )

    back_button = draw_button("Menu", WIDTH // 4 - 100, HIGHT // 2 + 50, 200, 50, (255, 0, 0), FONT_COLOR_BTN)
    
    replay_button = draw_button("Play", WIDTH // 4 * 3 - 100, HIGHT // 2 + 50, 200, 50, (0, 255, 0), FONT_COLOR_BTN)

    pygame.display.update()

    waiting = True
    while waiting:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_x, mouse_y = pygame.mouse.get_pos()

                if back_button.collidepoint(mouse_x, mouse_y):
                    
                    print("Повернутись назад")
                    waiting = False 

                if replay_button.collidepoint(mouse_x, mouse_y):
                    from utils import Game
                    game = Game()
                    game.run()
                    print("Грати ще")
                    waiting = False

    pygame.quit()
    sys.exit()

