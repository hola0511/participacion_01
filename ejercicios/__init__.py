class Punto:

    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y

    def mover(self, dx: int, dy: int):
        self.x += dx
        self.y += dy

    def calcular(self, punto: "Punto"):
        dx = self.x - punto.x
        dy = self.y - punto.y
        return (dx ** 2 + dy ** 2) ** 0.5

    def rotar(self):
        pass

    def __str__(self) -> str:
        return f"({self.x}, {self.y})"


class Rectangulo:

    def __init__(self, punto_01: Punto, punto_02: Punto):
        self.punto_01: Punto = punto_01
        self.punto_02: Punto = punto_02

    def area(self) -> float:
        pass

##otro documento

from ejercicio_01 import Punto


p_1: Punto = Punto(2, 3)
print(p_1)

p_2: Punto = Punto(-5, 6)
print(p_2)

print(p_1.calcular(p_2))

