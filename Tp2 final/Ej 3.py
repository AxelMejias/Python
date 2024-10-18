# 3) Codifique un algoritmo que solicite el ingreso de un numero de 3 dígitos (100 - 999) 
# y por medio del uso de las operaciones matemáticas módulo 10 y división por 10 
# efectué la suma de los 3 dígitos del número. Ejemplo ingreso 563, salida del algoritmo 
# 14. Plantee el algoritmo planteando métodos para su resolución.


def suma_digitos(numero):
    digito1 = numero // 100
    digito2 = (numero // 10) % 10
    digito3 = numero % 10
    
    suma = digito1 + digito2 + digito3
    return suma

while True:
    try:
        numero = int(input("Por favor, ingresá un número de 3 dígitos (100-999): "))
        if 100 <= numero <= 999:
            break
        else:
            print("Error: Debes ingresar un número de 3 dígitos. Inténtalo de nuevo.")
            
    except ValueError:
        print("Error: Ingresá un valor válido. Intentá otra vez.")  

resultado = suma_digitos(numero)

print(f"La suma de los dígitos del número {numero} es: {resultado}")