import pygame
import math
import event
from Tools.matrix import *
from Tools.Shapes.cube import Cube
from Tools.Shapes.grid import GridPlane
from Tools.Vector import *
from Tools.utils import *
from Tools.constants import *
from Tools.camera import Camera


window = pygame.display.set_mode(Resolution)
#hide mouse
pygame.mouse.get_rel()
pygame.mouse.set_visible(False)
a = pygame.event.set_grab(True)
clock = pygame.time.Clock()
fps = 60

mx, my = 0, 0
m_wheel = { "changed" :False, "value" :0}

cam = Camera()
angle = 0

gridPlane = GridPlane(30)
gridPlane.color = (255, 255, 255)
gridPlane.transform = rotationX(-math.pi/2)
c = Cube()

run = True
while run:
    clock.tick(fps)
    window.fill(BackgroundColor)

    #pygame.draw.rect(window, (50, 20, 120), pygame.Rect(300, 400, 200, 500))

    #get events
    run = event.GetEvent(mx, my, m_wheel, cam)
    cam.HandleInput(m_wheel)


    gridPlane.Draw(cam, window, False)
    c.Draw(cam, window)

    #angle += 0.005
    m_wheel["changed"] = False
    pygame.display.flip()
pygame.quit()
