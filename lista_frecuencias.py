class NodoFrecuencia:
    def __init__(self, frecuencia):
        self.frecuencia = frecuencia
        self.siguiente = None

class ListaFrecuencia:
    def __init__(self):
        self.head = None
        self.tail = None

    def agregar_frecuencia(self, frecuencia):
        nuevo_nodo = NodoFrecuencia(frecuencia)
        if self.head is None:
            self.head = nuevo_nodo
            self.tail = nuevo_nodo
        else:
            self.tail.siguiente = nuevo_nodo
            self.tail = nuevo_nodo

    def recorrer_frecuencias(self):
        actual = self.head
        while actual:
            yield actual.frecuencia
            actual = actual.siguiente
