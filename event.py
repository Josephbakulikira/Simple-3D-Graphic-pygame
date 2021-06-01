import pygame
from Tools.constants import *

def GetEvent(mx, my, wheel, camera):
    run = True
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                run = False
        if event.type == pygame.MOUSEMOTION:
            if pygame.mouse.get_pressed()[2]:
                mx, my = event.rel
                mx = mx/sens
                my = my/sens
                #print(f"{mx}, {my}")
                camera.HandleMouseEvent(mx, my)
            if pygame.mouse.get_pressed()[1]:
                x, y = event.rel
                x = x/sens
                y = y/sens
                camera.HandleMouseEvent2(x, y)
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 4:
                # mouse wheel input up
                wheel["changed"]=True
                wheel["value"] = 1
                #print("up")
            if event.button == 5:
                # mouse wheel input down
                wheel["changed"]=True
                wheel["value"] = -1
                #print("Down")
    return run
