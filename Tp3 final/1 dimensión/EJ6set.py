#Escribe un programa que permita al usuario ingresar una lista de números y elimine los 
#elementos duplicados.

lista_numeros = []

while True:
    numero = input("Ingrese varios números y aprete 'Enter' para terminar: ")
    if numero == "":
        break
    try:
        lista_numeros.append(float(numero))
    except ValueError:
        print("Ingrese un dato válido")

conjunto = set(lista_numeros)

lista_sin_repetidos = list(conjunto)

print(f"Lista original: {lista_numeros}")

print(f"Lista sin elementos duplicados: {lista_sin_repetidos}")

#El problema que le encuentro al set es que cambia el orden de la lista, en cambio que con un for podemos hacer lo mismo sin modificar su orden
