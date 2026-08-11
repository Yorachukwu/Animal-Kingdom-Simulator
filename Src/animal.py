import grid
import random
import lion as lion_script
import goat as goat_script

has_location = False

class Animal:
    is_alive = True

    def __init__(self, health, speed, food, sex):
        breed_list = ["Lion", "Goat"]
        self. breed = random.choice(breed_list)
        self.food = None
        self.health = health
        self.speed = speed
        self.has_location = has_location

    def spawn_animal(self):
        health = 0

        # FOR THE LION
        if self.breed == "Lion":

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
                    lion = lion_script.Lion(1, 1, 50, 50).spawn_lion(spawn_location[0], spawn_location[1])
                    grid.spawn_location_in_use.append([spawn_location[0], spawn_location[1]])

        # FOR THE GOAT
        elif self.breed == "Goat":

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
                    goat = goat_script.Goat(1, 1, 50, 50).spawn_goat(spawn_location[0], spawn_location[1])
                    grid.spawn_location_in_use.append([spawn_location[0], spawn_location[1]])

        else:
            pass
