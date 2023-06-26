import pygame
import mediapipe as mp
import cv2
import numpy as np
from utils import constants as cp


class FaceDetection:
    def __init__(self):
        # For video capture
        self.cap = cv2.VideoCapture(0)
        mp_face_mesh = mp.solutions.face_mesh

        self.face_mesh = mp_face_mesh.FaceMesh(
            max_num_faces=1,
            refine_landmarks=True,
            min_detection_confidence=0.5,
            min_tracking_confidence=0.5
        )

    def get_face_image(self):
        success, image = self.cap.read()
        if not success:
            print("Ignoring empty camera frame.")

        self.results = self.face_mesh.process(image)

        image.flags.writeable = True
        image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)

        frame = cv2.resize(image, (216, 144))
        frame = np.rot90(frame)
        return pygame.surfarray.make_surface(frame)

    def detect_movements(self, game_over):
        if self.results.multi_face_landmarks:
            for face_landmarks in self.results.multi_face_landmarks:
                if game_over and (face_landmarks.landmark[152].y - face_landmarks.landmark[10].y < 0.45):
                    return cp.DOWN
                if face_landmarks.landmark[10].x - face_landmarks.landmark[152].x > 0:
                    return cp.LEFT
                else:
                    return cp.RIGHT
