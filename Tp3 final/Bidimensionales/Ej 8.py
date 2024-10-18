#Crea un programa que genere una matriz identidad de tamaño n. Una matriz identidad 
#es una matriz cuadrada donde los elementos de la diagonal principal son 1 y el resto 
#son 0. 

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

identidad = [[1 if i == j else 0 for j in range(n)] for i in range(n)] 
for fila in identidad: 
    print(fila)