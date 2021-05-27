from Tools.Shapes.base import Shape
from Tools.matrix import *
from Tools.Vector import *
from Tools.utils import *
from Tools.constants import *

class GridPlane(Shape):
    def __init__(self, resolution, cell_size = 400, position=Vector2(Width//2, Height//2)):
        super().__init__(position)
        self.resolution = resolution
        self.color = (140, 140, 140)
        self.cell_size = cell_size/50
        self.vertices = []
        #generate vertices
        for j in range(self.resolution):
            for i in range(self.resolution):
                x = translate(i, 0, self.resolution, -1, 1)
                y = translate(j, 0, self.resolution, -1, 1)
                self.vertices.append(Vector3( x * self.cell_size, y * self.cell_size, 1).toMatrix())

        self.edges = []
        #generate edges
        #horizontal connections
        for i in range(len(self.vertices)-1):
            if i % self.resolution != self.resolution - 1:
                self.edges.append( (i, i+1) )

        #vertical connections
        for i in range(len(self.vertices) - self.resolution):
            self.edges.append( (i, i+ self.resolution) )

    def Draw(self, camera, window, ShowPoints=True, ShowLines=True, ShowFaces=False):
        points = []
        PointPositions = []

        for index, vert in enumerate(self.vertices):
            transform = matrix_multiplication(self.transform, vert)
            #print(transform)
            transform = matrix_multiplication(camera.rotation[1], transform)
            transform = matrix_multiplication(camera.rotation[0], transform)

            transform[0][0] += camera.position.x
            transform[1][0] += camera.position.y
            z = 1 / (-camera.position.z - transform[2][0])

            p = projectionMatrix(z)
            t = matrix_multiplication(p, transform)

            x, y = t[0][0], t[1][0]
            x = int(x * camera.scale) + self.position.x
            y = int(y * camera.scale) + self.position.y

            points.append((x, y, z) )
            PointPositions.append( (transform[0][0], transform[1][0], z) )

        if ShowFaces == True:
            print("draw faces")
            #DrawFaces(window, points, self.faces, self.faceColors, self.face_list, camera, PointPositions)

        if ShowLines == True:
            DrawLines(window, points, self.edges, self.color)

        if ShowPoints == True:
            for x, y, z in points:
                pygame.draw.circle(window, (25, 42, 241), (x, y), 5)
