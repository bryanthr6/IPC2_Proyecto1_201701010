class Nodo:
    def __init__(self, x, y, valor):
        self.x = x  # Posición x (fila)
        self.y = y  # Posición y (columna)
        self.valor = valor  # Valor de la celda
        
        # Referencias a los nodos vecinos
        self.arriba = None
        self.abajo = None
        self.izquierda = None
        self.derecha = None

    def __repr__(self):
        return f"Nodo({self.x}, {self.y}, {self.valor})"
