import pygame.sprite
import main
import animal

lion = animal.Animal(5, 3, animal.Animal)

# Sprite
original_lion_img = pygame.image.load("lion_spritesheet.png")
lion_img = pygame.transform.scale(original_lion_img, (300, 300))
anim_index = [5, 84, 163, 242, 321]

class Lion(pygame.sprite.Sprite):
    def __init__(self, width, height, pos_x, pos_y, color):
        super().__init__()
        self.image = pygame.Surface([width, height])
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.rect.center = [pos_x, pos_y]
        self.current_sprite = anim_index[0]

        top = 53

    def idle(self):
        current_sprite_index =1
        self.current_sprite = anim_index[current_sprite_index]
        main.screen.blit(lion_img, (5, 5), (self.current_sprite, anim_index[3], 70, 85))

        if self.current_sprite < len(anim_index):
            self.current_sprite += 1
        else:
            current_sprite = 0

        self.current_sprite += 1

        if self.current_sprite >= len(anim_index):
            self.current_sprite = 0


