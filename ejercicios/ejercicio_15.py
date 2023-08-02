def es_palindromo(cadena):
    cadena = cadena.lower()
    cadena = cadena.replace(" ", "")
    return cadena == cadena[::-1]

def main():
    entrada_usuario = input("Ingresa una cadena de texto: ")

    if es_palindromo(entrada_usuario):
        print("La cadena es un palíndromo.")
    else:
        print("La cadena no es un palíndromo.")

if __name__ == "__main__":
    main()