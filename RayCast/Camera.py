# Задаем класс для камеры
import CoPoVe
import Map


class Camera:

    def __init__(self, position, look, gfov, vfov, distance):        # Создание камеры
        self.pos = position                                          # Задание позиции
        self.look_at = look                                          # Угол обзора камеры
        self.gfov = gfov                                             # Ширина обзора камеры по горизонтали
        self.vfov = vfov                                             # Ширина обзора камеры по вертикали
        self.draw_distance = distance                                # Определяем длину прорисовки

    def intersect(self):
        pass

    def sendrays(self, map: Map):
        pass
