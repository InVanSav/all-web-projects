from Object import*
import math
import Camera


# Задаем класс для системы координат
class SystemCoords:

    def __init__(self, point_for_start, k):
        self.start_point = point_for_start  # Задаем точку начала координат
        self.k = k                          # Единичный вектор


# Задаем класс для точки
class Point:

    def __init__(self, x, y, z):            # Создаем точку с координатами x, y, z
        self.x = x
        self.y = y
        self.z = z

    def __truediv__(self, digit):
        return self.multiplication(1/digit)

    def __mul__(self, digit):
        return self.multiplication(digit)

    def __sub__(self, point):
        return self.addition(point.multiplication(-1))

    def __add__(self, point):
        return self.addition(point)

    def addition(self, point):
        return Point(self.x + point.x, self.y + point.y, self.z + point.z)

    def multiplication(self, j):
        return Point(self.x*j, self.y*j, self.z*j)

    def distance(self, point_2):
        dx = self.x-point_2.x
        dy = self.y-point_2.y
        dz = self.z-point_2.z
        return (dx**2 + dy**2 + dz**2)**(1/2)

    def print_p(self):
        print(self.x, self.y, self.z)


# Создаем класс угла поворота
class Angle(Point):

    def normalize(self):
        self.x %= 2*math.pi
        self.y %= 2*math.pi
        self.z %= 2*math.pi

    def addition(self, angle):
        ang = Angle(self.x + angle.x, self.y + angle.y, self.z + angle.z)
        ang.normalize()
        return ang

    def multiplication(self, j):
        ang = Angle(self.x*j, self.y*j, self.z*j)
        ang.normalize()
        return ang


# Задаем класс для векторов
class Vector(Point):

    def __pow__(self, vector):                                            # Скалярное произведение
        return self.scalar_prod(vector)

    def __xor__(self, vector):                                             # Векторное произведение
        return self.cross_prod(vector)

    def __len__(self):
        return self.len()

    def addition(self, vector):
        return Vector(self.x + vector.x, self.y + vector.y, self.z + vector.z)

    def scalar_prod(self, vector):
        return self.x * vector.x + self.y * vector.y + self.z * vector.z

    def cross_prod(self, vector):
        x = self.y * vector.z - self.z * vector.y
        y = self.z * vector.x - self.x * vector.z
        z = self.x * vector.y - self.y * vector.x
        return Vector(x, y, z)

    def len(self):
        return (self.x**2 + self.y**2 + self.z**2)**0.5

    def multiplication(self, j):
        return Vector(self.x*j, self.y*j, self.z*j)

    def print_v(self):
        print(self.x, self.y, self.z)


# Класс исключительно для личных целей
class Pygame:

    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.num_rays_vert = height//10
        self.num_rays_gor = width//10
        self.half_width = width//2
        self.half_height = height//2


# Цвета отдельно для меня (красота)
black = (0, 0, 0)
red = (255, 0, 0)
white = (255, 255, 255)
darkgray = (110, 110, 110)

