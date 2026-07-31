import pygame
from tile import Tile
import constants as const

class Grid:
    def __init__(self):
        self.tiles = [[Tile(r, col) for col in range(const.Columns)] for r in range(const.Rows)]

    def get_tile(self, row, col):
        if 0 <= row < const.Rows and 0 <= col < const.Columns:
            return self.tiles[row][col]
        return None
    def get_neighbours(self, row, col, radius=1):
        neighbours = []
        for r in range(row - radius, row + radius + 1):
            for colIndex in range(col - radius, col + radius + 1):
                if (r, colIndex) != (row, col):
                    tile = self.get_tile(r, colIndex)
                    if tile:
                        neighbours.append(tile)
        return neighbours
    def draw(self, surface):
        for row in self.tiles:
            for tile in row:
                x = tile.col * const.Tile_size
                y = tile.row * const.Tile_size
                rect = (x,y, const.Tile_size, const.Tile_size)
                pygame.draw.rect(surface, (60, 60, 60), rect, 1)
