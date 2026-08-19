# import pygame
# from tile import Tile
import constants
import random

column_spaces = []
row_spaces = []
grid_space = constants.Tile_size

occupied_spaces = []
initial_spawn_locations = []
spawn_location_in_use = []

all_positions = [[col * grid_space, row * grid_space]
                 for col in range(constants.Columns)
                 for row in range(constants.Rows)]


def generate_positions():

    random_location1 = [random.choice(column_spaces) * grid_space,
                        random.choice(row_spaces) * grid_space]

    random_location2 = [random.choice(column_spaces) * grid_space,
                        random.choice(row_spaces) * grid_space]

    random_location3 = [random.choice(column_spaces) * grid_space,
                        random.choice(row_spaces) * grid_space]

    random_location4 = [random.choice(column_spaces) * grid_space,
                        random.choice(row_spaces) * grid_space]

    occupied_spaces.append(random_location1)
    occupied_spaces.append(random_location2)
    occupied_spaces.append(random_location3)
    occupied_spaces.append(random_location4)

    initial_spawn_locations.append(random_location1)
    initial_spawn_locations.append(random_location2)
    initial_spawn_locations.append(random_location3)
    initial_spawn_locations.append(random_location4)

def find_nearby_space(location, radius = 1):
    x, y = location
    candidate = []
    r = radius
    max_radius = max(constants.Rows, constants.Columns)

    while not candidate and r <= max_radius:
        for dx in range(-r, r+1):
            for dy in range(-r, r+1):
                if dx == 0 and dy == 0:
                    continue
                pos = [x + dx * grid_space, y + dy * grid_space]
                if 0 <= pos[0] < constants.Columns * grid_space and 0 <= pos[1] < constants.Rows * grid_space:
                    if pos not in occupied_spaces:
                        candidate.append(pos)

        r += 1

    return random.choice(candidate) if candidate else None