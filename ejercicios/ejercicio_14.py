def media_aritmetica(lista):
    if not lista:
        raise ValueError("La lista está vacía.")

    suma = sum(lista)
    cantidad_numeros = len(lista)
    media = suma / cantidad_numeros
    return media

lista_ejemplo = [10, 20, 30, 40, 50]

media_resultado = media_aritmetica(lista_ejemplo)

print("Lista:", lista_ejemplo)
print("Media aritmética:", media_resultado)