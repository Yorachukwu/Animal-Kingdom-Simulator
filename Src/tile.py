class Tile:
    def __init__(self, row, col, max_animals=2):
        self.row = row
        self.col = col
        self.has_grass = False
        self.animals = []
        self.max_animals = max_animals

    def is_free_for(self, animal):
        return len(self.animals) < self.max_animals


