#Escribe un programa que pida al usuario una lista de números y cuente cuántos de 
#ellos son pares y cuántos son impares.

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
    pares = [numero for numero in lista_numeros if numero % 2 == 0]

    print(f"Los numeros pares de la lista son: {pares} dando en total {len(pares)} valores pares ")

    impares = [numero for numero in lista_numeros if numero % 2 != 0]

    print(f"Los numeros impares de la lista son: {impares} dando en total {len(impares)} valores impares")
else:    
    print("No se ingresó ningun valor")