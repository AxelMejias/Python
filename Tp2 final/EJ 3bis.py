# 3- Codifique un algoritmo que solicite el ingreso de un numero de 3 dígitos (100 - 999)
# y por medio del uso de las operaciones matemáticas módulo 10 y división por 10
# efectué la suma de los 3 dígitos del número. Ejemplo ingreso 563, salida del algoritmo
# 14. Plantee el algoritmo planteando métodos para su resolución.

num = 0

while num < 100 or num > 999:
    num = int(input("Ingrese un número entre 100 y 999: "))

thirdDigit = num % 10
print("El 3er dígito de el número es:", thirdDigit)

secondDigit = int(((num - thirdDigit) / 10) % 10)
print("El 2do dígito de el número es:", secondDigit)

firstDigit = int((((num - thirdDigit) / 10) - secondDigit) / 10)
print("El 1er dígito de el número es:", firstDigit)
print("La suma entre estos 3 es:",firstDigit + secondDigit + thirdDigit)
