class Cliente:
    def __init__(self):
	    self.__numeroCuenta = 2021
    
    def __cuentaProceso(self):
        print("Procesando Cuenta...")
        
    def conseguirNumeroCuenta(self):
        return self.__cuentaProceso

c = Cliente()
print(c._Cliente__numeroCuenta)
c._Cliente__cuentaProceso()