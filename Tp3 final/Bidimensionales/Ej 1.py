#Crea una función que reciba dos parámetros: el número de filas y columnas. La función 
#debe generar una matriz de ese tamaño, donde los valores son números enteros 
#consecutivos empezando desde 1.

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

filas = int(input("Ingresa el número de filas: "))
columnas = int(input("Ingresa el número de columnas: "))
matriz = generar_matriz(filas, columnas)

for fila in matriz:
    print(fila)