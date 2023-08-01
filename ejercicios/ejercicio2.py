import math

def radio(area):
    return math.pi * (area ** 2)

area = eval(input("Introduzca el area de el circulo: "))

print(radio(area))