import xml.etree.ElementTree as ET
from xml.dom import minidom

class ProcesadorMatriz:
    def __init__(self, matriz):
        self.matriz = matriz

    def convertir_a_matriz_binaria(self):
        return [[1 if valor > 0 else 0 for valor in fila] for fila in self.matriz]

    def agrupar_tuplas(self, matriz_binaria):
        grupos = {}
        patrones = {}
        for i, fila in enumerate(matriz_binaria):
            patron = tuple(fila)
            if patron not in patrones:
                patrones[patron] = len(grupos) + 1
                grupos[len(grupos) + 1] = []
            grupos[patrones[patron]].append(i)
        return grupos

    def crear_matriz_reducida(self, grupos):
        n_reducida = len(grupos)
        m = len(self.matriz[0])
        matriz_reducida = [[0] * m for _ in range(n_reducida)]
        for g, indices in grupos.items():
            for idx in indices:
                for j in range(m):
                    matriz_reducida[g-1][j] += self.matriz[idx][j]
        return matriz_reducida

    @staticmethod
    def procesar_datos_xml(root):
        matriz_elemento = root.find('matriz')
        if matriz_elemento is None:
            print("ERROR: No se encontró el elemento <matriz> en el archivo XML.")
            return None, None, None
        
        n = int(matriz_elemento.get('n'))
        m = int(matriz_elemento.get('m'))
        
        datos = []
        for dato in matriz_elemento.findall('dato'):
            x = int(dato.get('x')) - 1
            y = int(dato.get('y')) - 1
            valor = int(dato.text)
            while len(datos) <= x:
                datos.append([0] * m)
            datos[x][y] = valor
        
        return n, m, datos

    @staticmethod
    def escribir_archivo_salida(nombre_archivo, matriz_reducida, grupos):
        root = ET.Element("matrices")
        matriz_elem = ET.SubElement(root, "matriz", nombre=nombre_archivo, n=str(len(matriz_reducida)), m=str(len(matriz_reducida[0])), g=str(len(grupos)))
        for i, fila in enumerate(matriz_reducida):
            for j, valor in enumerate(fila):
                ET.SubElement(matriz_elem, "dato", x=str(i+1), y=str(j+1)).text = str(valor)
        
        for g, indices in grupos.items():
            frecuencia_elem = ET.SubElement(matriz_elem, "frecuencia", g=str(g))
            frecuencia_elem.text = str(len(indices))
        
        # Convertir el elemento a una cadena de texto
        xml_str = ET.tostring(root, 'utf-8')
        # Usar minidom para formatear el XML
        parsed_xml = minidom.parseString(xml_str)
        pretty_xml_str = parsed_xml.toprettyxml(indent="    ")
        
        # Guardar el XML formateado en un archivo
        with open("C:\\Users\\Bryant Herrera\\Documents\\IPC2 2S2024\\IPC2_Proyecto1_201701010\\" + nombre_archivo + ".xml", "w") as f:
            f.write(pretty_xml_str)
