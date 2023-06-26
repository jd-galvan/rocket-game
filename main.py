import mediapipe as mp
import cv2
import pygame
from classes.game import Game

pygame.init()
clock = pygame.time.Clock()

SCREEN_WIDTH = 720
SCREEN_HEIGHT = 720
screen = pygame.display.set_mode([SCREEN_WIDTH, SCREEN_HEIGHT])

game = Game()
kill = False

mp_face_mesh = mp.solutions.face_mesh
cap = cv2.VideoCapture(0)

face_mesh = mp_face_mesh.FaceMesh(
    max_num_faces=1,
    refine_landmarks=True,
    min_detection_confidence=0.5,
    min_tracking_confidence=0.5
)

while not kill:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            kill = True

    game.draw_screen(screen)
    clock.tick(60)
# cap.release()
pygame.quit()
