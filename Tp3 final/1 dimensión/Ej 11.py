#Escribe un programa que permita al usuario ingresar una lista y un número, y cuente 
#cuántas veces aparece ese número en la lista. 

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
    num_ocurrencia = float(input("Ingresa un número para saber cuantas veces se repite en la lista: "))
except ValueError:
    print("Ingrese un dato válido")
    exit()

ocurrencias = lista_numeros.count(num_ocurrencia)

print(f"Valores de la lista: {lista_numeros}")
print(f"El número {num_ocurrencia} aparece {ocurrencias} veces en la lista")