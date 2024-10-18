#Modifica el programa anterior para que imprima la suma de cada fila de la lista 
#bidimensional. 

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

for i, fila in enumerate(matriz):
    suma_fila = sum(fila)
    print(f"La suma de la fila {i + 1} es: {suma_fila}")