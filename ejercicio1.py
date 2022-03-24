#ejercicio1: Escriba una clase que permita describir un libro y situar los valores asociados. Dar un ejemplo de uso en Python.
class libro():
    def __init__(self, nombre, autor, fecha, pags, genero):
        self.nombre= nombre
        self.autor = autor
        self.fecha = fecha
        self.pags = pags
        self.genero = genero

    def nombre(self, nombre):
        print("Título: Vivencias en Villanueva de la Cañada Siglo XXI")

    def autor(self,autor):
        autor = int("Autor: Esther Rodríguez García")

    def fecha(self,fecha):
        print("FEcha de publicación: 28 de Diciembre 2003 ")

    def pags(self,pags):
        print("Número de páginas: 1028")

    def genero(self,genero):
        print("Género: Estudiante de ingeniería matemática. Universidad Alfonso X El Sabio.")

libro()
