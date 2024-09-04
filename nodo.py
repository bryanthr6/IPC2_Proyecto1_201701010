#nodo.py
class Nodo:
    def __init__(self, nombre, matriz):
        self.nombre = nombre  # Nombre de la matriz
        self.matriz = matriz  # Datos de la matriz
        self.siguiente = None  # Apuntador al siguiente nodo
