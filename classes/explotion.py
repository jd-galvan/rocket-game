import pygame

COUNTER_TO_CHANGE_SPRITE = 3
SPRITES = []
for i in range(16):
    SPRITES.append(f"./sprites/explotion/tile0{str(i).zfill(2)}.png")


class Explotion(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.index = 0
        self.image = pygame.image.load(SPRITES[self.index])
        self.counter = 0
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def update(self):
        self.counter += 1
        if self.counter > COUNTER_TO_CHANGE_SPRITE:
            self.counter = 0
            self.index += 1
            if self.index >= len(SPRITES):
                self.kill()
            else:
                self.image = pygame.image.load(SPRITES[self.index])
