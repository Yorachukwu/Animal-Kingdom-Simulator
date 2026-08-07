import pygame
from tile import Tile
import grid
import constants as const
import lion
import goat
import random
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
    print(grid.row_spaces, grid.column_spaces)

    def draw_BG(self, surface):
        screen.blit(background, (0, 0))
        # The Grid
        for row in tiles:
            for tile in row:
                x = tile.col * const.Tile_size
                y = tile.row * const.Tile_size
                rect = pygame.Rect(x, y, const.Tile_size, const.Tile_size)
                pygame.draw.rect(surface, (150, 150, 150), rect, 1)

    def draw_animals():

        # # Lion Handling
        # lion_anim = lion.Lion(1, 1, 50, 50)
        # lion_anim.spawn_lion(random_location1[0], random_location1[1])
        # lion_anim.idle()
        #
        # # Goat handling
        # goat_anim = goat.Goat(1, 1, 50, 50)
        # goat_anim.spawn_goat(random_location2[0], random_location2[1])
        # goat_anim.idle()
        animal1 = animal.Animal(None, None, None, None)
        animal1.spawn_animal()
        animal2 = animal.Animal(None, None, None, None)
        animal2.spawn_animal()
        animal3 = animal.Animal(None, None, None, None)
        animal3.spawn_animal()
        animal4 = animal.Animal(None, None, None, None)
        animal4.spawn_animal()

    run = True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        screen.fill((20, 20, 20))

        draw_BG(tiles, screen)
        draw_animals()

        pygame.display.flip()
        clock.tick(const.FPS)
    pygame.quit()

if __name__ == '__main__':
    main()
