import pygame
from tile import Tile
import constants
import random

# class Grid:
#     def __init__(self):
#         self.health = None
#
#     def get_tile(self, row, col):
#         if 0 <= row < constants.Rows and 0 <= col < constants.Columns:
#             return self.tiles[row][col]
#         return None
#
#     def draw(self, surface):
#         for row in self.tiles:
#             for tile in row:
#                 x = tile.col * constants.Tile_size
#                 y = tile.row * constants.Tile_size
#                 rect = pygame.Rect(x, y, constants.Tile_size, constants.Tile_size)
#                 pygame.draw.rect(surface, (60, 60, 60), rect, 1)



column_spaces = []
row_spaces = []
grid_space = constants.Tile_size

occupied_spaces = []

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
    print(occupied_spaces)