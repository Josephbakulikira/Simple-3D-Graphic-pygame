import colorsys
from Tools.Vector import *
from math import pow, sqrt
import pygame

def translate(value, min1, max1, min2, max2):
    return min2 + (max2 - min2)* ((value-min1)/(max1-min1))

def hsv_to_rgb(h, s, v):
    return tuple(round(i * 255) for i in colorsys.hsv_to_rgb(h, s, v))

def getDistance3D(v1, v2):
    return sqrt( pow((v1.x - v2.x), 2) + pow((v1.y - v2.y), 2) + pow((v1.z - v2.z), 2))

def getDistance2D(v1, v2):
    return sqrt((v2.x - v1.x)*(v2.x - v1.x) + (v2.y -v1.y)*(v2.y - v1.y))

def connect_point(i, j, points,window, color, thickness):
    a = points[i]
    b = points[j]
    pygame.draw.line(window, color, (a[0], a[1]), (b[0], b[1]), thickness)

def DrawLines(window, points, edges, color=(0, 0, 0), thickness=2):
    for i, j in edges:
        connect_point(i, j, points, window, color, thickness)


def DrawPolygons(window, x, y, z, w, points, color):
    a = points[x]
    b = points[y]
    c = points[z]
    d = points[w]
    polygons= (a[0], a[1]), (b[0], b[1]), (c[0], c[1]), (d[0], d[1])
    pygame.draw.polygon(window, color, polygons)

def lastIndex(k):
    return k[-1]

def Zsort(faces):
    return sorted(faces, key=lastIndex)

def DrawFaces(window, points, faces, colors, face_list, cam, indices):
    o = cam.position.z
    face_sort = []
    for face in faces:
        front = False
        dist = 0
        for i in face:
            dist += getDistance3D( cam.position, Vector3(indices[i][0], indices[i][1], indices[i][2]) )
        z = dist/4
        #print(z)

        face_sort.append([face[0], face[1], face[2], face[3], z])
    face_sort = Zsort(face_sort)
    for i, face in enumerate(face_sort):

        DrawPolygons(window, face[0], face[1], face[2], face[3], points, face_list[(face[0], face[1], face[2], face[3])])
