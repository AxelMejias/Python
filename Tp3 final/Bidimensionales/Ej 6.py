#Escribe un programa que multiplique cada elemento de una lista bidimensional por un 
#valor escalar dado por el usuario. 

import numpy as np

def generar_matriz(filas, columnas):
    matriz = []
    contador = 1

    for i in range(filas):
        fila = []
        for j in range(columnas):
            fila.append(contador)
            contador += 1
        matriz.append(fila)

    return matriz

filas = 3
columnas = 4
matriz = generar_matriz(filas, columnas)

for fila in matriz:
    print(fila)

multiplicador = int(input("Ingrese un número que multiplicara cada elemento de la matriz vista: "))

def valor_multiplicado(matriz, multiplicador):
    nueva_matriz = []
    for fila in matriz:
        nueva_fila = []
        for elemento in fila:
            nueva_fila.append(elemento * multiplicador)
        nueva_matriz.append(nueva_fila)

    return nueva_matriz

nueva_matriz = valor_multiplicado(matriz, multiplicador)

print("La nueva matriz es")
for fila in nueva_matriz:
    print(fila)