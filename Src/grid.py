import pygame
from tile import Tile
import constants

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