#Escribe un programa que sume dos listas de números elemento por elemento. Las 
#listas deben tener la misma longitud. 

def sumar_listas(lista1, lista2):
    resultado = [a + b for a, b in zip(lista1, lista2)]

    return resultado

def ingresar_dato(mensaje):
    lista = []
    while True:
        numero = input(mensaje)
        if numero == "":
            break
        try:
            lista.append(float(numero))
        except ValueError:
            print("Ingrese un dato válido")
    return lista

def main():
    lista1 = ingresar_dato("Ingrese los valores de la primera lista y aprete 'Enter' para terminar: ")
    lista2 = ingresar_dato("Ingrese la misma cantidad de valores de la segunda lista y aprete 'Enter' para terminar: ")

    if len(lista1) != len(lista2):
        print("Las listas deben tener la misma cantidad de datos")
        return

    resultado = sumar_listas(lista1, lista2)

    print(f"Lista 1: {lista1}")

    print(f"Lista 2: {lista2}")

    print(f"Resultado de la suma: {resultado}")

if __name__ == "__main__":
    main()