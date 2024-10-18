#CASTEO: Codifique un programa que solicite el ingreso de un numero decimal y 
#asigne el mismo a una variable valorDecimal, aplique las operaciones de CASTING para 
#convertir la variable a los siguientes tipos de datos, short, int, long, float investigue las 
#diferentes formas de lograr la conversión. Muestre por pantalla el resultado de las 
#conversiones.  

valorString = (input("Ingrese un nro decimal: "))

while float(valorString) % 1 == 0:
    print()
    valorString = (input("Ese nro es entero, para este ejercicio por favor ingrese un nro con porción decimal:"))

print()
print("El nro es", valorString)
print()
print("No podemos pasar un nro decimal en string a entero, así que primero pasamos a float con float().")

valorDecimal = float(valorString)

print("Lo visualizaremos de la misma manera, pero podemos operar con el.")
print("Con el código [  print(valorDecimal/2)  ] obtenemos el sgte. resultado:")
print(valorDecimal/2)

print()
print("Ahora que tenemos el valor en float, podemos pasarlo a entero con int().")

valorEntero = int(valorDecimal)

print("Al hacerlo, se trunca y da como resultado:", valorEntero)
print()

print("Finalmente podemos pasarlo a booleano bool().")

valorBooleano = bool(valorString)

print("Como el nro era", valorString, "en booleano se vuelve", valorBooleano)
print()

num = 0

print("Si fueramos a usar la variable num=0 en booleano se vuelve", bool(num))