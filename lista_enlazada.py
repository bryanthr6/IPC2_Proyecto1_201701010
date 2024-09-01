from nodo import Nodo

class MatrizEnlazada:
    def __init__(self, n, m):
        self.n = n  # Número de filas
        self.m = m  # Número de columnas
        self.head = None  # Nodo inicial de la matriz enlazada

    def crear_matriz(self, datos):
        """
        Crear una matriz enlazada a partir de los datos.
        `datos` es una lista de tuplas (x, y, valor) que representan las celdas.
        """
        nodos = [[None for _ in range(self.m)] for _ in range(self.n)]
        
        # Crear nodos
        for x, y, valor in datos:
            nodo = Nodo(x, y, valor)
            nodos[x][y] = nodo

        # Conectar nodos
        for i in range(self.n):
            for j in range(self.m):
                nodo_actual = nodos[i][j]
                if nodo_actual is None:
                    continue

                # Conectar con el nodo de la izquierda
                if j > 0 and nodos[i][j-1]:
                    nodo_actual.izquierda = nodos[i][j-1]
                    nodos[i][j-1].derecha = nodo_actual
                
                # Conectar con el nodo de arriba
                if i > 0 and nodos[i-1][j]:
                    nodo_actual.arriba = nodos[i-1][j]
                    nodos[i-1][j].abajo = nodo_actual

        # La cabeza de la matriz es el nodo superior izquierdo
        self.head = nodos[0][0]

    def mostrar_matriz(self):
        """
        Muestra la matriz enlazada recorriéndola desde el nodo superior izquierdo.
        """
        nodo_actual = self.head
        while nodo_actual:
            nodo_fila = nodo_actual
            while nodo_fila:
                print(f"{nodo_fila.valor} ", end="")
                nodo_fila = nodo_fila.derecha
            print("")
            nodo_actual = nodo_actual.abajo
