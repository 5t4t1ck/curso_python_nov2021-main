# Ejercicio 06
def areaPerimetroCircunferencia():
    try:
        radio = float(input("Por favor digite el radio de la circunferencia: "))
        areaC = (radio ** 2) * pi
        periC = radio * 2 * pi
        print(f"El area es: {round(areaC,4)}")
        print(f"El permitero es: {round(periC,4)}")
    except Exception as e:
        print("El valor no ingresado no es valido")

