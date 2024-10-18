#En la clase FuncionesPrograma codifique una método getFechaDate estática que 
#reciba como parámetro 3 valores enteros, día, mes, anio y retorne la fecha de tipo 
#date correspondiente.  
#En la clase Principal creada en el punto anterior haga uso de la función getFechaDate. 

from datetime import date

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

        dia, mes, año = fecha.split("/")

        dia_literal = dias[dia]
        mes_literal = meses[mes]

        año_literal = ""
        if año[0] == "1":
            año_literal += "mil "
        elif año[0] == "2":
            año_literal += "dos mil "
        año_literal += centenas[año[1]]

        if año[2] == "0":
            año_literal += unidades[año[3]]
        elif año[2] == "1":
            año_literal += {
                "0": "diez", "1": "once", "2": "doce", "3": "trece", "4": "catorce",
                "5": "quince", "6": "dieciséis", "7": "diecisiete", "8": "dieciocho", "9": "diecinueve"
            }[año[3]]
        elif año[2] == "2":
            año_literal += {
                "0": "veinte", "1": "veintiuno", "2": "veintidós", "3": "veintitrés",
                "4": "veinticuatro", "5": "veinticinco", "6": "veintiséis", "7": "veintisiete",
                "8": "veintiocho", "9": "veintinueve"
            }[año[3]]
        else:
            if año[3] == "0":
                año_literal += decenas[año[2]]
            else:
                año_literal += decenas[año[2]] + " y " + unidades[año[3]]

        año_literal = año_literal.strip()

        fecha_literal = f"{dia_literal} de {mes_literal} de {año_literal}".strip()

        return fecha_literal
    
    def getFechaDate(dia, mes, año):
        return date(año, mes, dia)

class Principal:
    def main():
        while True:
            try:
                fecha = input("Ingrese una fecha (dd/mm/yyyy): ")
                if len(fecha) != 10 or fecha[2] != '/' or fecha[5] != '/':
                    raise ValueError
                dia, mes, año = fecha.split("/")
                dia, mes, año = int(dia), int(mes), int(año)
                if not (1 <= int(dia) <= 31) or not (1 <= int(mes) <= 12) or not (1 <= int(año) <= 9999):
                    raise ValueError
                fecha_date = FunccionesPrograma.getFechaDate(dia, mes, año)
                fecha_literal = FunccionesPrograma.getFechaString(fecha)
                print(f"Fecha en formato date: {fecha_date}")
                print(f"Fecha en formato literal: {fecha_literal}")
                break
            except ValueError:
                print("Ingrese una fecha válida en formato dd/mm/yyyy.")

if __name__ == "__main__":
    Principal.main()