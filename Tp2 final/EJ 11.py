# 11- Pedir dos palabras por teclado, indicar si son iguales.

palabra1 = input("Ingrese la palabra 1: ")
palabra2 = input("Ingrese la palabra 2: ")

if palabra1 == palabra2:
    print("Es la misma palabra.")
else:
    print(palabra1.capitalize(), "no es lo mismo que", palabra2 + ".")