def factorial(numero):
    if numero < 0:
        raise ValueError("El número debe ser no negativo.")
    else:
        resultado = 1
        for i in range(1, numero + 1):
            resultado *= i
        return resultado

numero = eval(input("ingresde aqui el numero a factoriar: "))

resultado_factorial = factorial(numero)

print("El factorial de ", numero, " es: ", resultado_factorial)