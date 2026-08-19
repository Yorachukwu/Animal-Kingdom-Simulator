import pygame
from tile import Tile
import grid
import constants as const
import animal
import grass
import simulation

screen = pygame.display.set_mode((const.screen_width, const.screen_height))


def main():
    pygame.init()
    pygame.display.set_caption("Animal Kingdom")
    clock = pygame.time.Clock()

    # Sprites
    background = pygame.image.load("grass_field.png")

    # Getting the tiles
    tiles = []
    for row in range(const.Rows):

        # adding each row and column to the grid for coordinates
        grid.row_spaces.append(row)
        grid.column_spaces.append(row)
        row_list = []
        for col in range(const.Columns):
            row_list.append(Tile(row, col))
        tiles.append(row_list)

    def draw_BG(self, surface):
        screen.blit(background, (0, 0))
        # The Grid
        for row in tiles:
            for tile in row:
                x = tile.col * const.Tile_size
                y = tile.row * const.Tile_size
                rect = pygame.Rect(x, y, const.Tile_size, const.Tile_size)
                pygame.draw.rect(surface, (150, 150, 150), rect, 1)

    animals = []

    def draw_animals():
        # NUMBER OF ANIMALS TO SPAWN
        for i in range(const.Number_of_animals):

            new_aniimal1 = animal.Animal(None, None, None, None)
            new_aniimal1.spawn_animal()
            animals.append(new_aniimal1)

    screen.fill((20, 20, 20))
    draw_BG(tiles, screen)
    draw_animals()

    run = True
    while run:

        # Checks for close button
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        screen.fill((20, 20, 20))
        draw_BG(tiles, screen)

        grass.update()
        grass.draw_flowers(screen)

        for i in animals:

            i.move_animal()

        grass.check_goat_eating(animals)

        # CHECKING ANIMAL COLLISIONS AND GETTING INFORMATION
        for sprite_a, sprite_b in simulation.check_collisions(animals):
            animal_a = sprite_a.owner
            animal_b = sprite_b.owner

            if animal_a.breed == "Lion" and animal_b.breed == "Goat":
                lion_sprite, goat_sprite = sprite_a, sprite_b
            elif animal_b.breed == "Lion" and animal_a.breed == "Goat":
                lion_sprite, goat_sprite = sprite_b, sprite_a
            else:
                lion_sprite, goat_sprite = None, None

            if lion_sprite is not None:
                goat_animal = goat_sprite.owner
                if goat_sprite.escape_timer <= 0:
                    lion_sprite.steps_since_meal = 0
                    goat_animal.take_damage(1)
                    if goat_animal.is_alive:
                        goat_sprite.flee_from(lion_sprite.location)

            elif animal_a.breed == animal_b.breed and sprite_a.sex != sprite_b.sex:
                if sprite_a.can_reproduce() and sprite_b.can_reproduce():
                    nearby = grid.find_nearby_space(sprite_a.location)
                    if nearby is not None:
                        baby = animal.Animal(None, None, None, None)
                        baby.breed = animal_a.breed
                        baby.spawn_animal_at(nearby)
                        animals.append(baby)

                        sprite_a.reproduction_timer = const.reproduction_cooldown
                        sprite_b.reproduction_timer = const.reproduction_cooldown

        for a in animals:
            if not a.is_alive:
                continue
            if a.breed == "Goat" and a.goat is not None:
                a.goat.tick_escape_timer()
                a.goat.tick_reproduction_timer()
            elif a.breed == "Lion" and a.lion is not None:
                a.lion.tick_reproduction_timer()

        pygame.display.flip()
        clock.tick(const.FPS)
    pygame.quit()


if __name__ == '__main__':
    main()


