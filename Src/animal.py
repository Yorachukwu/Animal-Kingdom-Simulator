import pygame
import tile
class Animal():

    is_alive = True

    def __init__(self, health, speed, sex):
        self.health = health
        self.speed = speed
        self.sex = sex


    def Move(self):
        is_alive = True
        clock = pygame.time.wait(3000)

    def spawn_animal(self):
        self.sex = None

