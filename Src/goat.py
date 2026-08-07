import pygame.sprite
import main
import animal
import grass

# Animal = (health, speed, food)
goat = animal.Animal(2, 1, grass.Grass)

# Sprite
goat_img = pygame.image.load("goat_spritesheet.png")

class Goat(pygame.sprite.Sprite):
    def __init__(self, width, height, pos_x, pos_y, color):
        super().__init__()
        self.image = pygame.Surface([width, height])
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.rect.center = [pos_x, pos_y]

    def draw_sprite(self):
        # Every 48 changes its row with an initial offset of 5
        # {5, 53, 101, 149, 197}
        # { idle_row = 101
        #  die_row = 149
        #  walk_row = 53
        # }

        top = 53
        left = 53

        def idle():
            main.screen.blit(goat_img, (5, 5), (left, top, 50, 55))
