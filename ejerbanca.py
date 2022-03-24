
import random
from datetime import datetime


class cuentabancaria():


    def __init__(self, id, fecha, nombre, modo, saldo):
        self.id = id
        self.fecha = fecha
        self.nombre = nombre
        self.modo = modo
        self.saldo = saldo

    def setid(self, id):
        self.id = id

    def getid(self):
        return(self.id)

    def setfecha(self, fecha):
        self.fecha = fecha

    def getfecha(self):
        return(self.fecha)

    def setnombre(self, nombre):
        self.nombre = nombre

    def getnombre(self):
        return (self.nombre)

    def setmodo(self, modo):
        self.modo = modo

    def getmodo(self):
        return (self.modo)

    def setsaldo(self, saldo):
        self.saldo = saldo

    def getsaldo(self):
            return self.saldo


    def crearcuenta():
        print("Bienvenido. Usted va a crear una cuenta bancaria.")
        nombre = str(input("Introduzca su nombre por favor: "))
        global A
        global E
        modo = int(input("1. Cuenta a plazo fijo/n2 : Cuenta VIP "))
        numero = str(random.randint(100000000000, 999999999999))
        now = datetime.now()
        A = cuentabancaria(str(random.randint(100000, 999999)), nombre, datetime.now(),numero, 10000, modo)
        print("Hola " + nombre + ". Ha creado una cuenta el día " + str(datetime.now()) + " con el número de cuenta: " + numero)
        E = cuentabancaria(str(random.randint(100000, 999999)), "Segunda cuenta", datetime.now(), str(random.randint(100000000000, 999999999999)), 10000, 5)
        print("La segunda cuenta ha sido asociada a una cuenta VIP. También tiene un saldo inicial de 10.000 € ")

    crearcuenta()


    def RETIRAR():
        dineroretirado=int(input("Usted ha elegido retirar dinero./n¿Cuánto desea retirar de su cuenta?: "))
        if dineroretirado > 0  and dineroretirado <= self.saldo:
            print("Han sido retirados ", dineroretirado, " €.")
            print("Ctualmente dispone de un saldo de ", self.saldo, " €.")
            nuevaop = int(input("¿Quiere realizar más operaciones?/nSí: pulse 1 /nNo: pulse 2 "))
            if nuevaop == 1:
                pass #falta algo!!!
            else:
                exit()

        else:
            print("Lo sentimos. No puede retirar más dinero del que tiene su cuenta.Introduzca correctamente cuánto quiere retirar de su cuenta.")
            cuentabancaria.RETIRAR(A)

cuentabancaria()

