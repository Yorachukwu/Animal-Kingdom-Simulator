import random
import pygame.sprite
import main
import goat
import grid
import constants

sex_list = ["male", "female"]

# Sprite
original_lion_img = pygame.image.load("lion_spritesheet.png")
lion_img = pygame.transform.scale(original_lion_img, (300, 300))
animation_index = [5, 84, 163, 242, 321]


class Lion(pygame.sprite.Sprite):
    def __init__(self, width, height, pos_x, pos_y, location):
        super().__init__()
        self.image = pygame.Surface([width, height])
        self.rect = self.image.get_rect()
        self.rect.center = [pos_x, pos_y]
        self.current_sprite = animation_index[0]
        self.location = location

    def spawn_lion(self, pos_x, pos_y):
        self.location = [pos_x, pos_y]
        main.screen.blit(lion_img, self.location, (self.current_sprite, animation_index[2]-10, 70, 85))
        return self

    def idle(self):
        current_sprite_index = 1
        self.current_sprite = animation_index[current_sprite_index]
        return self

    def move(self):
        move_direction = ["up", "down", "left", "right", "none"]
        if random.choice(move_direction) == "up":
            self.location[1] += constants.Tile_size
        elif random.choice(move_direction) == "down":
            self.location[1] -= constants.Tile_size
        elif random.choice(move_direction) == "left":
            self.location[0] -= constants.Tile_size
        elif random.choice(move_direction) == "right":
            self.location[0] += constants.Tile_size
        elif random.choice(move_direction) == "none":
            pass
        return self