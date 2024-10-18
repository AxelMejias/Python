#Escribe un programa que permita al usuario ingresar una lista de números y calcule la 
#suma de todos los elementos en la lista.

lista_numeros = []

while True:
    numero = input("Ingrese varios números y aprete 'Enter' para terminar: ")
    if numero == "":
        break
    try:
        lista_numeros.append(float(numero))
    except ValueError:
        print("Ingrese un dato válido")

if len(lista_numeros) == 1:
    print(f"Solo se ingreso el valor : {lista_numeros[0]}")
elif lista_numeros:
    suma = 0
    for numero in lista_numeros:
        suma += numero
    print(f"La suma de los números de la lista es: {suma}")
else:
    print("No se ingreso ningún valor")