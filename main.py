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
game_over = False

mp_face_mesh = mp.solutions.face_mesh
cap = cv2.VideoCapture(0)

with mp_face_mesh.FaceMesh(
        max_num_faces=1,
        refine_landmarks=True,
        min_detection_confidence=0.5,
        min_tracking_confidence=0.5) as face_mesh:
    while not game_over:
        game_over = game.process_events()
        game.draw_screen(screen)
        clock.tick(60)

        success, image = cap.read()
        if not success:
            print("Ignoring empty camera frame.")
            # If loading a video, use 'break' instead of 'continue'.
            continue
        image.flags.writeable = False
        image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        results = face_mesh.process(image)

        image.flags.writeable = True
        image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)

        if results.multi_face_landmarks:
            for face_landmarks in results.multi_face_landmarks:
                if face_landmarks.landmark[10].x - face_landmarks.landmark[152].x > 0:
                    event = pygame.event.Event(
                        pygame.KEYDOWN, key=pygame.K_LEFT)
                    pygame.event.post(event)
                    print("IZQUIERDA")
                else:
                    event = pygame.event.Event(
                        pygame.KEYDOWN, key=pygame.K_RIGHT)
                    pygame.event.post(event)
                    print("DERECHA")
        cv2.imshow('MediaPipe Face Mesh', cv2.flip(image, 1))
cap.release()
