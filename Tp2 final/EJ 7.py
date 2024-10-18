# 7- Solicite el ingreso de una cadena y determine el tamaño de la misma y cuantas vocales tiene en total.

cadena = input("Por favor ingrese una cadena: ")

print("La cadena tiene", len(cadena), "caractéres.")

nroDeAs = cadena.count("a")
nroDeEs = cadena.count("e")
nroDeIs = cadena.count("i")
nroDeOs = cadena.count("o")
nroDeUs = cadena.count("u")

nroDeAs += cadena.count("á")
nroDeEs += cadena.count("é")
nroDeIs += cadena.count("í")
nroDeOs += cadena.count("ó")
nroDeUs += cadena.count("ú")

nroDeAs += cadena.count("A")
nroDeEs += cadena.count("E")
nroDeIs += cadena.count("I")
nroDeOs += cadena.count("O")
nroDeUs += cadena.count("U")

nroDeAs += cadena.count("Á")
nroDeEs += cadena.count("É")
nroDeIs += cadena.count("Í")
nroDeOs += cadena.count("Ó")
nroDeUs += cadena.count("Ú")

nroDeVocales = nroDeAs + nroDeEs + nroDeIs + nroDeOs + nroDeUs

print("La cadena tiene", nroDeVocales, "vocales.")