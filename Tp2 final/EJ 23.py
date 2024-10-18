#Crea un programa donde se pida el ingreso de una cadena y por medio de 
#recursión mostrar la cadena de forma inversa.  
#Ejemplo: Ingreso “computadora de escritorio”  
#Invertir cadena “oirotircse ed arodatupmoc”

def invertir_cadena(cadena):
    if len(cadena) == 0:
        return ""
    else:
        return cadena[-1] + invertir_cadena(cadena[:-1])
    
def main():
    cadena = input("Ingrese una cadena: ")
    cadena_invertida = invertir_cadena(cadena)
    print(f"Cadena invertida = {cadena_invertida}")

if __name__ == "__main__":
    main()