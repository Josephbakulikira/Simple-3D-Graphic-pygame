from Tools.Vector import Vector3, Vector2
from Tools.matrix import *
import pygame

def rotationCam(val1, val2):
    return [ rotationX(val1), rotationY(val2) ]

class Camera:
    def __init__(self, position=Vector3(0, 0, 0), scale=600, distance=5):
        self.position = position
        self.scale = scale
        self.rotation = rotationCam(0, 0)
        self.r = Vector2(0, 0)
        self.distance = distance
        self.speed = 0.05
        self.zoomSpeed = 3
        self.transform = 0

    def HandleInput(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP] or keys[pygame.K_w]:
            self.position.y -= self.speed
        if keys[pygame.K_DOWN]or keys[pygame.K_s]:
            self.position.y += self.speed
        if keys[pygame.K_LEFT] or keys[pygame.K_a]:
            self.position.x -= self.speed
        if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
            self.position.x += self.speed

        if keys[pygame.K_KP_PLUS]:
            self.scale += self.zoomSpeed

        if keys[pygame.K_KP_MINUS]:
            self.scale -= self.zoomSpeed

    def HandleMouseEvent(self, x, y):
        self.r.x += y
        self.r.y += x
        self.rotation = rotationCam(self.r.x, self.r.y)
