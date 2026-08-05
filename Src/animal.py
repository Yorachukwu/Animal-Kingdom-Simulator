import pygame
import tile
class Animal():

    is_alive = True

    def __init__(self, health, speed, food):
        self.health = health
        self.speed = speed
        self.food = food


    def Move(self):
        is_alive = True
        clock = pygame.time.wait(3000)


