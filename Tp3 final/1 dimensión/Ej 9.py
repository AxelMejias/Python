#Escribe un programa que permita al usuario ingresar una lista de números y filtre los 
#números primos. 

def es_primo(numero):
    if numero <= 1:
        return False

    for i in range(2, int(numero**0.5) + 1):
        if numero % i == 0:
            return False

    return True

def ingresar_numeros ():
    lista_numeros = []
    while True:
        numero = input("Ingrese varios números y aprete 'Enter' para terminar: ")
        if numero == "":
            break
        try:
            lista_numeros.append(float(numero))
        except ValueError:
            print("Ingrese un dato válido")
    return lista_numeros

def main ():
    lista_numeros = ingresar_numeros()
    if lista_numeros:
        numeros_primos = [numero for numero in lista_numeros if es_primo(numero)]
        if numeros_primos:
            print(f"Números primos en la lista: {numeros_primos}")
        else:
            print("No hay números primos en la lista.")
    else:
        print("No se ingresaron números.")

if __name__ == "__main__":
    main()