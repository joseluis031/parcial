id = 12344
nombre = "jose"
ncuenta = 567
saldo = 2000
fecha = 2015
class cuenta_banco:
    def __init__(self,id,nombre,ncuenta,saldo,fecha):
        self.id = id
        self.nombre = nombre
        self.ncuenta = ncuenta
        self.saldo = saldo
        self.fecha = fecha
    def transferencia(self):
        operacion = input("¿Desea hacer una operación como transferir dinero,retirar o abonar?")
        if operacion == "no":
            print("Vale gracias por consultar este banco. Hasta pronto.")
        elif operacion == "abonar":
            introducir_dinero= float(input("Introduzca el dinero de desea ingresar en la cuenta: "))
            self.saldo = (self.saldo + introducir_dinero)
            print("Su saldo es de " , saldo , "€")
        elif operacion == "transferir":
            transferir = float(input("¿Cuanto dinero deseas transferir?:"))
            self.saldo = self.saldo - transferir
            if self.saldo < transferir:
                print("No tienes suficiente saldo para esa transferencia")
        elif operacion == "retirar":
            retirar_dinero= float(input("Introduzca el dinero que desea retirar: "))
            self.saldo = (self.saldo - retirar_dinero)
            if self.saldo < retirar_dinero:
                print("No tienes esa cantidad de dinero para retirar")
            
        

class vip:
