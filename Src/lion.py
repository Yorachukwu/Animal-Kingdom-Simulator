import random
import pygame.sprite
import main
import goat

sex_list = ["male", "female"]
# lion = animal.Animal(5, 3, goat.Goat(None, None, None, None), random.choice(sex_list))

# Sprite
original_lion_img = pygame.image.load("lion_spritesheet.png")
lion_img = pygame.transform.scale(original_lion_img, (300, 300))
animation_index = [5, 84, 163, 242, 321]


class Lion(pygame.sprite.Sprite):
    def __init__(self, width, height, pos_x, pos_y):
        super().__init__()
        self.image = pygame.Surface([width, height])
        self.rect = self.image.get_rect()
        self.rect.center = [pos_x, pos_y]
        self.current_sprite = animation_index[0]

    def spawn_lion(self, pos_x, pos_y):
        main.screen.blit(lion_img, (pos_x, pos_y), (self.current_sprite, animation_index[2]-10, 70, 85))

    def idle(self):
        current_sprite_index = 1
        self.current_sprite = animation_index[current_sprite_index]
