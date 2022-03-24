import random
from datetime import datetime, timedelta
id = random.randint(1000, 9999)
print ("Tu id es: ",id)
nombre = "jose"
print (nombre)
ncuenta = random.randint(100000000000, 999999999999)
print ("Tu numero de cuenta es: ",ncuenta)
saldo = 10000
print ("Tu saldo es: ",saldo)

inicio = datetime(2015, 1, 30)
final =  datetime(2017, 5, 28)
random_date = inicio + timedelta(seconds= int((final - inicio).total_seconds() * random.random()))
print("Tu fecha de apertura de la cuenta es: " , random_date)

inicio2 = datetime(2017, 5, 30)
final2 =  datetime(2023, 5, 28)
random_date2 = inicio2 + timedelta(seconds= int((final2 - inicio2).total_seconds() * random.random()))
print("Tu fecha de vencimiento de la cuenta es: " , random_date2)

class cuenta_banco:
    def __init__(self,id,nombre,ncuenta,saldo):
        self.id = id
        self.nombre = nombre
        self.ncuenta = ncuenta
        self.saldo = saldo
        
    def transferencia(self):
        operacion = input("¿Desea hacer una operación como transferir dinero o ingresar?")
        if operacion == "no":
            print("Vale gracias por consultar este banco. Hasta pronto.")
        elif operacion == "ingresar":
            introducir_dinero= 575
            self.saldo = (self.saldo + introducir_dinero)
            print("Su saldo es de " , saldo , "€")
        elif operacion == "transferir":
            transferir = 2000
            self.saldo = self.saldo - transferir
            if self.saldo < transferir:
                print("No tienes suficiente saldo para esa transferencia")
    def retirar(self):
        operacion2 = input("¿Desea hacer una operacion de retirar dinero?(escriba retirar)")
        if operacion2 == "retirar":
            retirar_dinero= 78
            self.saldo = (self.saldo - retirar_dinero)
            if self.saldo < retirar_dinero:
                    print("No tienes esa cantidad de dinero para retirar")
                
        

class Plazo_fijo(cuenta_banco):
    def __init__(self,id,nombre,ncuenta,saldo):
         cuenta_banco.__init__(self,id,nombre,ncuenta,saldo)
    def transferencia(self):
        return super().transferencia()
    def retirar2(self):
        operacion3 = input("¿Desea hacer una operacion de retirar dinero?(escriba retirar)")
        if operacion3 == "retirar":
            retirar_dinero= 78
            self.saldo = (self.saldo - retirar_dinero)-(retirar_dinero*0.05)
            if self.saldo < retirar_dinero:
                    print("No tienes esa cantidad de dinero para retirar")
        
    
class vip(cuenta_banco):
    def __init__(self,id,nombre,ncuenta,saldo,saldonegativo):
        self.saldonegativo = saldonegativo
        cuenta_banco.__init__(self,id,nombre,ncuenta,saldo)
    def transferencia(self):
        return super().transferencia()
    def retirar(self):
        return super().retirar()
         
    