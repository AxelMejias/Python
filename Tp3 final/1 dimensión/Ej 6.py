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

lista_sin_repetidos = []

if len(lista_numeros) == 1:
    print(f"Solo se ingreso el valor : {lista_numeros[0]}")
else:
    for elemento in lista_numeros:
        if elemento not in lista_sin_repetidos:
            lista_sin_repetidos.append(elemento)
    print(f"La lista original es: {lista_numeros}")
    print(f"La lista sin duplicados seria: {lista_sin_repetidos}")
