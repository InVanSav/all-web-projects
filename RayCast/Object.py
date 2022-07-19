# Задаем класс для объекта
from CoPoVe import*
import Ray


class Object:

    def __init__(self, pos, angle, parameters):
        self.pos = pos
        self.angle = angle
        self.parameters = parameters

    def position(self, pos: Point):
        self.pos = pos

    def rotation(self, angle: Angle):
        self.angle = angle
        self.parameters.rotate(angle)

    def contains(self, point):
        pass


class Parameters:

    def __init__(self):
        pass

    def rotate(self, angle):
        pass


class ParametersPlane(Parameters):

    def __init__(self, A, B, C, D):
        self.A = A
        self.B = B
        self.C = C
        self.D = D

    def rotate(self, angle):
        pass


class Plane(Object):

    def contains(self, point):
        p = self.parameters
        return p.A * point.x + p.B * point.y + p.C * point.z - p.D <= 10

    def intersect(self, ray: Ray):
        pass


class ParametersSphere(Parameters):

    def __init__(self, x_0, y_0, z_0, R):
        self.x_0 = x_0
        self.y_0 = y_0
        self.z_0 = z_0
        self.R = R


class Sphere(Object):

    def contains(self, point):
        l = (point.x - self.parameters.x_0)**2 + (point.y - self.parameters.y_0)**2 + (point.z - self.parameters.z_0)**2
        r = self.parameters.R**2

        return round(l, 3) == round(r, 3)


class ParametersEllipse(Parameters):

    def __init__(self, x_0, y_0, z_0, R, a, b, c):
        self.x_0 = x_0
        self.y_0 = y_0
        self.z_0 = z_0
        self.R = R
        self.a = a
        self.b = b
        self.c = c


class Ellipse(Object):

    def contains(self, point):
        l = (point.x - self.parameters.x_0)**2 / self.parameters.a**2 \
            + (point.y - self.parameters.y_0)**2 / self.parameters.b**2 \
            + (point.z - self.parameters.z_0)**2 / self.parameters.c**2
        r = self.parameters.R**2
        
        return l <= r


class ParametersWall(Parameters):

    def __init__(self, a, b, c, d, x_min, x_max, y_min, y_max, z_min, z_max):
        self.a = a
        self.b = b
        self.c = c
        self.d = d
        self.x_min = x_min
        self.x_max = x_max
        self.y_min = y_min
        self.y_max = y_max
        self.z_min = z_min
        self.z_max = z_max


class Wall(Object):

    def contains(self, point):
        if (point.x <= self.parameters.x_max and point.x >= self.parameters.x_min \
            and point.y <= self.parameters.y_max and point.y >= self.parameters.y_min and \
            point.z <= self.parameters.z_max and point.z >= self.parameters.z_min):
                p = self.parameters
                return p.A * point.x + p.B * point.y + p.C * point.z - p.D <= 0.1
        else:
            return False


# Создаем класс управления игроком
class FreeCamera:

    def __init__(self, camera: Camera, pos: Camera, look: Camera):
        self.camera = camera
        self.pos = pos
        self.look = look

    def strafe(self, point):
        pass

    def rotate(self, angle):
        pass


# Задаем класс игрока
class Player:

    def __init__(self, player_pos, player_angle, tile, speed):
        self.x, self.y = player_pos
        self.angle = player_angle
        self.tile = tile
        self.speed = speed

    @property
    def position(self):
        return self.x, self.y

    def movement(self):
        pass



