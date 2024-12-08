import pygame
import random
from tile import Tile
from constants import FPS, WIDTH, HIGHT, ROWS, COLS, RECT_HEIGHT, RECT_WIDTH, OUTLINE_COLOR, OUTLINE_THICKNESS, BACKGROUND_COLOR, MOVE_VEL, FONT_COLOR
from end_screen import show_end_screen

class Game:
    def __init__(self):
        pygame.init()
        self.window = pygame.display.set_mode((WIDTH, HIGHT))
        pygame.display.set_caption("2048")
        self.clock = pygame.time.Clock()
        self.font = pygame.font.SysFont("comicsans", 60, bold=True)
        self.small_font = pygame.font.SysFont("comicsans", 30, bold=True)
        self.tiles = {}
        self.generate_tiles()
        self.points = 0

    def draw_grid(self):
        for row in range(1, ROWS):
            y = row * RECT_HEIGHT
            pygame.draw.line(self.window, OUTLINE_COLOR, (0, y), (WIDTH, y), OUTLINE_THICKNESS)
        
        for col in range(1, COLS):
            x = col * RECT_WIDTH
            pygame.draw.line(self.window, OUTLINE_COLOR, (x, 0), (x, HIGHT), OUTLINE_THICKNESS)

        pygame.draw.rect(self.window, OUTLINE_COLOR, (0, 0, WIDTH, HIGHT), OUTLINE_THICKNESS)

    def draw_points(self):
            points_text = self.small_font.render(f"Score: {self.points}", True, FONT_COLOR)
            self.window.blit(points_text, (20, 10))

    def draw(self):
        self.window.fill(BACKGROUND_COLOR)
        for tile in self.tiles.values():
            tile.draw(self.window)
        self.draw_grid()
        self.draw_points()
        pygame.display.update()

    def get_random_pos(self):
        row = None
        col = None
        while True:
            row = random.randrange(0, ROWS)
            col = random.randrange(0, COLS)

            if f"{row}{col}" not in self.tiles:
                break
        
        return row, col

    def move_tiles(self, direction):
        updated = True
        blocks = set()

        if direction == "left":
            sort_func = lambda x: x.col
            reverse = False
            delta = (-MOVE_VEL, 0)
            boundary_check = lambda tile: tile.col == 0
            get_next_tile = lambda tile: self.tiles.get(f"{tile.row}{tile.col - 1}")
            merge_check = lambda tile, next_tile: tile.x > next_tile.x + MOVE_VEL
            move_check = lambda tile, next_tile: tile.x > next_tile.x + RECT_WIDTH + MOVE_VEL
            ceil = True
        elif direction == "right":
            sort_func = lambda x: x.col
            reverse = True
            delta = (MOVE_VEL, 0)
            boundary_check = lambda tile: tile.col == COLS - 1
            get_next_tile = lambda tile: self.tiles.get(f"{tile.row}{tile.col + 1}")
            merge_check = lambda tile, next_tile: tile.x < next_tile.x - MOVE_VEL
            move_check = lambda tile, next_tile: tile.x + RECT_WIDTH + MOVE_VEL < next_tile.x
            ceil = False

        elif direction == "up":
            sort_func = lambda x: x.row
            reverse = False
            delta = (0, -MOVE_VEL)
            boundary_check = lambda tile: tile.row == 0
            get_next_tile = lambda tile: self.tiles.get(f"{tile.row - 1}{tile.col}")
            merge_check = lambda tile, next_tile: tile.y > next_tile.y + MOVE_VEL
            move_check = lambda tile, next_tile: tile.y > next_tile.y + RECT_HEIGHT + MOVE_VEL
            ceil = True

        elif direction == "down":
            sort_func = lambda x: x.row
            reverse = True
            delta = (0, MOVE_VEL)
            boundary_check = lambda tile: tile.row == ROWS - 1
            get_next_tile = lambda tile: self.tiles.get(f"{tile.row + 1}{tile.col}")
            merge_check = lambda tile, next_tile: tile.y < next_tile.y - MOVE_VEL
            move_check = lambda tile, next_tile: tile.y + RECT_HEIGHT + MOVE_VEL < next_tile.y
            ceil = False

        while updated:
            self.clock.tick(FPS)
            updated = False
            sorted_tiles = sorted(self.tiles.values(), key=sort_func, reverse=reverse)

            for i, tile in enumerate(sorted_tiles):
                if boundary_check(tile):
                    continue

                next_tile = get_next_tile(tile)
                if not next_tile:
                    tile.move(delta)
                elif tile.value == next_tile.value and tile not in blocks and next_tile not in blocks:
                    if merge_check(tile, next_tile):
                        tile.move(delta)
                    else:
                        next_tile.value *= 2
                        sorted_tiles.pop(i)
                        blocks.add(next_tile)
                        self.points += next_tile.value
                elif move_check(tile, next_tile):
                    tile.move(delta)
                else:
                    continue
                
                tile.set_pos(ceil)
                updated = True

            self.update_tiles(sorted_tiles)

        return self.end_move()

    def end_move(self):
        if len(self.tiles) == 16:
            for tile in self.tiles.values():
                row, col = tile.row, tile.col
                neighbors = [
                    self.tiles.get(f"{row - 1}{col}"),
                    self.tiles.get(f"{row + 1}{col}"),
                    self.tiles.get(f"{row}{col - 1}"),
                    self.tiles.get(f"{row}{col + 1}")
                ]

                for neighbor in neighbors:
                    if neighbor and neighbor.value == tile.value:
                        return "continue"

            show_end_screen(self.points)
            return "lost"

        row, col = self.get_random_pos()
        self.tiles[f"{row}{col}"] = Tile(random.choice([2, 4]), row, col)
        return "continue"

    def update_tiles(self, sorted_tiles):
        self.tiles.clear()
        for tile in sorted_tiles:
            self.tiles[f"{tile.row}{tile.col}"] = tile

        self.draw()

    def generate_tiles(self):
        for _ in range(2):
            row, col = self.get_random_pos()
            self.tiles[f"{row}{col}"] = Tile(2, row, col)

    def run(self):
        run = True
        while run:
            self.clock.tick(FPS)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
                    break
                
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT:
                        self.move_tiles("left")
                    elif event.key == pygame.K_RIGHT:
                        self.move_tiles("right")
                    elif event.key == pygame.K_UP:
                        self.move_tiles("up")
                    elif event.key == pygame.K_DOWN:
                        self.move_tiles("down")

            self.draw()

        pygame.quit()

if __name__ == "__main__":
    game = Game()
    game.run()




