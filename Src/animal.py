import grid
import random
import lion as lion_script
import goat as goat_script

has_location = False


class Animal:
    def __init__(self, health, speed, food, sex):
        breed_list = ["Lion", "Goat"]
        sex_list = ["Male", "Female"]
        self. breed = random.choice(breed_list)
        self.sex = random.choice(sex_list)
        self.food = None
        self.health = health
        self.speed = speed
        self.has_location = has_location
        self.lion = None
        self.goat = None
        self.is_alive = True

    def spawn_animal(self):
        health = 0

        # FOR THE LION
        if self.breed == "Lion":
            self.speed = 2
            self.food = "Goat"
            health = 5
            speed = 3
            grid.generate_positions()

            while not self.has_location:
                spawn_location = random.choice(grid.initial_spawn_locations)
                if spawn_location in grid.spawn_location_in_use:
                    pass
                else:
                    self.has_location = True
                    self.lion = lion_script.Lion(1, 1, 50, 50, [spawn_location[0], spawn_location[1]], self.sex, self.speed)
                    self.lion.spawn_lion(spawn_location[0], spawn_location[1])
                    self.lion.owner = self
                    grid.spawn_location_in_use.append([spawn_location[0], spawn_location[1]])

        # FOR THE GOAT
        elif self.breed == "Goat":
            self.speed = 1
            self.food = "Grass"
            health = 3
            speed = 1
            grid.generate_positions()

            while not self.has_location:
                spawn_location = random.choice(grid.initial_spawn_locations)
                if spawn_location in grid.spawn_location_in_use:
                    pass
                else:
                    self.has_location = True
                    self.goat = goat_script.Goat(1, 1, 50, 50, [spawn_location[0], spawn_location[1]], self.sex, self.speed)
                    self.goat.spawn_goat(spawn_location[0], spawn_location[1])
                    self.goat.owner = self
                    grid.spawn_location_in_use.append([spawn_location[0], spawn_location[1]])

    def move_animal(self):
        if not self.is_alive:
            return

        if self.breed == "Lion":
            self.lion.move()
            self.lion.spawn_lion(self.lion.location[0], self.lion.location[1])
        elif self.breed == "Goat":
            self.goat.move()
            self.goat.spawn_goat(self.goat.location[0], self.goat.location[1])

    def kill(self):
        self.is_alive = False
        sprite = self.lion if self.breed == "Lion" else self.goat
        if sprite and sprite.location in grid.occupied_spaces:
            grid.occupied_spaces.remove(sprite.location)
