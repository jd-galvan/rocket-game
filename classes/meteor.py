import pygame
import random

METEOR_WIDTH = 40
METEOR_HEIGHT = 40

SCREEN_WIDTH = 720


class Meteor(pygame.sprite.Sprite):
    def __init__(self, x, y, speed):
        super().__init__()
        self.image = pygame.image.load("./sprites/meteor.png").convert()
        self.image = pygame.transform.scale(
            self.image, [METEOR_WIDTH, METEOR_HEIGHT])
        self.image.set_colorkey([0, 0, 0])
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.speed_y = speed

    def update(self):
        self.rect.y += self.speed_y
        if self.rect.y > 720:
            self.rect.x = random.randint(0, SCREEN_WIDTH - 30)
            self.rect.y = 0
