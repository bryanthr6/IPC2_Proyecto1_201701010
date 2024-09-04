#procesar.py
from lista_patrones import ListaPatrones  # Importa ListaPatrones
from lista_suma import ListaSuma  # Importa ListaSuma
from matriz import Matriz  # Importa la clase Matriz

class ProcesadorMatriz:
    def __init__(self, matriz):
        self.matriz = matriz
        self.patrones = ListaPatrones()  # Reemplazo del diccionario

    def procesar(self):
        self.agrupar_patrones()
        return self.generar_matriz_reducida()

    def agrupar_patrones(self):
        actual = self.matriz.head
        while actual:
            patron = self.generar_patron(actual)
            nodo_patron = self.patrones.buscar_patron(patron)
            if nodo_patron is None:
                nodo_patron = self.patrones.agregar_patron(patron)
            # Verificamos si el nodo actual ya existe en la lista de nodos
            if not nodo_patron.nodos.buscar(actual):
                nodo_patron.nodos.agregar(actual)  # Agregar el nodo a la lista de nodos del patrón
            actual = actual.siguiente


    def generar_patron(self, nodo):
        patron = ""
        for col in range(1, self.matriz.m + 1):
            valor = self.matriz.obtener_dato(nodo.x, col)
            patron += "1" if valor > 0 else "0"
        return patron

    def generar_matriz_reducida(self):
        matriz_reducida = Matriz(
            nombre=f"{self.matriz.nombre}_Salida",
            n=self.contar_patrones(),
            m=self.matriz.m
        )

        nodo_patron = self.patrones.head
        grupo = 1
        while nodo_patron:
            suma_fila = ListaSuma()
            for i in range(1, self.matriz.m + 1):
                suma_fila.agregar_valor(0)

            nodo_actual = nodo_patron.nodos.head
            print(f"Procesando grupo {grupo} con patrón: {nodo_patron.patron}")
            filas_sumadas = set()
            while nodo_actual:
                nodo_dato = nodo_actual.dato
                if nodo_dato.x not in filas_sumadas:
                    filas_sumadas.add(nodo_dato.x)
                    print(f"  Sumar fila {nodo_dato.x} con valores: ", end="")
                    for col in range(1, self.matriz.m + 1):
                        valor = self.matriz.obtener_dato(nodo_dato.x, col)
                        print(f"{valor} ", end="")
                        suma_fila.incrementar(col, valor)
                    print()  # Nueva línea después de imprimir los valores
                nodo_actual = nodo_actual.siguiente

            for col in range(1, self.matriz.m + 1):
                valor_sumado = suma_fila.obtener_valor(col)
                print(f"  Resultado columna {col}: {valor_sumado}")
                matriz_reducida.agregar_dato(grupo, col, valor_sumado)

            nodo_patron = nodo_patron.siguiente
            grupo += 1

        return matriz_reducida






    def contar_patrones(self):
        contador = 0
        actual = self.patrones.head
        while actual:
            contador += 1
            actual = actual.siguiente
        return contador
    
    def generar_matriz_patrones(self):
        matriz_patrones = Matriz(
            nombre=f"{self.matriz.nombre}_Patrones",
            n=self.matriz.n,
            m=self.matriz.m
        )

        actual = self.matriz.head
        while actual:
            patron = ""
            for col in range(1, self.matriz.m + 1):
                valor = self.matriz.obtener_dato(actual.x, col)
                patron += "1" if valor > 0 else "0"

            for col in range(1, len(patron) + 1):
                matriz_patrones.agregar_dato(actual.x, col, int(patron[col-1]))

            actual = actual.siguiente

        return matriz_patrones

