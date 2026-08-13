def get_active_sprites(animals):

    sprites = []
    for a in animals:
        if a.breed == "Lion" and a.lion is not None:
            sprites.append(a.lion)
        elif a.breed == "Goat" and a.goat is not None:
            sprites.append(a.goat)
    return sprites


def check_collisions(animals):
    sprites = get_active_sprites(animals)
    collisions = []

    for i in range(len(sprites)):
        for j in range(i + 1, len(sprites)):
            a, b = sprites[i], sprites[j]
            if a.rect.colliderect(b.rect):
                collisions.append((a, b))

    return collisions
