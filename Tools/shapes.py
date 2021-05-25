import pygame
from Tools.utils import *
from Tools.matrix import *
from Tools.Vector import *
from Tools.constants import Width, Height

class Shape:
    def __init__(self, position):
        self.position = position
        self.transform = [[1, 0, 0], [0, 1, 0], [0, 0, 1]]
class Cube(Shape):
    def __init__(self, position=Vector2(Width//2, Height//2)):
        super().__init__(position)
        self.vertices = [
                         Vector3( 1,  1,  1).toMatrix(),
                         Vector3( 1,  1, -1).toMatrix(),
                         Vector3( 1, -1,  1).toMatrix(),
                         Vector3( 1, -1, -1).toMatrix(),
                         Vector3(-1, -1, -1).toMatrix(),
                         Vector3(-1,  1, -1).toMatrix(),
                         Vector3(-1,  1,  1).toMatrix(),
                         Vector3(-1, -1,  1).toMatrix()
                        ]
        self.edges = [(0, 1), (0, 2), (0, 6),
                     (1, 3), (1, 5), (2, 7),
                     (2, 3), (4, 7), (4, 3),
                     (4, 5), (5, 6), (6, 7)
                     ]
        self.faces = [ (0, 1, 3, 2), (2, 3, 4, 7), (0, 1, 5, 6), (0, 2, 7, 6), (6, 7, 4, 5), (1, 3, 4, 5) ]
        #front, back
        #self.faces = [(0, 2, 7, 6),(1, 3, 4, 5) ]

        self.faceColors = [(0, 0,0 ), (255,238,173), (255,111,105), (255,204,92), (40,54,85), (75,56,50)]
        #self.faceColors = [(255, 0,0 ), (0, 255, 0), (0, 0, 255), (255,255,0), (0, 255, 255), (255, 0, 255)]

        self.face_list = dict(zip(self.faces, self.faceColors) )
        print(self.face_list)

    def Draw(self, camera, window, ShowPoints=False, ShowLines=False, ShowFaces=True):
        points = []
        PointPositions = []
        for index, vert in enumerate(self.vertices):
            transform = matrix_multiplication(self.transform, vert)
            transform[0][0] += camera.position.x
            transform[1][0] += camera.position.y
            z = 1 / (camera.distance - transform[2][0])

            p = projectionMatrix(z)
            t = matrix_multiplication(p, transform)

            x, y = t[0][0], t[1][0]
            x = int(x * camera.scale) + self.position.x
            y = int(y * camera.scale) + self.position.y

            points.append((x, y, z) )
            PointPositions.append( (transform[0][0], transform[1][0], z) )

        if ShowFaces == True:
            DrawFaces(window, points, self.faces, self.faceColors, self.face_list, camera, PointPositions)

        if ShowLines == True:
            DrawLines(window, points, self.edges)

        if ShowPoints == True:
            for x, y, z in points:
                pygame.draw.circle(window, (25, 42, 241), (x, y), 5)
