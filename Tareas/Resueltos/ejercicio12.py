#Ejercicio 11
def DiaJuliano():
    anio = int(input("Ingrese el año: "))
    mes = int(input("Ingrese el mes: "))
    dia = int(input("Ingrese el dia: "))
    if ValidaFecha(dia,mes,anio):
        jd = (365.25*(anio+4716)) + (30.6001*(mes+1)) + dia + (2 - (3*anio / 400)) - 1524.5
        print(f"La fecha juliana es: {int(jd)}")
    else:
        print("La fecha ingresada es erronea..")

