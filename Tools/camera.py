from Tools.Vector import Vector3, Vector2
from Tools.matrix import *
import pygame

def rotationCam(val1, val2):
    return [ rotationX(val1), rotationY(val2) ]

class Camera:
    def __init__(self, position=Vector3(0, 0, -10), scale=600, distance=5):
        self.position = position
        self.rotation = rotationCam(0, 0)
        self.r = Vector2(0, 0)
        self.scale = scale
        self.distance = distance
        self.speed = 0.05
        self.zoomSpeed = 3
        self.transform = 0

    def HandleInput(self, wheel):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_UP] :
            self.position.y -= self.speed
        if keys[pygame.K_DOWN]:
            self.position.y += self.speed
        if keys[pygame.K_LEFT] or keys[pygame.K_a]:
            self.position.x -= self.speed
        if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
            self.position.x += self.speed

        if keys[pygame.K_q]:
            self.rotation -= self.speed
        if keys[pygame.K_e]:
            self.position.x += self.speed

        if keys[pygame.K_KP_PLUS] or keys[pygame.K_w]:
            self.scale += self.zoomSpeed

        if keys[pygame.K_KP_MINUS] or keys[pygame.K_s]:
            self.scale -= self.zoomSpeed

        if wheel["changed"] == True:
            if (self.position.z + wheel["value"] ) != -4:
                self.position.z += wheel["value"]
                #print(self.position.z)

    def HandleMouseEvent(self, x, y):
        self.r.x += y
        self.r.y += x
        self.rotation = rotationCam(self.r.x, self.r.y)

    def HandleMouseEvent2(self, x, y):
        self.position.x += x
        self.position.y += y
