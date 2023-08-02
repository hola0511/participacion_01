def obtener_numero_usuario(mensaje):
    while True:
        try:
            numero = float(input(mensaje))
            return numero
        except ValueError:
            print("Error: Ingresa un número válido.")

def suma(a, b):
    return a + b

def resta(a, b):
    return a - b

def multiplicacion(a, b):
    return a * b

def division(a, b):
    if b == 0:
        raise ValueError("No se puede dividir entre cero.")
    return a / b

def main():
    try:
        numero1 = obtener_numero_usuario("Ingresa el primer número: ")
        numero2 = obtener_numero_usuario("Ingresa el segundo número: ")

        resultado_suma = suma(numero1, numero2)
        resultado_resta = resta(numero1, numero2)
        resultado_multiplicacion = multiplicacion(numero1, numero2)
        resultado_division = division(numero1, numero2)

        print("Suma:", resultado_suma)
        print("Resta:", resultado_resta)
        print("Multiplicación:", resultado_multiplicacion)
        print("División:", resultado_division)

    except ValueError as error:
        print("Error:", error)

if __name__ == "__main__":
    main()