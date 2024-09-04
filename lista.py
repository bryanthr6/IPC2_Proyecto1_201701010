#lista.py
from nodo import Nodo

class ListaCircular:
    def __init__(self):
        self.head = None  # Cabeza de la lista
        self.tail = None  # Cola de la lista (el último nodo)

    def agregar(self, nombre, matriz):
        nuevo_nodo = Nodo(nombre, matriz)
        if self.head is None:
            self.head = nuevo_nodo
            self.tail = nuevo_nodo
            nuevo_nodo.siguiente = nuevo_nodo  # Apunta a sí mismo, formando el círculo
        else:
            nuevo_nodo.siguiente = self.head
            self.tail.siguiente = nuevo_nodo
            self.tail = nuevo_nodo

    def mostrar(self):
        if self.head is None:
            print("La lista está vacía.")
            return

        actual = self.head
        while True:
            print(f"Matriz: {actual.nombre}")
            actual = actual.siguiente
            if actual == self.head:
                break

    def buscar(self, nombre):
        if self.head is None:
            return None

        actual = self.head
        while True:
            if actual.nombre == nombre:
                return actual
            actual = actual.siguiente
            if actual == self.head:
                break
        return None
