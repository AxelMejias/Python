#Escribe un programa que permita al usuario ingresar una lista y la invierta. 

lista_numeros = []

while True:
    numero = input("Ingrese varios números y aprete 'Enter' para terminar: ")
    if numero == "":
        break
    try:
        lista_numeros.append(float(numero))
    except ValueError:
        print("Ingrese un dato válido")

if len(lista_numeros) == 1:
    print(f"Solo se ingreso el valor : {lista_numeros[0]}")
elif lista_numeros:
    lista_numeros.reverse()
    print(f"La lista de números invertida sería : {lista_numeros}")
else:
    print("No se ingresó ningun valor")