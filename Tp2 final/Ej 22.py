# 22) Suma los dígitos de un número ingresado por el usuario de forma recursiva.


def suma_digitos(n):
    if n == 0:
        return 0
    else:
        return n % 10 + suma_digitos(n // 10)

def main():
    while True:
        try:
            numero = int(input("Ingrese un número entero: "))
            if numero < 0:
                print("Por favor, ingresá un número entero positivo.")
            else:
                resultado = suma_digitos(numero)
                print(f"La suma de los dígitos de '{numero}' es: '{resultado}'.")
                break

        except ValueError:
            print("Error: Ingresá un valor válido. Intentá otra vez.")

main()