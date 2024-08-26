import xml.etree.ElementTree as ET
from collections import defaultdict

class Procesador:
    def __init__(self):
        self.matriz_original = []
        self.matriz_procesada = []

    def procesar_archivo(self, ruta_archivo):
        print(f"Ruta del archivo en procesar_archivo: {ruta_archivo}")

        try:
            tree = ET.parse(ruta_archivo)
            root = tree.getroot()
        except ET.ParseError:
            print("ERROR: El archivo XML está mal formado")
            return
        except Exception as e:
            print(f"ERROR: {e}")
            return

        matriz = {}
        self.matriz_original = {}
        
        for dato in root.findall('.//dato'):
            x = int(dato.get('x'))
            y = int(dato.get('y'))
            valor = int(dato.text)
            
            if x not in matriz:
                matriz[x] = {}
            
            matriz[x][y] = 1 if valor > 0 else 0
            self.matriz_original[(x, y)] = valor
        
        # Transponer para comparar filas
        self.matriz_procesada = [
            [matriz.get(row, {}).get(col, 0) for col in range(1, max(len(matriz.get(r, {})) for r in matriz) + 1)]
            for row in range(1, len(matriz) + 1)
        ]
        
        print("Matriz de patrones de acceso:")
        for fila in self.matriz_procesada:
            print(' '.join(map(str, fila)))
        print(" ")
        
        self.generar_matriz_reducida()
    
    def generar_matriz_reducida(self):
        fila_patrones = defaultdict(list)
        for index, fila in enumerate(self.matriz_procesada):
            fila_patrones[tuple(fila)].append(index)
        
        matriz_reducida = []
        for indices in fila_patrones.values():
            if len(indices) > 1:
                fila_sumada = [0] * len(self.matriz_procesada[0])
                for index in indices:
                    fila_sumada = [fila_sumada[i] + self.matriz_original.get((index + 1, i + 1), 0) for i in range(len(fila_sumada))]
                matriz_reducida.append(fila_sumada)
            else:
                matriz_reducida.append([self.matriz_original.get((indices[0] + 1, i + 1), 0) for i in range(len(self.matriz_procesada[0]))])
        
        print("Matriz reducida de frecuencia de accesos:")
        for fila in matriz_reducida:
            print(' '.join(map(str, fila)))
        print(" ")
