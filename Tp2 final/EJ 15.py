# 15- Indique que sucede si realizo la siguiente declaración de variable:
# x = None print(x)
# Explique y ejemplifique el uso de None

x = None
print(x)
print()
print(bool(x))
print()

print("None es un valor especial que indica que una variable está vacía.")
print()
print("Una variable que contenga None mostrará False si se transforma en boolena.")
print()
print("También se puede usar dentro de una condición para representar un caso donde no se devuelve un valor")
print()

def funcion_dia_laboral (dia_numero):
    dias_semana = {
        1: "Lunes",
        2: "Martes",
        3: "Miercoles",
        4: "Jueves",
        5: "Viernes",
        6: "Sabado",
        7: "Domingo"
    }

    if dia_numero in dias_semana:
        dia = dias_semana [dia_numero]
        if dia_numero >= 1 and dia_numero <= 5:
            return f"{dia} es un día laboral."
        else:
            return f"{dia} es un día no laboral"
    

def main():
    while True:
        try:
            dia_numero = int(input("Ingresa un número del 1 al 7 (1 = Lunes, 7 = Domingo): "))
            resultado = funcion_dia_laboral(dia_numero)
            if resultado == None:
                print("Ingrese un número válido")
            else:
                print(resultado)
                break
            
        except ValueError:
            print("Por favor, ingresa un valor válido")

print("En este caso con un ejercicio hecho en el TP 1, en nuestro while True, si el resultado arrojado es None, "
"osea un valor fuera del margen 1/7, el programa nos pedirá ingresar un dato válido, por la misma condición 'while True' siendo None: 'False'")
print()

if __name__ == "__main__":
    main()