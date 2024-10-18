#Crea un programa que genere una matriz identidad inversa de tamaño n. Una matriz 
#identidad inversa es una matriz cuadrada donde los elementos de la diagonal inversa 
#principal son 1 y el resto son 0. 

def ingresar_tamaño():
    while True:
        try:
            n = int(input("Ingrese el tamaño de la matriz identidad: "))
            if n <= 1:
                raise ValueError ("El número debe ser mayor a 1")
            return n
        except ValueError as e:
            if str(e).startswith("invalid"):
                print("El tipo de dato no es válido. Por favor, introduce un número entero.")
            else:
                print(e)

n = ingresar_tamaño()

def matriz_identidad_inversa(n):
    matriz = [[0 for _ in range(n)] for _ in range(n)]

    for i in range(n):
        matriz[i][n - 1 - i] = 1

    return matriz

matriz_identidad_inversa = matriz_identidad_inversa(n)

for fila in matriz_identidad_inversa:
    print(fila)