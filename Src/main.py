import pygame


def main():
    pygame.init()
    screen = pygame.display.set_mode((1920 - 50, 1080 - 100))
    pygame.display.set_caption("Animal Kingdom")
    clock = pygame.time.Clock()

    run = True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        screen.fill((0, 0, 0))
        pygame.display.flip()
        clock.tick(120)
    pygame.quit()


if __name__ == '__main__':
    main()
