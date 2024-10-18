def convertir_cadena(cadena, opcion):
    
    if opcion == 'Mayus':
        return cadena.upper()
    elif opcion == 'Minus':
        return cadena.lower()
    else:
        return cadena
def main():

    cadena = input("Ingrese una cadena: ")

    opcion = input("¿Desea convertir la cadena a mayúsculas o minúsculas? (Mayus/Minus): ")

    cadena_convertida = convertir_cadena(cadena, opcion)

    print(f"Cadena convertida: {cadena_convertida}")
if __name__ == "__main__":
    main()