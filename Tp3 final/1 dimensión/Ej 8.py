#Escribe un programa que identifique y muestre los elementos que se repiten en una 
#lista. 

lista_numeros = []

while True:
    numero = input("Ingrese varios números y aprete 'Enter' para terminar: ")
    if numero == "":
        break
    try:
        lista_numeros.append(float(numero))
    except ValueError:
        print("Ingrese un dato válido")

elementos_no_repetidos = set()

elementos_repetidos = set()

for elemento in lista_numeros:
    if elemento in elementos_no_repetidos:
        elementos_repetidos.add(elemento)
    else:
        elementos_no_repetidos.add(elemento)

if elementos_repetidos:
    print(f"Elementos que se repiten en la lista: {elementos_repetidos}")
else:
    print("No hay elementos repetidos en la lista")