# 2) Si se asigna un valor a una variable fuera de rango (mayor de lo establecido) ¿Qué ocurre? ¿Existe alguna forma de resolverlo? Ejemplifique.


mi_lista = [1, 2, 3]

while True:
    try:
        indice = int(input("Ingrese un número del índice: "))

        if 0 <= indice < len(mi_lista): # Con esto verificamos si el índice está dentro del rango válido.
            print(mi_lista[indice])
            break
            
    except ValueError:
        print("Error: Ingresá un valor válido. Intentá otra vez.")               
            
    else:
        print("Error. índice fuera de Rango") # Y si en efecto esta fuera de rango, nos vuelve a pedir un índice correcto.