import pygame
import grid
from grid import Grid
import constants as const

def main():
    pygame.init()
    screen = pygame.display.set_mode((const.screen_width, const.screen_height))
    pygame.display.set_caption("Animal Kingdom")
    clock = pygame.time.Clock()

    run = True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        screen.fill((20, 20, 20))
        Grid.draw(screen)

        for row in range(const.Rows):
            rect = pygame.Rect(const.Columns * const.Tile_size, const.Rows * const.Tile_size, const.Tile_size, const.Tile_size)
            pygame.draw.rect(screen, (60,60,60), rect, 1)


        pygame.display.flip()
        clock.tick(const.FPS)
    pygame.quit()


if __name__ == '__main__':
    main()
