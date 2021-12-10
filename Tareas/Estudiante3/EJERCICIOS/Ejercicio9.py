"""
Escribe un programa que pida un número entero entre uno 
y doce e imprima el número de días que tiene el mes correspondiente
"""
mes=int(input("Ingrese numero: "))
if mes>=1 and  mes<=12:
    if mes==1:
       nmes="Enero"
    elif mes==2:
       nmes="Febrero"
    elif mes==3:
        nmes="Marzo"
    elif mes==4:
        nmes="Abril"
    elif mes==5:
        nmes="Mayo"
    elif mes==6:
        nmes="Junio"
    elif mes==7:
        nmes="Julio"
    elif mes==8:
        nmes="Agosto"
    elif mes==9:
        nmes="Septiembre"
    elif mes==10:
        nmed="Octubre"
    elif mes==11:
        nmes="Noviembre"
    else:
        nmes="Diciembre"

    if(mes==1 or mes ==3 or mes==5 or mes==7 or mes==8 or mes==10 or mes==12):
        print("El mes ingresado es {mes} tiene {dias} dias".format(mes=nmes,dias=31))
    elif mes==2:
        print("El mes ingresado es {mes} tiene {dias} dias".format(mes=nmes,dias=28))
    else:
        print("El mes ingresado es {mes} tiene {dias} dias".format(mes=nmes,dias=30))

else:
    print("Valor ingresado no corresponde")