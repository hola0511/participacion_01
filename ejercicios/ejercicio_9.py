import random

m = 4
n = 5

matriz = [[random.randint(1, 100) for i in range(m)] for j in range(n)]

for fila in matriz:
    for elemento in fila:
        print(elemento, end=" ")
    print()
