import pygame.sprite
import random
import main
import grass
import grid
import constants

# Sprite
original_goat_img = pygame.image.load("goat_spritesheet.png")
goat_img = pygame.transform.scale(original_goat_img, (300, 300))
animation_index = [5, 84, 163, 242, 321]


class Goat(pygame.sprite.Sprite):
    def __init__(self, width, height, pos_x, pos_y, location, sex, speed):
        super().__init__()
        self.image = pygame.Surface([width, height])
        self.rect = self.image.get_rect()
        self.rect.center = [pos_x, pos_y]
        self.current_sprite = animation_index[0]
        self.location = location
        self.target_location = list(location)
        self.sex = sex
        self.speed = speed

    def spawn_goat(self, pos_x, pos_y):
        self.location = [pos_x, pos_y]
        self.rect = pygame.Rect(pos_x, pos_y+10, 65, 65)

        tint = (150, 150, 255) if self.sex == "Male" else (255, 150, 150)
        tinted_img = goat_img.copy()
        tinted_img.fill(tint, special_flags=pygame.BLEND_RGB_MULT)

        main.screen.blit(tinted_img, self.location, (self.current_sprite, animation_index[2] - 10, 70, 85))
        pygame.draw.rect(main.screen, (255, 0, 0), self.rect, 2)
        grid.occupied_spaces.append(self.location)
        return self

    def idle(self):
        current_sprite_index = 1
        self.current_sprite = animation_index[current_sprite_index]
        return self

    def move(self):
        # Only choose a new destination once we've actually reached the current one
        if self.location == self.target_location:
            move_direction = random.choice(["up", "down", "left", "right", "none"])
            new_target = list(self.location)

            if move_direction == "up" and self.location[1] < constants.Rows * constants.Tile_size:
                new_target[1] += constants.Tile_size
            elif move_direction == "down" and self.location[1] > 0:
                new_target[1] -= constants.Tile_size
            elif move_direction == "left" and self.location[0] > 0:
                new_target[0] -= constants.Tile_size
            elif move_direction == "right" and self.location[0] < constants.Columns * constants.Tile_size:
                new_target[0] += constants.Tile_size
            else:
                return self  # "none", or blocked by the edge — stay put this frame

            if new_target in grid.occupied_spaces:
                return self  # someone's already headed there or standing there

            if self.location in grid.occupied_spaces:
                grid.occupied_spaces.remove(self.location)
            grid.occupied_spaces.append(new_target)
            self.target_location = new_target

        # Step a few pixels closer to the target, every frame, until we arrive
        dx = self.target_location[0] - self.location[0]
        dy = self.target_location[1] - self.location[1]

        if abs(dx) <= self.speed:
            self.location[0] = self.target_location[0]
        elif dx != 0:
            self.location[0] += self.speed if dx > 0 else -self.speed

        if abs(dy) <= self.speed:
            self.location[1] = self.target_location[1]
        elif dy != 0:
            self.location[1] += self.speed if dy > 0 else -self.speed

        return self

    def Reproduce(self):
        pass