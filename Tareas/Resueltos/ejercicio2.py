# Ejercicio 02
def EsMultiplo():
    try:
        num1 = int(input("Por favor digite el numero 1: "))
        num2 = int(input("Por favor digite el numero 2: "))
        if num1 % num2 == 0:
            print(f"El numero {num1} es multiplo de {num2}")
        else:
            print(f"El numero {num1} NO es multiplo de {num2}")
    except Exception as e:
        print("Los valores ingresados no son enteros, error: ", type(e).__name__)

