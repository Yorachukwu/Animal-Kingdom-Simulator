import pygame
from tile import Tile
import constants as const
import animal
import lion
import goat
import grass


def main():
    pygame.init()
    screen = pygame.display.set_mode((const.screen_width, const.screen_height))
    pygame.display.set_caption("Animal Kingdom")
    clock = pygame.time.Clock()

    # Background
    background = pygame.image.load("grass_field.png")

    tiles = [
        [Tile(row, col) for col in range(const.Columns)]
        for row in range(const.Rows)
    ]

    # Creating the lion sprite
    lion_anim = lion.Lion(50, 50, 40, 40, (255, 255, 255))
    lion_group = pygame.sprite.Group()
    lion_group.add(lion_anim)

    def draw_BG(self, surface):
        screen.blit(background, (0,0))
        for row in tiles:
            for tile in row:
                x = tile.col * const.Tile_size
                y = tile.row * const.Tile_size
                rect = pygame.Rect(x, y, const.Tile_size, const.Tile_size)
                pygame.draw.rect(surface, (150, 150, 150), rect, 1)

    def draw_animals():
        lion_group.draw(screen)

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
