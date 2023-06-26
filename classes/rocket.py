from typing import Any
import pygame

INITIAL_POSITION_X = 320
INITIAL_POSITION_Y = 540
COUNTER_TO_CHANGE_IMG = 6
SPRITES = []
for i in range(8):
    SPRITES.append(f"./sprites/rocket/tile00{i}.png")


class Rocket(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.index = 0
        self.counter = 0
        self.image = pygame.image.load(SPRITES[self.index])
        self.rect = self.image.get_rect()
        self.rect.x = INITIAL_POSITION_X
        self.rect.y = INITIAL_POSITION_Y
        self.speed_x = 0

    def animate(self):
        self.counter += 1
        if self.counter > COUNTER_TO_CHANGE_IMG:
            self.counter = 0
            self.index += 1
            if self.index >= len(SPRITES):
                self.index = 0
            self.image = pygame.image.load(SPRITES[self.index])

    def move(self):
        if 720 - self.image.get_width() > self.rect.x + self.speed_x > 0:
            self.rect.x += self.speed_x

    def change_speed(self, speed):
        self.speed_x = speed

    def update(self):
        self.animate()
        self.move()
