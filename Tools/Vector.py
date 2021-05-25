from math import sqrt, atan2
import pygame


class Vector2:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y
        self.color = (255,255,255)

    def __mul__(a, b):
        x,y = 0, 0
        if type(b) == Vector2:
            x = a.x * b.x
            y = a.y * b.y
        else:
            x = a.x * b
            y = a.x * b
        return Vector2(x, y)

    def __add__(a, b):
        x,y = 0, 0
        if type(b) == Vector2:
            x = a.x + b.x
            y = a.y + b.y
        else:
            x = a.x + b
            y = a.x + b
        return Vector2(x, y)

    def __sub__(a, b):
        x,y = 0, 0
        if type(b) == Vector2:
            x = a.x - b.x
            y = a.y - b.y
        else:
            x = a.x - b
            y = a.x - b
        return Vector2(x, y)

    def __truediv__(a, b):
        x,y = 0, 0
        if type(b) == Vector2:
            x = a.x / b.x
            y = a.y / b.y
        else:
            x = a.x / b
            y = a.x / b
        return Vector2(x, y)

    def parsetoInt(vec):
        return Vector2(int(vec.x), int(vec.y))

    def getMagnitude(vec):
        return sqrt(vec.x * vec.x + vec.y * vec.y)

    def Normalize(vec):
        mag = Vector2.getMagnitude(vec)
        if mag != 0:
            return Vector2(vec.x/mag, vec.y/mag)
        return Vector2(1, 1)

    def heading(vec):
        angle = atan2(vec.y, vec.x)
        #in radians
        return angle

    def limit(vec, max_length):
        squared_mag = self.magnitude() * self.magnitude()
        if squared_mag > (max_length * max_length):
            vec.x = vec.x/sqrt(squared_mag)
            vec.y = vec.y/sqrt(squared_mag)
            vec.x = vec.x * max_length
            vec.y = vec.y * max_length
    def __repr__(self):
        return f'2DVector-> x:{self.x}, y:{self.y}'

class Vector3:
    def __init__(self, x=0, y=0, z=0):
        self.x = x
        self.y = y
        self.z = z
        self.color = (255,255,255)

    def __mul__(a, b):
        x,y,z = 0, 0, 0
        if type(b) == Vector3:
            x = a.x * b.x
            y = a.y * b.y
            z = a.z * b.z
        else:
            x = a.x * b
            y = a.y * b
            z = a.z * b
        return Vector3(x, y, z)

    def __add__(a, b):
        x,y,z = 0, 0, 0
        if type(b) == Vector3:
            x = a.x + b.x
            y = a.y + b.y
            z = a.z + b.z
        else:
            x = a.x + b
            y = a.y + b
            z = a.z + b
        return Vector3(x, y, z)

    def __sub__(a, b):
        x,y,z = 0, 0, 0
        if type(b) == Vector3:
            x = a.x - b.x
            y = a.y - b.y
            z = a.z - b.z
        else:
            x = a.x - b
            y = a.y - b
            z = a.z - b
        return Vector3(x, y, z)

    def __truediv__(a, b):
        x,y,z = 0, 0, 0
        if type(b) == Vector3:
            x = a.x / b.x
            y = a.y / b.y
            z = a.z / b.z
        else:
            x = a.x / b
            y = a.y / b
            z = a.z / b
        return Vector3(x, y, z)

    def parsetoInt(vec):
        return Vector3(int(vec.x), int(vec.y), int(vec.z))

    def getMagnitude(vec):
        return sqrt(vec.x * vec.x + vec.y * vec.y + vec.z * vec.z)

    def Normalize(vec):
        mag = Vector3.getMagnitude(vec)
        if mag != 0:
            return Vector3(vec.x/mag, vec.y/mag, vec.z/mag)
        return Vector3(1, 1, 1)

    def toMatrix(self):
        return [[self.x], [self.y], [self.z]]

    # def heading(vec):
    #     angle = math.atan2(vec.y, vec.x)
    #     #in radians
    #     return angle

    def limit(vec, max_length):
        squared_mag = self.magnitude() * self.magnitude()
        if squared_mag > (max_length * max_length):
            vec.x = vec.x/sqrt(squared_mag)
            vec.y = vec.y/sqrt(squared_mag)
            vec.z = vec.z/sqrt(squared_mag)
            vec.x = vec.x * max_length
            vec.y = vec.y * max_length
            vec.z = vec.z * max_length
    def __repr__(self):
        return f'3DVector-> x:{self.x}, y:{self.y}, z:{self.z}'
