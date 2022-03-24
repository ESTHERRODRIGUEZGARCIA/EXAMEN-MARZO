
import random
from datetime import datetime


class cuentabancaria():


    def __init__(self, id, fecha, nombre, saldo, modo):
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
        modo = int(input("Elija que cuenta desea crear: \n1. Cuenta a plazo fijo\n2 : Cuenta VIP \n"))
        numero = str(random.randint(100000000000, 999999999999))
        now = datetime.now()
        A = cuentabancaria(str(random.randint(100000, 999999)), nombre, datetime.now(),numero, 10000, modo)
        print("Hola " + nombre + ". Ha creado una cuenta el día " + str(datetime.now()) + " con el número de cuenta: " + numero)
        E = cuentabancaria(str(random.randint(100000, 999999)), "Segunda cuenta", datetime.now(), str(random.randint(100000000000, 999999999999)), 10000, 5)
        print("La segunda cuenta ha sido asociada a una cuenta VIP. También tiene un saldo inicial de 10.000 € ")

    crearcuenta()
cuentabancaria()


    def metodo(): #aquí me pedira retirar ingresar o transferir
        operacion = int(input("Introduzca que operacion va a realizar en su cuenta bancaria: /n1. Retirar/n2. Ingresar/n3. Transferir "))
        if operacion == 1:
            cuentabancaria.RETIRAR(A)
        if operacion == 2:
            cuentabancaria.INGRESAR(A)
        if operacion == 3:
            cuentabancaria.TRANSFERIR(A)
        else:
            print("Hasta pronto. ")




    def RETIRAR(self):
        dineroretirado=int(input("Usted ha elegido retirar dinero./n¿Cuánto desea retirar de su cuenta?: "))
        if dineroretirado > 0  and dineroretirado <= self.saldo:
            print("Han sido retirados ", dineroretirado, " €.")
            print("Ctualmente dispone de un saldo de ", self.saldo, " €.")
            nuevaop = int(input("¿Quiere realizar más operaciones?/nSí: pulse 1 /nNo: pulse 2\n "))
            if nuevaop == 1:
                operacion = int(input("Introduzca que operacion va a realizar en su cuenta bancaria: /n1. Retirar/n2. Ingresar/n3. Transferir "))
                if operacion == 1:
                    cuentabancaria.RETIRAR(A)
                if operacion == 2:
                    cuentabancaria.INGRESAR(A)
                if operacion == 3:
                    cuentabancaria.TRANSFERIR(A)
                else:
                    print("Hasta pronto. ")
            else:
                exit()

        else:
            print("Lo sentimos. No puede retirar más dinero del que tiene su cuenta.Introduzca correctamente cuánto quiere retirar de su cuenta.")
            cuentabancaria.RETIRAR(A)

    def INGRESAR(self):
        dineroingresado=int(input("Usted ha elegido ingresar dinero./n¿Cuánto desea ingresar a su cuenta?: "))
        if dineroingresado > 0:
            print("HAs ingresado ", dineroingresado, " €")
            self.saldo += dineroingresado
            print("Su saldo ahora es de ", self.saldo, " €")
            nuevaop = int(input("¿Quiere realizar más operaciones?/nSí: pulse 1 /nNo: pulse 2 "))
            if nuevaop == 1:
                operacion = int(input("Introduzca que operacion va a realizar en su cuenta bancaria: /n1. Retirar/n2. Ingresar/n3. Transferir "))
                if operacion == 1:
                    cuentabancaria.RETIRAR(A)
                if operacion == 2:
                    cuentabancaria.INGRESAR(A)
                if operacion == 3:
                    cuentabancaria.TRANSFERIR(A)
                else:
                    print("Hasta pronto. ")
            else:
                exit()

    def TRANSFERIR(self): #hay que hacer dos bucles pues si retiras de E a A eres penalizado
        aoe= int(input("Ha elegido transferir dinero. Desea transferir de su cuenta principal a su cuenta VIP?\npulse 1 (si)\npulse 2(operación contraria)"))
        if aoe == 1:
            dinerotransferido = int(input("Ha elegido transferir dinero a su segunda cuenta. ¿Cuánto desea transferir?"))
            if dinerotransferido <= self.saldo:
                print("HAn sido transferidos ", dinerotransferido, " € a la segunda cuenta (VIP).")
                A.saldo -= dinerotransferido
                E.saldo += dinerotransferido
                print("El saldo actual de la primera cuenta es de ", A.saldo, " €")
                print("El saldo actual de la segunda cuenta es de ", E.saldo, " €")
                nuevaop = int(input("¿Quiere realizar más operaciones?/nSí: pulse 1 /nNo: pulse 2 "))
                if nuevaop == 1:
                    operacion = int(input("Introduzca que operacion va a realizar en su cuenta bancaria: /n1. Retirar/n2. Ingresar/n3. Transferir "))
                    if operacion == 1:
                        cuentabancaria.RETIRAR(A)
                    if operacion == 2:
                        cuentabancaria.INGRESAR(A)
                    if operacion == 3:
                        cuentabancaria.TRANSFERIR(A)
                    else:
                        print("Hasta pronto. ")
                else:
                    exit()
        else:
            dinerotransferido = int(input("Ha elegido transferir dinero a su primera cuenta. ¿Cuánto desea transferir?"))
            if (dinerotransferido + dinerotransferido*0.05)<= self.saldo:
                print("Has transferido ", dinerotransferido, " €")
                A.saldo += dinerotransferido - dinerotransferido*0.05
                E.saldo -= dinerotransferido - dinerotransferido*0.05
                print("El saldo de su primera cuenta es de ", A.saldo, " €")
                print("El saldo de su primera cuenta es de ", E.saldo, " €")
                nuevaop = int(input("¿Quiere realizar más operaciones?/nSí: pulse 1 /nNo: pulse 2 "))
                if nuevaop == 1:
                    operacion = int(input("Introduzca que operacion va a realizar en su cuenta bancaria: /n1. Retirar/n2. Ingresar/n3. Transferir "))
                    if operacion == 1:
                        cuentabancaria.RETIRAR(A)
                    if operacion == 2:
                        cuentabancaria.INGRESAR(A)
                    if operacion == 3:
                        cuentabancaria.TRANSFERIR(A)
                    else:
                        print("Hasta pronto. ")
                else:
                    exit()



cuentabancaria()


