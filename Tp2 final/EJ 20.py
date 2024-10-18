#Cree una clase Fracción con dos atributos, numerador y denominador.  
#Agregue a la clase los siguientes 4 métodos e implemente los mismos:  
#sumarFracciones(Fraccion f1, Fraccion f2) 
#restarFracciones(Fraccion f1, Fraccion f2) 
#multiplicarFracciones(Fraccion f1, Fraccion f2) 
#dividirFracciones(Fraccion f1, Fraccion f2) 
#Todos los métodos deben retornar la fracción resultante de la operación. 
#Cree una clase OperacionesFraccion que contenga un método main donde se solicite 
#al usuario el ingreso de 4 valores numéricos enteros con los cuales se crearan 2 objetos 
#Fracción y finalizada la creación de los mismos se ejecutaran los 4 métodos 
#implementados anteriormente asignando el resultado a una nueva variable de tipo 
#Fracción y mostrando por pantalla el resultado de las operaciones realizadas.

class Fraccion:
    def __init__(self, numerador, denominador):
        self.numerador = numerador
        self.denominador = denominador

    def __repr__(self):
        return f"{self.numerador}/{self.denominador}"
    
    
    @staticmethod
    def sumarFracciones(f1, f2):
        numerador = f1.numerador * f2.denominador + f2.numerador * f1.denominador
        denominador = f1.denominador * f2.denominador
        return Fraccion (numerador, denominador)
    
    @staticmethod
    def restarFracciones(f1, f2):
        numerador = f1.numerador * f2.denominador - f2.numerador * f1.denominador
        denominador = f1.denominador * f2.denominador
        return Fraccion (numerador, denominador)
    
    @staticmethod
    def multiplicarFracciones(f1, f2):
        numerador = f1.numerador * f2.numerador
        denominador = f1.denominador * f2.denominador
        return Fraccion (numerador, denominador)
    
    @staticmethod
    def dividirFracciones(f1, f2):
        numerador = f1.numerador * f2.denominador
        denominador = f1.denominador * f2.numerador
        return Fraccion (numerador, denominador)
    
class OperacionesFraccion:
    @staticmethod
    def main():
        while True:
            try:
                numerador1 = int(input("Ingrese el valor del numerador de la primera fracción: "))
                denominador1 = int(input("Ingrese el valor del denominador de la primera fracción: "))
                fraccion1 = Fraccion(numerador1, denominador1)
                break
            except ValueError:
                print("El denominador debe ser un número distinto de cero. Intente nuevamente.")

        while True:
            try:
                numerador2 = int(input("Ingrese el valor del numerador de la segunda fracción: "))
                denominador2 = int(input("Ingrese el valor del denominador de la segunda fracción: "))
                fraccion2 = Fraccion(numerador2, denominador2)
                break
            except ValueError:
                print("El denominador debe ser un número distinto de cero. Intente nuevamente.")

        suma = Fraccion.sumarFracciones(fraccion1, fraccion2)
        resta = Fraccion.restarFracciones(fraccion1, fraccion2)
        multiplicacion = Fraccion.multiplicarFracciones(fraccion1, fraccion2)
        division = Fraccion.dividirFracciones(fraccion1, fraccion2)

        print(f"Suma: {fraccion1} + {fraccion2} = {suma}")
        print(f"Resta: {fraccion1} - {fraccion2} = {resta}")
        print(f"Multiplicación : {fraccion1} * {fraccion2} = {multiplicacion}")
        print(f"Division : {fraccion1} / {fraccion2} = {division}")

if __name__ == "__main__":
    OperacionesFraccion.main()