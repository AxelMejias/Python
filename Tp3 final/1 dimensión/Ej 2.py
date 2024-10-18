#Escribe un programa que pida al usuario una lista de números y encuentre el mayor y 
#el menor de ellos

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
    print(f"El número mayor de la lista es {max(lista_numeros)} y el número menor de la lista es {min(lista_numeros)}")
else:
    print("No se ingresó ningun valor")