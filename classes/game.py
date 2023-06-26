from .rocket import Rocket
from .meteor import Meteor
from .explotion import Explotion
import pygame
import random
from .face import FaceDetection
from utils import constants as c

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

SCREEN_WIDTH = 720
SCREEN_HEIGHT = 720

VELOCITY_FACTORS = {
    c.LEFT: -5,
    c.RIGHT: 5
}

BANNER_GO_HEIGHT = 200
BANNER_GO_WIDTH = SCREEN_WIDTH


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

        self.face_detection = FaceDetection()

        self.game_over = False
        self.game_over_text = pygame.font.SysFont("serif", 25).render(
            "Game Over. Asiente con la cabeza para volver a jugar...", True, WHITE)

    def draw_screen(self, screen):
        self.all_sprites.update()
        self.meteor_hit_group = pygame.sprite.spritecollide(
            self.rocket, self.meteor_group, True)
        for m in self.meteor_hit_group:
            explotion = Explotion(m.rect.x, m.rect.y)
            self.all_sprites.remove(self.rocket)
            self.rocket.kill()
            self.all_sprites.add(explotion)
            self.game_over = True

        screen.blit(self.background, [0, 0])
        self.all_sprites.draw(screen)

        frame = self.face_detection.get_face_image()
        screen.blit(frame, (0, 0))
        face_movement_direction = self.face_detection.detect_movements(
            self.game_over)
        if face_movement_direction != None and face_movement_direction != c.DOWN:
            self.rocket.change_speed(VELOCITY_FACTORS[face_movement_direction])

        if self.game_over:
            pygame.draw.rect(
                screen, BLACK, (0, (SCREEN_HEIGHT // 2 - BANNER_GO_HEIGHT // 2), BANNER_GO_WIDTH, BANNER_GO_HEIGHT))
            screen.blit(self.game_over_text, [
                        (SCREEN_WIDTH // 2 - self.game_over_text.get_width() // 2),
                        (SCREEN_HEIGHT // 2)])
            if face_movement_direction == c.DOWN:
                self.__init__()

        pygame.display.flip()
