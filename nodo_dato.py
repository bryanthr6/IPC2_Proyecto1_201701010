#nodo_dato.py
class NodoDato:
    def __init__(self, x, y, valor):
        self.x = x  # Fila en la matriz
        self.y = y  # Columna en la matriz
        self.valor = valor  # Valor en esa posición
        self.siguiente = None  # Apuntador al siguiente dato en la estructura
