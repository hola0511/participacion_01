lista = [1, 4, 7, 3, 21]

sumatoria = 0

for i in range(len(lista)):
    sumatoria = sumatoria + lista[0]
    del lista[0]

print(sumatoria)