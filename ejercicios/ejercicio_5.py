def celcius(grados):
    return (grados - 32) * (5 / 9)

grados = eval(input("ingrese aqui la cantidad de grados fahrenheit: "))

print(celcius(grados))