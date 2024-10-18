#Escribe un programa que calcule la suma de todos los elementos en una lista 
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

filas = 6
columnas = 3
matriz = generar_matriz(filas, columnas)

for fila in matriz:
    print(fila)

suma_total = sum(sum(fila) for fila in matriz)
print(f"La suma de todos los elementos de la matriz es: {suma_total}")