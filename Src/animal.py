import pygame
import grid
import random
import lion as lion_script
import goat as goat_script
class Animal():

    is_alive = True

    def __init__(self, health, speed, food, sex):
        breed_list = ["Lion", "Goat"]
        self. breed = random.choice(breed_list)
        self.food = None
        self.health = health
        self.speed = speed

    def spawn_animal(self):
        health = 0
        if self.breed == "Lion":
            self.food = "Goat"
            health = 5
            speed = 3
            grid.generate_positions()
            lion = lion_script.Lion(1, 1, 50, 50).spawn_lion(grid.random_location1[0], grid.random_location1[1])
        elif self.breed == "Goat":
            self.food = "Grass"
            health = 3
            speed = 1
            grid.generate_positions()
            goat = goat_script.Goat(1, 1, 50, 50).spawn_goat(grid.random_location1[0], grid.random_location1[1])


