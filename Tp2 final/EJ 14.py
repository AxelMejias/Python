# 14- Indique si en Python existen o no variables de tipo valor y su contraparte tipo referencia como sucede en otros lenguajes como Java. 

print("")
print("Valores por referencia y por valor:")
print("")
print('Python maneja las variable dentro funciones como "varibles por valor".')
print("")
print("Las variables que son definidas en el bloque principal pueden ser utilizadas en las diferentes funciones.")

print("")
variable_global=23
print("Valor original de la variable global:", variable_global)
print("")
def sumar(num):
    return variable_global+num
print("Valor devuelto por una función le adiciona -en este caso- 3 unidades:", sumar(3))
print("")
print("Variable global sigue con el valor:", variable_global)
print("")
print("Sin embargo, ahora intentaramos cambiar la variable dentro de la funcion dará el sgte. error:")

def sumar(num):
    variable_global=variable_global+num
    return variable_global
print("")
print(f"Modificar variable global:", sumar(2))