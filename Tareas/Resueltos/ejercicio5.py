# Ejercicio 05
def CalcularMaxMin(lista_num):
    num_max = 0
    num_min = 1000
    for i,dato in enumerate(lista_num):
        num_max = max(num_max, dato)
        num_min = min(num_min, dato)
    print(f"La lista es: {lista_num}")
    print(f"El valor maximo es: {num_max}")    
    print(f"El valor minimo es: {num_min}")    

