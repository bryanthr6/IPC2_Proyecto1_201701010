# lista_suma.py
class NodoSuma:
    def __init__(self, valor):
        self.valor = valor  # Valor de la suma en la columna específica
        self.siguiente = None  # Apuntador al siguiente nodo en la lista

class ListaSuma:
    def __init__(self):
        self.head = None

    def agregar_valor(self, valor):
        nuevo_nodo = NodoSuma(valor)
        if self.head is None:
            self.head = nuevo_nodo
        else:
            actual = self.head
            while actual.siguiente:
                actual = actual.siguiente
            actual.siguiente = nuevo_nodo

    def incrementar(self, index, valor):
        actual = self.head
        for i in range(index - 1):
            if actual is None:
                return
            actual = actual.siguiente
        if actual:
            actual.valor += valor

    def obtener_valor(self, index):
        actual = self.head
        for i in range(index - 1):
            if actual is None:
                return None
            actual = actual.siguiente
        if actual:
            return actual.valor
        return None
