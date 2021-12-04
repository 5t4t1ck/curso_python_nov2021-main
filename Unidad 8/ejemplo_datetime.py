#import datetime 
from datetime import date, datetime, timedelta

#FechaActual = datetime.datetime.now()
FechaActual = datetime.now()
print(FechaActual)

#fecha = datetime(1988, 3, 16)
fecha = datetime(2021, 12, 3, 17,28,33)
print(fecha)

fechaActual2 = datetime.strftime(FechaActual, "%d/%m/%Y %H:%M:%S")
print(fechaActual2)

fechaActual3 = datetime.strftime(FechaActual, "%b %d %Y %H:%M:%S")
print(fechaActual3)

fechaActual3 = datetime.strftime(FechaActual, "%B %d %Y %H:%M:%S")
print(fechaActual3)

fechaTexto = "Dec 03 2021 17:33:12"
fechaActual4 = datetime.strptime(fechaTexto, "%b %d %Y %H:%M:%S")
print(fechaActual4)

dia = datetime.strftime(FechaActual, "%d")
print(dia)

dia = int(datetime.strftime(FechaActual, "%d"))
print(dia)

horaActual = datetime.strftime(FechaActual, "%H:%M:%S")
print(horaActual)

fechaPasada = datetime(1988, 3, 16)
diferencia = FechaActual - fechaPasada
print(diferencia)
print(diferencia.days)
print(diferencia.total_seconds())

dia_delta = timedelta(days=10)
fechaInicial = date.today()
print(fechaInicial)
fechaFutura = fechaInicial + dia_delta
print(fechaFutura)

dia_delta = timedelta(days=-5)
fechaInicial = date.today()
print(fechaInicial)
fechaFutura = fechaInicial + dia_delta
print(fechaFutura)

fecha = datetime.now().isoformat()
print(fecha)