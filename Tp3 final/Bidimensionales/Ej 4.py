#Escribe un programa que calcule la transpuesta de una matriz. La transpuesta de una 
#matriz intercambia sus filas por columnas. 

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

def transpuesta(matriz):
    fila = len(matriz)
    columnas = len(matriz[0])

    matriz_transpuesta = [[0] * filas for _ in range(columnas)]

    for i in range(filas):
        for j in range(columnas):
            matriz_transpuesta[j][i] = matriz [i][j]
    
    return matriz_transpuesta

filas = 3
columnas = 4
matriz = generar_matriz(filas, columnas)

print("La matriz original es: ")
for fila in matriz:
    print(fila)

matriz_transpuesta = transpuesta(matriz)

print("La matriz transpuesta es: ")
for fila in matriz_transpuesta:
    print(fila)