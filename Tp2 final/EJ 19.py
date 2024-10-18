#19 Cree una clase OperacionMatematica con dos atributos valor1 y valor2 y un 
#atributo de nombre operación. 
#Agregue a la clase los siguientes 5 métodos e implemente la lógica correspondiente:  
#sumarNumeros() 
#restarNumeros() 
#multiplicarNumeros() 
#dividirNumeros() 
#El quinto método será el siguiente:  
#aplicarOperacion(operacion){  
#…………………..  
#}  
#Cree una clase Calculo que contenga un método main, donde cree una instancia de la 
#clase OperacionMatematica, asigne 2 valores para las variables de la instancia y 
#ejecute la función aplicarOperacion, pasando como parámetro primero “+”, después “
#”, a continuación “*” y finalmente “/”. Muestre por pantalla el resultado de las 
#operaciones.

class OperacionMatematica:
    def __init__(self, valor1, valor2):
        self.valor1 = valor1
        self.valor2 = valor2
        self.operacion = None

    def sumarNumeros(self):
        return self.valor1 + self.valor2
    
    def restarNumeros(self):
        return self.valor1 - self.valor2
    
    def multipllicarNumeros(self):
        return self.valor1 * self.valor2
    
    def dividirNumeros(self):
        if self.valor2 != 0:
            return self.valor1 / self.valor2
        else:
            return "Error, no se puede dividir entre cero"
        
    def aplicarOperacion(self, operacion):
        self.operacion == operacion
        if operacion == "+":
            return self.sumarNumeros()
        elif operacion == "-":
            return self.restarNumeros()
        elif operacion == "*":
            return self.multipllicarNumeros()
        elif operacion == "/":
            return self.dividirNumeros()
        else:
            print("Operación no válida")
        
class Calculo:
    @staticmethod
    def main ():
        valor1 = float(input("Ingrese el valor del primer número: "))
        valor2 = float(input("Ingrese el valor del segundo número: "))

        operacion = OperacionMatematica(valor1, valor2)

        operaciones = ["+", "-", "*", "/"]

        for op in operaciones:
            resultado = operacion.aplicarOperacion(op)
            print(f"{valor1} {op} {valor2} = {resultado}")

if __name__ == "__main__":
    Calculo.main()