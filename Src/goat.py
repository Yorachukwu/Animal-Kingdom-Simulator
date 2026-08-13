import pygame.sprite
import random
import main
import grass
import grid
import constants

sex_list = ["male", "female"]

# Sprite
original_goat_img = pygame.image.load("goat_spritesheet.png")
goat_img = pygame.transform.scale(original_goat_img, (300, 300))
animation_index = [5, 84, 163, 242, 321]


class Goat(pygame.sprite.Sprite):
    def __init__(self, width, height, pos_x, pos_y, location):
        super().__init__()
        self.image = pygame.Surface([width, height])
        self.rect = self.image.get_rect()
        self.rect.center = [pos_x, pos_y]
        self.current_sprite = animation_index[0]
        self.location = location

    def spawn_goat(self, pos_x, pos_y):

        self.location = [pos_x, pos_y]
        self.rect = pygame.Rect(pos_x, pos_y, 70, 85)
        main.screen.blit(goat_img, self.location, (self.current_sprite, animation_index[2] - 10, 70, 85))
        pygame.draw.rect(main.screen, (255, 0, 0), self.rect, 2)
        grid.occupied_spaces.append(self.location)
        return self

    def idle(self):
        current_sprite_index = 1
        self.current_sprite = animation_index[current_sprite_index]
        return self

    def move(self):
        move_direction = ["up", "down", "left", "right", "none"]
        if random.choice(move_direction) == "up":
            if self.location[1] < constants.Rows * constants.Tile_size:
                if self.location in grid.occupied_spaces:
                    grid.occupied_spaces.remove(self.location)
                    self.location[1] += constants.Tile_size
                    grid.occupied_spaces.append(self.location)

        elif random.choice(move_direction) == "down":
            if self.location[1] > 0:
                if self.location in grid.occupied_spaces:
                    grid.occupied_spaces.remove(self.location)
                    self.location[1] -= constants.Tile_size
                    grid.occupied_spaces.append(self.location)

        elif random.choice(move_direction) == "left":
            if self.location[0] > 0:
                if self.location in grid.occupied_spaces:
                    grid.occupied_spaces.remove(self.location)
                    self.location[0] -= constants.Tile_size
                    grid.occupied_spaces.append(self.location)

        elif random.choice(move_direction) == "right":
            if self.location[0] < constants.Columns * constants.Tile_size:
                if self.location in grid.occupied_spaces:
                    grid.occupied_spaces.remove(self.location)
                    self.location[0] += constants.Tile_size
                    grid.occupied_spaces.append(self.location)

        elif random.choice(move_direction) == "none":
            pass
        return self

    def get_neighbours(self):
        above = [self.location[1] + constants.Tile_size]
        below = [self.location[1] - constants.Tile_size]
        left = [self.location[0] - constants.Tile_size]
        right = [self.location[0] + constants.Tile_size]

        

        if above in grid.occupied_spaces:
            pass
        if below in grid.occupied_spaces:
            pass
        if left in grid.occupied_spaces:
            pass
        if right in grid.occupied_spaces:
            pass
