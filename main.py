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
mx, my = 0, 0
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
        if event.type == pygame.MOUSEMOTION:
            if pygame.mouse.get_pressed()[0]:
                mx, my = event.rel
                mx = mx/sens
                my = my/sens
                #print(f"{mx}, {my}")
                cam.HandleMouseEvent(mx, my)
    cam.HandleInput()

    c.Draw(cam, window)

    pygame.display.flip()
    angle += 0.008
pygame.quit()
