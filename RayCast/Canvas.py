# Создаем абстрактный класс отрисовки
import Map, Camera, CoPoVe


class Canvas:

    def __init__(self, map: Map, camera: Camera, coordsystem: CoPoVe.SystemCoords):
        self.map = map
        self.camera = camera
        self.coordsystem = coordsystem

    def draw(self, map: Map, camera: Camera):
        pass


class Console(Canvas):

    def __init__(self):
        pass

    def gradient(self, grad):
        self.grad = grad

    # Зависит от количества лучей. На сколько делить и в какой массив включать
    def gradient_draw(self, gradient):
        return gradient//10