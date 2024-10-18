#21 Codifique un programa que solicite un número entero mayor a cero y que 
#mediante recursión sume todos los números números naturales desde el número 
#ingresado hasta 1.  
#Ejemplo: Ingreso 10  
#El programa debe sumar 10 + 9 + 8 +7 +6 + 5 + 4 + 3 + 2 + 1 

#limite denotado en "998"
def suma_recursiva(n):
    if n == 1:
        return 1
    else:
        return n + suma_recursiva(n - 1)
    
def construir_expresion(n):
    if n == 1:
        return "1"
    else:
        return f"{n} + {construir_expresion(n - 1)}"

def main():
    while True:
        try:
            numero = int(input("Ingrese un número mayor a cero: "))
            if numero > 0:
                break
            else:
                print("El número debe ser mayora cero.")
        except ValueError:
            print("Debe ser un número entero: ")

    resultado = suma_recursiva(numero)
    expresion = construir_expresion(numero)
    print(f"La suma de todos los números desde {numero} hasta 1 es: {expresion} = {resultado}")
    #print(f"Siendo la suma de los valores = {expresion}")

if __name__ == "__main__":
    main()