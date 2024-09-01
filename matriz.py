from lista_enlazada import ListaCircular

class Matriz:
    def __init__(self, nombre, n, m):
        self.nombre = nombre
        self.n = n
        self.m = m
        self.lista_enlazada = ListaCircular()

    def agregar_dato(self, valor, x, y):
        self.lista_enlazada.agregar((x, y, valor))

    def obtener_matriz(self):
        return self.lista_enlazada.obtener_matriz()
