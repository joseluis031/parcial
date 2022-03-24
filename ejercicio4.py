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
        if operacion == "abonar":
            introducir_dinero= float(input("Introduzca el dinero de desea ingresar en la cuenta: "))
            saldo = (saldo + introducir_dinero)
            print("Su saldo es de " , saldo , "€")
        if operacion == "transferir":
            transferir = float(input("¿Cuanto dinero deseas transferir?:"))
            print("El saldo de su cuenta es " , saldo - transferir, "€")
        if operacion == "retirar":
            retirar_dinero= float(input("Introduzca el dinero que desea retirar: "))
            saldo = (saldo - retirar_dinero)
            if saldo >= 0:
                print("Con la retirada de " , retirar_dinero , " su saldo disminuye a un total de " , saldo , "€")
            if saldo < 0:
                saldo = saldo * -1
                print("Con la retirada de " , retirar_dinero ,"Usted no tiene saldo en la cuenta, además debe un total de  " , saldo , "€")
        

class vip:
