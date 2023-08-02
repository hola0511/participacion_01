def encontrar_mayor(lista):
    if len(lista) == 0:
        print("La lista está vacía.")
        return None

    maximo = max(lista)
    return maximo
def encontrar_menor(lista):
    if len(lista) == 0:
        print("La lista está vacía.")
        return None

    minimo = min(lista)
    return minimo

lista = [34, 12, 56, 78, 23, 9, 45]

minimo =encontrar_menor(lista)
maximo = encontrar_mayor(lista)

if maximo is not None and minimo is not None:
    print("El numero más grande:", maximo)
    print("El numero más pequeño:", minimo)