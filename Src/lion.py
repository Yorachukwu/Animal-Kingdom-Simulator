import random
import pygame.sprite
import main
import goat
import grid
import constants
import ui

# Sprite
original_lion_img = pygame.image.load("lion_spritesheet.png")
# lion_img = pygame.transform.scale(original_lion_img, (300, 300))
lion_img = pygame.image.load(r"C:\Users\VICTUS\PycharmProjects\Animal Kingdom Simulator\Assets\Sprites\lion.png")

animation_index = [5, 84, 163, 242, 321]


class Lion(pygame.sprite.Sprite):
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
        self.owner = None
        self.steps_since_meal = 0
        self.reproduction_timer = 0
        self.facing = "down"
        self.animation_frame = 0
        self.animation_timer = 0

    def spawn_lion(self, pos_x, pos_y):
        self.location = [pos_x, pos_y]
        self.rect = pygame.Rect(pos_x, pos_y + 10, 65, 65)

        self.animation_timer += 1
        if self.animation_timer >= 6:
            self.animation_timer = 0
            self.animation_frame = (self.animation_frame + 1) % constants.Lion_frame_count

        direction_row = {
            "up": constants.Lion_row_top,
            "left": constants.Lion_row_left,
            "right": constants.Lion_row_right,
            "down": constants.Lion_row_bottom,
        }
        row = direction_row.get(self.facing, constants.Lion_row_bottom)

        frame_x = self.animation_frame * constants.Lion_frame_size
        frame_y = row * constants.Lion_frame_size

        tint = (150, 255, 150) if self.sex == "Male" else (255, 150, 150)
        tinted_img = lion_img.copy()
        tinted_img.fill(tint, special_flags=pygame.BLEND_RGB_MULT)

        main.screen.blit(tinted_img, self.location,
                         (frame_x, frame_y, constants.Lion_frame_size, constants.Lion_frame_size))
        pygame.draw.rect(main.screen, (255, 0, 0), self.rect, 2)

        if self.owner is not None:
            ui.draw_health(main.screen, self.location[0], self.location[1] - 16, self.owner.health)

        return self

    def idle(self):
        current_sprite_index = 1
        self.current_sprite = animation_index[current_sprite_index]
        return self

    def move(self):
        # Only choose a new destination once we've actually reached the current one
        if self.location == self.target_location:
            move_direction = random.choice(["up", "down", "left", "right", "none"])
            self.facing = move_direction if move_direction != "none" else self.facing

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
                return self

            if new_target in grid.occupied_spaces:
                return self

            if self.location in grid.occupied_spaces:
                grid.occupied_spaces.remove(self.location)
            grid.occupied_spaces.append(new_target)
            self.target_location = new_target

            self.steps_since_meal += 1
            if self.steps_since_meal >= constants.lion_steps_before_damage:
                self.steps_since_meal = 0
                if self.owner is not None:
                    self.owner.take_damage(1)

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

    def can_reproduce(self):
        return self.reproduction_timer <= 0

    def tick_reproduction_timer(self):
        if self.reproduction_timer > 0:
            self.reproduction_timer -= 1
