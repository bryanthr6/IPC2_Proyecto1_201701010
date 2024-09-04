#lista_patrones.py
# Definición de la clase Nodo para la lista enlazada
class NodoEnlazado:
    def __init__(self, dato):
        self.dato = dato  # Este será un nodo de la matriz
        self.siguiente = None  # Apuntador al siguiente nodo

# Clase ListaEnlazada para manejar los nodos de los patrones
class ListaEnlazada:
    def __init__(self):
        self.head = None

    def agregar(self, dato):
        nuevo_nodo = NodoEnlazado(dato)
        if not self.head:
            self.head = nuevo_nodo
        else:
            actual = self.head
            while actual.siguiente:
                actual = actual.siguiente
            actual.siguiente = nuevo_nodo

    def buscar(self, dato):
        actual = self.head
        while actual:
            if actual.dato == dato:
                return True
            actual = actual.siguiente
        return False


# PatronNodo es el nodo que contiene un patrón y la lista de nodos con ese patrón
class PatronNodo:
    def __init__(self, patron):
        self.patron = patron  # Cadena que representa el patrón binario
        self.nodos = ListaEnlazada()  # Lista de nodos que comparten el mismo patrón
        self.siguiente = None  # Apuntador al siguiente PatronNodo

# ListaPatrones es la lista que contiene los patrones
class ListaPatrones:
    def __init__(self):
        self.head = None  # Cabeza de la lista de patrones

    def agregar_patron(self, patron):
        nuevo_patron = PatronNodo(patron)
        if self.head is None:
            self.head = nuevo_patron
        else:
            actual = self.head
            while actual.siguiente:
                actual = actual.siguiente
            actual.siguiente = nuevo_patron
        return nuevo_patron

    def buscar_patron(self, patron):
        actual = self.head
        while actual:
            if actual.patron == patron:
                return actual
            actual = actual.siguiente
        return None
