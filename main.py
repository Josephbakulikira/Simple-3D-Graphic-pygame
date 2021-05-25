import pygame

from Tools.matrix import *
from Tools.shapes import *
from Tools.Vector import *
from Tools.utils import *
from Tools.constants import *
from Tools.camera import Camera

window = pygame.display.set_mode(Resolution)

clock = pygame.time.Clock()
fps = 60

cam = Camera()
angle = 0
c = Cube()

run = True
while run:
    clock.tick(fps)
    window.fill(BackgroundColor)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                run = False
    cam.HandleInput()

    c.transform = matrix_multiplication(matrix_multiplication(rotationY(angle), rotationX(angle)), rotationZ(angle) )

    c.Draw(cam, window)

    pygame.display.flip()
    angle += 0.008
pygame.quit()
