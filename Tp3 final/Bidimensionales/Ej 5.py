#Escribe un programa que encuentre el valor más grande en una lista bidimensional.

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

def maximo_elemento(matriz):
    maximo = matriz [0][0]
    for fila in matriz:
        for elemento in fila:
            if elemento > maximo:
                maximo = elemento
    return maximo

maximo = maximo_elemento(matriz)

print(f"El maximo elemento de la matriz es {maximo}")