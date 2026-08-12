import pygame
from tile import Tile
import grid
import constants as const
import animal

screen = pygame.display.set_mode((const.screen_width, const.screen_height))


def main():
    pygame.init()
    pygame.display.set_caption("Animal Kingdom")
    clock = pygame.time.Clock()

    # Sprites
    background = pygame.image.load("grass_field.png")

    # Getting the tiles
    tiles = []
    for row in range(const.Rows):

        # adding each row and column to the grid for coordinates
        grid.row_spaces.append(row)
        grid.column_spaces.append(row)
        row_list = []
        for col in range(const.Columns):
            row_list.append(Tile(row, col))
        tiles.append(row_list)

    def draw_BG(self, surface):
        screen.blit(background, (0, 0))
        # The Grid
        for row in tiles:
            for tile in row:
                x = tile.col * const.Tile_size
                y = tile.row * const.Tile_size
                rect = pygame.Rect(x, y, const.Tile_size, const.Tile_size)
                pygame.draw.rect(surface, (150, 150, 150), rect, 1)

    animals = []
    # grid.generate_positions()
    def draw_animals():
        for i in range(10):

            new_aniimal1 = animal.Animal(None, None, None, None)
            new_aniimal1.spawn_animal()
            animals.append(new_aniimal1)

    screen.fill((20, 20, 20))
    draw_BG(tiles, screen)
    draw_animals()

    run = True
    while run:

        # Checks for close button
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        screen.fill((20, 20, 20))
        draw_BG(tiles, screen)
        for i in animals:

            i.move_animal()

        pygame.display.flip()
        clock.tick(const.FPS)
    pygame.quit()


if __name__ == '__main__':
    main()
