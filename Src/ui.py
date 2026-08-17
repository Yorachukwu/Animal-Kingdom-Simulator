import pygame

no_lion = 0
no_goat = 0

heart_img = pygame.image.load("Heart.png")
heart_img = pygame.transform.scale(heart_img, (14, 14))

def draw_health(surface, x, y, health, spacing=16):

    for i in range(health):
        surface.blit(heart_img, (x + i * spacing, y))