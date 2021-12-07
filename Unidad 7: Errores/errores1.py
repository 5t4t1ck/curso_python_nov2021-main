try:
    n = input("Introduce un número: ")
    5/n

except Exception as e:
    ("Ha ocurrido un error =>", type(e).__name__)

try:
    n = float(input("Introduce un valor en el divisor: "))
    5/n
except TypeError:
    print("No se puede dividir entre una cadena")
except ValueError:
    print("Debes introducir una cadena que sea un número")
except ZeroDivisionError:
    print("No se puede dividir un número por 0, prueba otro número")
except Exception as e:
    print("Ha ocurrido un error =>", type(e).__name__)   
