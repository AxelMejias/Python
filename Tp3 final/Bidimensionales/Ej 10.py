#Una matriz es simétrica si es igual a su transpuesta. Escribe un programa que verifique 
#si una matriz es simétrica. 

matriz_simetrica = [
    [1, 2, 3],
    [2, 4, 5],
    [3, 5, 6],
]

#se puede verificar el funcionamiento del programa dado que la matriz de arriba si es simétrica y el programa
#arroja que si lo es, en cambio si reemplazamos los valores por los de abajo (una matriz no simetrica)
#el programa nos dira que es una matriz no simetrica

#matriz_simetrica =[
#    [1, 2, 3],
#    [4, 5, 6],
#    [7, 8, 9]
#]

def es_simetrica(matriz):
    n = len(matriz)
    m = len(matriz[0])

    if n != m:
        return False
    
    for i in range(n):
        for j in range(i + 1, n):
            if matriz[i][j] != matriz [j][i]:
                return False
            
    return True

for fila in matriz_simetrica:
    print(fila)

if es_simetrica(matriz_simetrica):
    print("La matriz es simétrica")
else:
    print("La matriz no es simétrica")