import pygame
from tile import Tile
import constants
import random

column_spaces = []
row_spaces = []
grid_space = constants.Tile_size

occupied_spaces = []
initial_spawn_locations = []
spawn_location_in_use = []

# has_random_location1 = False
# has_random_location2 = False
# has_random_location3 = False
# has_random_location4 = False

def generate_positions():
    global random_location1, random_location2, random_location3, random_location4

    # Sprite locations
    random_location1 = [random.choice(column_spaces) * grid_space,
                        random.choice(row_spaces) * grid_space]

    random_location2 = [random.choice(column_spaces) * grid_space,
                        random.choice(row_spaces) * grid_space]

    random_location3 = [random.choice(column_spaces) * grid_space,
                        random.choice(row_spaces) * grid_space]

    random_location4 = [random.choice(column_spaces) * grid_space,
                        random.choice(row_spaces) * grid_space]

    occupied_spaces.append([random_location1[0], random_location1[1]])
    occupied_spaces.append([random_location2[0], random_location2[1]])
    occupied_spaces.append([random_location3[0], random_location3[1]])
    occupied_spaces.append([random_location4[0], random_location4[1]])

    initial_spawn_locations.append(random_location1)
    initial_spawn_locations.append(random_location2)
    initial_spawn_locations.append(random_location3)
    initial_spawn_locations.append(random_location4)

    print(occupied_spaces)
