import CoPoVe as pov


# Создаем класс кватернионов
class Quaternion:

    def __init__(self, real: float, imag: pov.Vector(float, float, float)):
        self.real = real
        self.imag = imag

    @staticmethod
    def from_values(a: float = 0, b: float = 0, c: float = 0, d: float = 0):
        return Quaternion(a, pov.Vector(b, c, d))

    def is_imag_zero(self, b: bool = True, c: bool = True, d: bool = True) -> bool:
        b1 = self.imag.x == 0 or not b
        b2 = self.imag.y == 0 or not c
        b3 = self.imag.z == 0 or not d

        return b1 and b2 and b3

    def sum(self, number: 'Quaternion') -> 'Quaternion':
        if isinstance(number, (int, float)):
            return Quaternion(self.real + number, self.imag)

        elif isinstance(number, complex):
            imag = pov.Vector(number.imag, 0, 0)
            return Quaternion(self.real + number.real, self.imag + imag)

        elif isinstance(number, Quaternion):
            return Quaternion(self.real + number.real, self.imag + number.imag)

    def multiply_by_quaternion(self, number: 'Quaternion') -> 'Quaternion':
        real = self.real * number.real - self.imag * number.imag
        imag = self.real * number.imag + number.real * self.imag + self.imag ** number.imag
        return Quaternion(real, imag)

    def multiply(self, number: [int, float, complex, 'Quaternion']) -> 'Quaternion':
        if isinstance(number, (int, float)):
            return Quaternion(self.real * number, self.imag * number)

        elif isinstance(number, complex):
            return self.multiply_by_quaternion(
                Quaternion(number.real, pov.Vector(number.imag, 0, 0))
            )

        elif isinstance(number, Quaternion):
            return self.multiply_by_quaternion(number)

    def len(self) -> float:
        return (self.real ** 2 + self.imag.len() ** 2) ** (1 / 2)

    @property
    def conjugate(self) -> 'Quaternion':
        return Quaternion(self.real, -self.imag)

    def inverse(self) -> 'Quaternion':
        return (self.conjugate) / (self.len() ** 2)

    def __compare_equality__(self, value: [int, float, complex, 'Quaternion']) -> bool:
        if isinstance(value, (int, float)):
            return self.real == value and self.is_imag_zero()
        elif isinstance(value, complex):
            return self.real == value.real and self.imag.x == value.imag and self.is_imag_zero(False)
        elif isinstance(value, Quaternion):
            return self.real == value.real and self.imag == value.imag

    def __add__(self, number: 'Quaternion') -> 'Quaternion':
        return self.sum(number)

    def __radd__(self, number: 'Quaternion') -> 'Quaternion':
        return self.sum(number)

    def __mul__(self, number: 'Quaternion') -> 'Quaternion':
        return self.multiply(number)

    def __rmul__(self, number: 'Quaternion') -> 'Quaternion':
        if isinstance(number, Quaternion):
            return number.multiply(self)
        else:
            return self * number

    def __sub__(self, number: 'Quaternion') -> 'Quaternion':
        return self.sum(-number)

    def __rsub__(self, number: 'Quaternion') -> 'Quaternion':
        return -self.sum(number)

    def __neg__(self) -> 'Quaternion':
        return Quaternion(-self.real, -self.imag)

    def __truediv__(self, number: 'Quaternion') -> 'Quaternion':
        if isinstance(number, Quaternion):
            return self * number.inverse()
        else:
            return self * (1 / number)

    def __rtruediv__(self, number: 'Quaternion') -> 'Quaternion':
        return number * self.inverse()

    def __eq__(self, number: 'Quaternion') -> bool:
        return self.__compare_equality__(number)

    def __ne__(self, number: 'Quaternion') -> bool:
        return not self.__compare_equality__(number)
