#Escribe un programa que permita al usuario ingresar una lista de números y eliminar 
#un elemento en un índice especificado. 

lista_numeros = []

while True:
    numero = input("Ingrese varios números y aprete 'Enter' para terminar: ")
    if numero == "":
        break
    try:
        lista_numeros.append(float(numero))
    except ValueError:
        print("Ingrese un dato válido")

try:
    indice = int(input("Ingresa el índice de la lista para borrar su elemento: "))
except ValueError:
    print("Ingrese un dato válido")
    exit()

print(f"Lista antes de eliminar el elemento: {lista_numeros}")

elemento_eliminado = lista_numeros.pop(indice)

print(f"Lista despues del elemento eliminado: {lista_numeros}")

print(f"Elemento eliminado: {elemento_eliminado}")

