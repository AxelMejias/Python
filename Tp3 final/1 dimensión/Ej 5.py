#Escribe un programa que multiplique cada elemento de una lista de números por un 
#valor ingresado por el usuario. 

lista_numeros = []

while True:
    numero = input("Ingrese varios números y aprete 'Enter' para terminar: ")
    if numero == "":
        break
    try:
        lista_numeros.append(float(numero))
    except ValueError:
        print("Ingrese un dato válido")

try:
    multiplicador = float(input("Ingresa un número por el que quieras multiplicar todos los valores de la lista: "))
except ValueError:
    print("Ingrese un dato válido")
    exit()

result_multiplicador = [numero * multiplicador for numero in lista_numeros]

if len(lista_numeros) == 0:
    print("No se puede multiplicar porque la lista no tiene valores.")
else:
    print(f"Los valores de la lista son: {lista_numeros}")
    print(f"Los valores multiplicados por {multiplicador} en la lista son: {result_multiplicador}")