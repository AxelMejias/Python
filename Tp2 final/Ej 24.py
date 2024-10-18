# 24) Crea un programa que lea una cadena de texto carácter por carácter usandorecursión.


def imprimir_caracteres(cadena, indice=0):
    if indice < len(cadena):
        print(cadena[indice])
        imprimir_caracteres(cadena, indice + 1)

def main():
    cadena = input("Ingresá una cadena: ")
    imprimir_caracteres(cadena)

main()