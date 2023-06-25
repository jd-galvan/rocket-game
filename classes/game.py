from .rocket import Rocket
from .meteor import Meteor
from .explotion import Explotion
import pygame
import random

SCREEN_WIDTH = 720
SCREEN_HEIGHT = 720

VELOCITY_FACTOR_LEFT = -5
VELOCITY_FACTOR_RIGHT = 5


class Game(object):
    def __init__(self):
        self.rocket = Rocket()
        self.all_sprites = pygame.sprite.Group()
        self.meteor_group = pygame.sprite.Group()
        self.all_sprites.add(self.rocket)
        self.background = pygame.image.load(
            "./images/space-background.jpg").convert()

        for _ in range(5):
            meteor = Meteor(random.randint(
                10, SCREEN_WIDTH - 10), 0, random.randint(1, 5))
            self.meteor_group.add(meteor)
            self.all_sprites.add(meteor)

    # Return True if window is closed

    def process_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    self.rocket.change_speed(VELOCITY_FACTOR_LEFT)
                if event.key == pygame.K_RIGHT:
                    self.rocket.change_speed(VELOCITY_FACTOR_RIGHT)
        return False

    def draw_screen(self, screen):
        self.all_sprites.update()
        self.meteor_hit_group = pygame.sprite.spritecollide(
            self.rocket, self.meteor_group, True)
        for m in self.meteor_hit_group:
            explotion = Explotion(m.rect.x, m.rect.y)
            self.rocket.kill()
            self.all_sprites.add(explotion)

        screen.blit(self.background, [0, 0])
        self.all_sprites.draw(screen)
        pygame.display.flip()
