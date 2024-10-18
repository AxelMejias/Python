# 4) Desarrolle un programa que ayude a una cajera a determinar el número de billetes y 
# monedas que se necesitan de cada una de las siguientes denominaciones 200, 100, 50, 
# 20, 10, 5, 2 y 1, y monedas de 0.50, 0.25, 0.10 y 0.05 centavos para una cantidad de 
# dinero dada. Ejemplo si la cantidad es 1390,55 se necesitan 6 billetes de 200, 1 billete 
# de 100, 1 billete de 50, 2 billetes de 20, 1 moneda de 0.50 y una moneda de 0.05 
# centavos. Plantee el algoritmo planteando métodos para su resolución.

# "((Agregué la moneda de 1 centavo para ser más preciso y tuve que importar el módulo "decimal",
# para que al ingresar otra cosa que no sea un número vuelva a preguntar.))"


from decimal import Decimal, InvalidOperation, ROUND_DOWN

def calcular_billetes_monedas(cantidad):
    denominaciones = [(200), (100), (50), (20), (10), (5), (2), (1), Decimal('0.50'), Decimal('0.25'), Decimal('0.10'), Decimal('0.05'), Decimal('0.01')]
    resultado = {}

    cantidad = Decimal(cantidad).quantize(Decimal('0.01'), rounding=ROUND_DOWN)

    for denominacion in denominaciones:
        if cantidad >= denominacion:
            cantidad_billetes_monedas = int(cantidad // denominacion)
            cantidad -= cantidad_billetes_monedas * denominacion
            resultado[denominacion] = cantidad_billetes_monedas

    return resultado

while True:
    try:
        cantidad = input("Por favor, ingresá una cantidad de dinero: ")
        cantidad = Decimal(cantidad).quantize(Decimal('0.01'), rounding=ROUND_DOWN)
        break  
    except (ValueError, InvalidOperation):
        print("Error: Ingresá un valor válido. Intentá otra vez.")  

resultado = calcular_billetes_monedas(cantidad)

print("Para la cantidad ingresada de dinero, se necesitan:")
for denominacion, cantidad in resultado.items():
    if denominacion >= 1:
        tipo_singular = "Billete"
        tipo_plural = "Billetes"
    else:
        tipo_singular = "Moneda"
        tipo_plural = "Monedas"
                    
    tipo = tipo_singular if cantidad == 1 else tipo_plural
    print(f"- {cantidad} {tipo} de '{denominacion:.2f}'.")