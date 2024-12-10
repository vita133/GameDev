import pygame


class Grid:
    def __init__(self):
        self.num_rows = 20
        self.num_cols = 10
        self.cell_size = 30
        self.grid = [[0 for j in range(self.num_cols)] for i in range(self.num_rows)]
        self.colors = self.get_cell_colors()

    def print_grid(self):
        for row in range(self.num_rows):
            for column in range(self.num_cols):
                print(self.grid[row][column], end = " ")
            print()

    def get_cell_colors(self):

        dark_grey = (26, 31, 40)
        bright_yellow = (255, 223, 0)
        turquoise = (0, 204, 204)
        bright_red = (255, 51, 51)
        lime_green = (102, 255, 102)
        orange = (255, 153, 51)
        light_blue = (102, 204, 255)
        pink = (255, 102, 178)

        return [dark_grey, bright_yellow, turquoise, bright_red, lime_green, orange, light_blue,pink]
    
    def draw(self, screen):
        for row in range(self.num_rows):
            for column in range(self.num_cols):
                cell_value = self.grid[row][column]
                cell_rect = pygame.Rect(column*self.cell_size +1, row*self.cell_size +1,
                self.cell_size -1, self.cell_size -1)
                pygame.draw.rect(screen, self.colors[cell_value], cell_rect)