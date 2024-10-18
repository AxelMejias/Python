#17 Cree una clase FuncionesPrograma y codifique una función estática getFechaString 
#que reciba como parámetro una fecha y retorne la fecha como una cadena literal.  
#Ejemplo recibo 15/10/1900, la salida debe ser 
#Quince de Octubre de mil novecientos. 
#Cree una clase Principal que contenga un método main y haga uso de la función 
#getFechaString.

class FunccionesPrograma:
    def getFechaString(fecha):
        # Diccionarios para días, meses, unidades, decenas y centenas
        dias = {
            "01": "Uno", "02": "Dos", "03": "Tres", "04": "Cuatro", "05": "Cinco",
            "06": "Seis", "07": "Siete", "08": "Ocho", "09": "Nueve", "10": "Diez",
            "11": "Once", "12": "Doce", "13": "Trece", "14": "Catorce", "15": "Quince",
            "16": "Dieciséis", "17": "Diecisiete", "18": "Dieciocho", "19": "Diecinueve",
            "20": "Veinte", "21": "Veintiuno", "22": "Veintidós", "23": "Veintitrés",
            "24": "Veinticuatro", "25": "Veinticinco", "26": "Veintiséis", "27": "Veintisiete",
            "28": "Veintiocho", "29": "Veintinueve", "30": "Treinta", "31": "Treinta y uno"
        }

        meses = {
            "01": "Enero", "02": "Febrero", "03": "Marzo", "04": "Abril", "05": "Mayo",
            "06": "Junio", "07": "Julio", "08": "Agosto", "09": "Septiembre", "10": "Octubre",
            "11": "Noviembre", "12": "Diciembre"
        }

        unidades = {
            "0": "", "1": "uno", "2": "dos", "3": "tres", "4": "cuatro", "5": "cinco",
            "6": "seis", "7": "siete", "8": "ocho", "9": "nueve"
        }

        decenas = {
            "0": "", "3": "treinta", "4": "cuarenta", "5": "cincuenta",
            "6": "sesenta", "7": "setenta", "8": "ochenta", "9": "noventa"
        }

        centenas = {
            "0": "", "1": "ciento ", "2": "doscientos ", "3": "trescientos ", "4": "cuatrocientos ",
            "5": "quinientos ", "6": "seiscientos ", "7": "setecientos ", "8": "ochocientos ",
            "9": "novecientos "
        }

        dia, mes, anio = fecha.split("/")

        dia_literal = dias[dia]
        mes_literal = meses[mes]

        anio_literal = ""
        if anio[0] == "1":
            anio_literal += "mil "
        elif anio[0] == "2":
            anio_literal += "dos mil "
        elif anio[0] == "3":
            anio_literal += "tres mil "
        elif anio[0] == "4":
            anio_literal += "cuatro mil "
        elif anio[0] == "5":
            anio_literal += "cinco mil "
        elif anio[0] == "6":
            anio_literal += "seis mil "
        elif anio[0] == "7":
            anio_literal += "siete mil "
        elif anio[0] == "8":
            anio_literal += "ocho mil "
        else:
            anio [0] == "9"
            anio_literal += "nueve mil "


        anio_literal += centenas[anio[1]]

        if anio[2] == "0":
            anio_literal += unidades[anio[3]]
        elif anio[2] == "1":
            anio_literal += {
                "0": "diez", "1": "once", "2": "doce", "3": "trece", "4": "catorce",
                "5": "quince", "6": "dieciséis", "7": "diecisiete", "8": "dieciocho", "9": "diecinueve"
            }[anio[3]]
        elif anio[2] == "2":
            anio_literal += {
                "0": "veinte", "1": "veintiuno", "2": "veintidós", "3": "veintitrés",
                "4": "veinticuatro", "5": "veinticinco", "6": "veintiséis", "7": "veintisiete",
                "8": "veintiocho", "9": "veintinueve"
            }[anio[3]]
        else:
            if anio[3] == "0":
                anio_literal += decenas[anio[2]]
            else:
                anio_literal += decenas[anio[2]] + " y " + unidades[anio[3]]

        anio_literal = anio_literal.strip()

        fecha_literal = f"{dia_literal} de {mes_literal} de {anio_literal}".strip()

        return fecha_literal

class Principal:
    def main():
        while True:
            try:
                fecha = input("Ingrese una fecha (dd/mm/yyyy): ")
                if len(fecha) != 10 or fecha[2] != '/' or fecha[5] != '/':
                    raise ValueError
                dia, mes, anio = fecha.split("/")
                if not (1 <= int(dia) <= 31) or not (1 <= int(mes) <= 12) or not (1 <= int(anio) <= 9999):
                    raise ValueError
                fecha_literal = FunccionesPrograma.getFechaString(fecha)
                print(fecha_literal)
                break
            except ValueError:
                print("Ingrese una fecha válida en formato dd/mm/yyyy.")

if __name__ == "__main__":
    Principal.main()