from lista_enlazada import MatrizEnlazada

class Matriz:
    def __init__(self, nombre, n, m):
        self.nombre = nombre
        self.n = n
        self.m = m
        self.lista_enlazada = MatrizEnlazada(n, m)

    def agregar_dato(self, valor, x, y):
        self.lista_enlazada.agregar(valor, x, y)

    def obtener_matriz(self):
        return self.lista_enlazada.obtener_matriz()
