# 5- Solicite el ingreso de una cadena y elimine todos los espacios de la misma, muestre la cadena resultante.

cadena = input("Por favor ingrese una oración: ")

lista = cadena.split()

texto_unido = "".join(lista)

print(texto_unido)