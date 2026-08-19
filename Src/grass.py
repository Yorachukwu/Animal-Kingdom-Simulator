import pygame
import random
import grid
import constants

original_flower_img = pygame.image.load("Flower.png")
flower_img = pygame.transform.scale(original_flower_img, (40, 40))

active_flowers = []
flower_spaces = []   # tiles currently holding a flower, so two don't stack
spawn_timer = 0
max_flowers = 10

class Grass():
    def __init__(self, location):
        self.location = location
        self.rect = pygame.Rect(location[0], location[1], 20, 20)

    def draw(self, surface):
        surface.blit(flower_img, self.location)

def spawn_flower():
    if len(active_flowers) >= max_flowers:
        return

    available = [pos for pos in grid.all_positions if pos not in grid.occupied_spaces and pos not in flower_spaces]

    if not available:
        return

    location = random.choice(available)
    active_flowers.append(Grass(location))
    flower_spaces.append(location)

def update():
    global spawn_timer
    spawn_timer += 1
    if spawn_timer >= constants.grass_grow_rate:
        spawn_timer = 0
        spawn_flower()

def draw_flowers(surface):
    for flower in active_flowers:
        flower.draw(surface)

def check_goat_eating(animals):
    for a in animals:
        if a.breed == "Goat" and a.is_alive and a.goat is not None:
            goat_sprite = a.goat
            for flower in active_flowers[:]:
                if goat_sprite.rect.colliderect(flower.rect):
                    if a.health < a.max_health:
                        a.heal(1)
                    active_flowers.remove(flower)
                    flower_spaces.remove(flower.location)
                    break
