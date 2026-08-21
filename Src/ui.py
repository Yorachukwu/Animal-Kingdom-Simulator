import pygame

pygame.font.init()
count_font = pygame.font.SysFont(None, 26, bold=True)

heart_img = pygame.image.load("Heart.png")
heart_img = pygame.transform.scale(heart_img, (14, 14))


def draw_health(surface, x, y, health):
    spacing = 16
    for i in range(health):
        surface.blit(heart_img, (x + i * spacing, y))


def draw_animal_counts(surface, lion_count, goat_count, top_y):
    entries = [f"Lion: {lion_count}", f"Goat: {goat_count}"]
    padding = 6
    spacing = 20
    x = 10

    for text in entries:
        text_surf = count_font.render(text, True, (255,255,255))
        bg_rect = text_surf.get_rect(topleft=(x, top_y)).inflate(padding * 2, padding * 2)
        pygame.draw.rect(surface, (0, 0, 0), bg_rect)
        surface.blit(text_surf, (bg_rect.x + padding, bg_rect.y + padding))
        x = bg_rect.right + spacing
