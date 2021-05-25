from Tools.Vector import Vector3

import pygame

class Camera:
    def __init__(self, position=Vector3(0, 0, 0), scale=600, distance=5):
        self.position = position
        self.scale = scale
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
