#Codifique un método que reciba como parámetro una cadena y determine si  la 
#misma  contiene o no números. 

def contiene_numeros(cadena):
    for caracter in cadena:
        if caracter.isdigit():
            return True
    return False
    
cadena = input("Ingrese una cadena: ")

if contiene_numeros(cadena):
    print("La cadena contiene números")
else:
    print("La cadena no contiene números")