#Escribe un programa que extraiga los elementos de la diagonal principal de una matriz 
#cuadrada.

def generar_matriz(fila, columna):
    matriz = []
    contador = 1

    for i in range(fila):
        fila = []
        for j in range(columna):
            fila.append(contador)
            contador += 1
        matriz.append(fila)

    return matriz

def introducir_datos():
    while True:
        try:
            fila = int(input("Introduce el número de filas: "))
            columna = int(input("Ingrese el mismo número de columnas que de filas: "))
            if fila != columna:
                raise ValueError("Introduce el mismo número en ambas para que sea una matriz cuadrada")
            matriz = generar_matriz(fila, columna)
            return matriz
        except ValueError as e:
            if str(e).startswith("invalid"):
                print("El tipo de dato no es válido. Por favor, introduce un número entero.")
            else:
                print(e)

def extraer_elementos(matriz):
    n = len(matriz)
        
    diagonal_principal = [matriz[i][i] for i in range(n)]

    return diagonal_principal

matriz = introducir_datos()

for fila in matriz:
    print(fila)

diagonal = extraer_elementos(matriz)
print(f"Los elementos de la diagonal principal son: {diagonal}")