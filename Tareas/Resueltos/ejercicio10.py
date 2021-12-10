#Ejercicio 10
def TiempoSegundos():
    try:
        hora = int(input("Ingrese las horas: "))
        min = int(input("Ingrese los minutos: "))
        seg = int(input("Ingrese los segundos: "))
        seg01 = seg + (min *60) + (hora*3600)
        print(f"Los valores ingresados (hh:mm:ss): {hora}:{min}:{seg} dan {seg01} segundos")
    except Exception as e:
        print("Los vlaores ingresados no son admitidos..")

def SegundosTiempo():
    try:
        segs = int(input("Ingrese los segundos: "))
        auxseg = 0
        if segs >= 3600:
            horas = segs // 3600
            auxseg = segs % 3600
            mins = auxseg // 60
            auxseg = auxseg % 60
            print(f"Los segundos ingresados {segs} da (hh:mm:ss): {horas}:{mins}:{auxseg}")
        elif (segs >= 60 and segs < 3600):
            horas = 0
            mins = auxseg // 60
            auxseg = auxseg % 60
            print(f"Los segundos ingresados {segs} da (hh:mm:ss): {horas}:{mins}:{auxseg}")
        elif (segs >= 0 and segs < 60):
            horas = 0
            mins = 0
            print(f"Los segundos ingresados {segs} da (hh:mm:ss): {horas}:{mins}:{segs}")
        else:
            print("Valores ingresados erroneos")
    except Exception as e:
        print("Los valores ingresados no son admitidos..")
 
