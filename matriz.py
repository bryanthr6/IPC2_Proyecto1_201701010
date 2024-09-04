
from nodo_dato import NodoDato

class Matriz:
    def __init__(self, nombre, n, m):
        self.nombre = nombre  # Nombre de la matriz
        self.n = n  # Número de filas
        self.m = m  # Número de columnas
        self.head = None  # Nodo inicial de la matriz

    def agregar_dato(self, x, y, valor):
        nuevo_dato = NodoDato(x, y, valor)
        if self.head is None:
            self.head = nuevo_dato
        else:
            actual = self.head
            while actual.siguiente:
                actual = actual.siguiente
            actual.siguiente = nuevo_dato

    def obtener_dato(self, x, y):
        actual = self.head
        while actual:
            if actual.x == x and actual.y == y:
                return actual.valor
            actual = actual.siguiente
        return None  # Si no se encuentra el dato

    def mostrar(self):
        actual = self.head
        while actual:
            print(f"({actual.x}, {actual.y}) -> {actual.valor}")
            actual = actual.siguiente
