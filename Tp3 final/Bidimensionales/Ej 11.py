def rotar_matriz_90_grados(matriz):
    # Transponer la matriz
    matriz_transpuesta = list(zip(*matriz))
    # Invertir cada fila de la matriz transpuesta
    matriz_rotada = [list(reversed(fila)) for fila in matriz_transpuesta]
    return matriz_rotada

# Ejemplo de uso
matriz = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print("Matriz original:")
for fila in matriz:
    print(fila)

matriz_rotada = rotar_matriz_90_grados(matriz)

print("\nMatriz rotada 90 grados:")
for fila in matriz_rotada:
    print(fila)
