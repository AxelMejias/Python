#Escribe un programa que permita al usuario ingresar una lista de números y calcule el 
#promedio de los elementos. 

lista_numeros = []

while True:
    numero = input("Ingrese varios números y aprete 'Enter' para terminar: ")
    if numero == "":
        break
    try:
        lista_numeros.append(float(numero))
    except ValueError:
        print("Ingrese un dato válido")

#tambien puede usarse una estructura for para sumar los valores de la lista como antes visto

if lista_numeros:
    suma = sum(lista_numeros)

    cantidad = len(lista_numeros)

    promedio = suma / cantidad

    print(f"Los valores de la lista son: {lista_numeros} y su promedio es {promedio}")
else:
    print("La lista está vacía.")    