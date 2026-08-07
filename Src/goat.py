import pygame.sprite
import random
import main
import animal
import grid
import grass

sex_list = ["male", "female"]
goat = animal.Animal(2, 1, grass.Grass, random.choice(sex_list))

# Sprite
original_goat_img = pygame.image.load("goat_spritesheet.png")
goat_img = pygame.transform.scale(original_goat_img, (300, 300))
animation_index = [5, 84, 163, 242, 321]

class Goat(pygame.sprite.Sprite):
    def __init__(self, width, height, pos_x, pos_y):
        super().__init__()
        self.image = pygame.Surface([width, height])
        self.rect = self.image.get_rect()
        self.rect.center = [pos_x, pos_y]
        self.current_sprite = animation_index[0]

    def spawn_goat(self, pos_x, pos_y):
        main.screen.blit(goat_img, (pos_x, pos_y), (self.current_sprite, animation_index[2] - 10, 70, 85))

    def idle(self):
        current_sprite_index = 1
        self.current_sprite = animation_index[current_sprite_index]
