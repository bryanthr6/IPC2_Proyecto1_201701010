from nodo import Nodo

class ListaCircular:
    def __init__(self):
        self.cabeza = None
        self.cola = None

    def agregar(self, dato):
        nuevo_nodo = Nodo(dato[0], dato[1], dato[2])
        if self.cabeza is None:
            self.cabeza = nuevo_nodo
            self.cola = nuevo_nodo
            self.cola.derecha = self.cabeza
            self.cabeza.arriba = self.cola
        else:
            self.cola.derecha = nuevo_nodo
            nuevo_nodo.arriba = self.cola
            self.cola = nuevo_nodo
            self.cola.derecha = self.cabeza
            self.cabeza.arriba = self.cola

    def mostrar(self):
        if self.cabeza is None:
            return "Lista vacía"
        actual = self.cabeza
        while True:
            print(f"({actual.x}, {actual.y}, {actual.valor})", end=" -> ")
            actual = actual.derecha
            if actual == self.cabeza:
                break
        print()

    def obtener_matriz(self):
        matriz = []
        if self.cabeza is None:
            return matriz
        actual = self.cabeza
        while True:
            if len(matriz) <= actual.x:
                matriz.append([0] * (actual.y + 1))
            if len(matriz[actual.x]) <= actual.y:
                matriz[actual.x].extend([0] * (actual.y + 1 - len(matriz[actual.x])))
            matriz[actual.x][actual.y] = actual.valor
            actual = actual.derecha
            if actual == self.cabeza:
                break
        return matriz
