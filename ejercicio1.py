#ejercicio1: Escriba una clase que permita describir un libro y situar los valores asociados. Dar un ejemplo de uso en Python.
class libro():
    def __init__(self, autor, fecha, pags, tema):
        self.autor = autor
        self.fecha = fecha
        self.pags = pags
        self.tema = tema

    def autor():
        print("El autor del libro es ")