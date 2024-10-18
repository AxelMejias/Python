import random

def solicitar_tamano():
    while True:
        filas = int(input("Ingrese el número de filas (mínimo 3): "))
        columnas = int(input("Ingrese el número de columnas (mínimo 2): "))
        if filas >= 3 and columnas >= 2:
            return filas, columnas
        else:
            print("Los valores ingresados no son válidos. Intente nuevamente.")

def cargar_datos_manual(filas, columnas):
    lista = []
    for i in range(filas):
        fila = []
        for j in range(columnas):
            while True:
                try:
                    valor = float(input(f"Ingrese el valor para la posición [{i}][{j}]: "))
                    if 1 <= valor <= 999:
                        fila.append(valor)
                        break
                    else:
                        print("El valor debe estar en el rango de 1 a 999. Intente nuevamente.")
                except ValueError:
                    print("Entrada inválida. Por favor, ingrese un número decimal.")
        lista.append(fila)
    return lista

def cargar_datos_aleatorio(filas, columnas):
    lista = []
    for i in range(filas):
        fila = []
        for j in range(columnas):
            valor = random.uniform(1, 999)
            fila.append(valor)
        lista.append(fila)
    return lista

def mostrar_datos(lista):
    for fila in lista:
        print(end="")
        for valor in fila:
            print(f"[{valor:.2f}]", end=" ")
        print("")

def generar_sumatoria(lista):
    sumatoria = []
    for fila in lista:
        suma_fila = 0
        for valor in fila:
            suma_fila += valor
        sumatoria.append([suma_fila])
    return sumatoria

def mostrar_sumatoria(sumatoria):
    for fila in sumatoria:
        print(end="")
        for valor in fila:
            print(f"[{valor:.2f}]", end=" ")
        print("")

def generar_lista_ordenada(sumatoria):
    lista_ordenada = []
    for i, fila in enumerate(sumatoria):
        lista_ordenada.append([fila[0], i])

    # Ordenar la lista de mayor a menor basado en la primera columna
    for i in range(len(lista_ordenada)):
        for j in range(i + 1, len(lista_ordenada)):
            if lista_ordenada[i][0] < lista_ordenada[j][0]:
                lista_ordenada[i], lista_ordenada[j] = lista_ordenada[j], lista_ordenada[i]

    return lista_ordenada

def mostrar_lista_ordenada(lista_ordenada):
    print("\nLista ordenada de mayor a menor con índices originales:")
    for fila in lista_ordenada:
        print(end="")
        for valor in fila:
            print(f"[{valor:.2f}]", end=" ")
        print("")

def sumar_columna_1(lista_ordenada):
    suma = 0
    for fila in lista_ordenada:
        suma += fila[0]
    return suma

def main():
    filas, columnas = solicitar_tamano()

    while True:
        opcion = input("¿Desea cargar los datos manualmente (M) o de manera aleatoria (A)? ").upper()
        if opcion == 'M':
            lista = cargar_datos_manual(filas, columnas)
            break
        elif opcion == 'A':
            lista = cargar_datos_aleatorio(filas, columnas)
            break
        else:
            print("Opción inválida. Por favor, ingrese 'M' para manual o 'A' para aleatorio.")

    print("\nDatos cargados:")
    mostrar_datos(lista)

    sumatoria = generar_sumatoria(lista)
    print("\nSumatoria de cada fila:")
    mostrar_sumatoria(sumatoria)

    lista_ordenada = generar_lista_ordenada(sumatoria)
    mostrar_lista_ordenada(lista_ordenada)

    suma_columna_1 = sumar_columna_1(lista_ordenada)
    print(f"\nSumatoria de la columna 1 de la lista ordenada: [{suma_columna_1:.2f}]")

if __name__ == "__main__":
    main()
