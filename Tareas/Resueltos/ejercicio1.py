# Ejercicio 01
def EscribirCentrado():
    cadena = input("Por favor digite la cadena: ")
    columnas = 80
    aux = (columnas - len(cadena)) // 2
    espacios = " " * aux
    print(espacios+cadena)

