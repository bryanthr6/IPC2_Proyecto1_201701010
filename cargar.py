
import xml.etree.ElementTree as ET
from lista import ListaCircular
from matriz import Matriz

def cargar_archivo():
    archivo = input("Ingrese la ruta del archivo XML: ")
    try:
        tree = ET.parse(archivo)
        root = tree.getroot()
        print("Archivo cargado exitosamente.")
        print(" ")

        lista_matrices = ListaCircular()
        for matriz_xml in root.findall('matriz'):
            nombre = matriz_xml.get('nombre')
            n = int(matriz_xml.get('n'))
            m = int(matriz_xml.get('m'))

            matriz = Matriz(nombre, n, m)
            for dato in matriz_xml.findall('dato'):
                x = int(dato.get('x'))
                y = int(dato.get('y'))
                valor = int(dato.text)
                matriz.agregar_dato(x, y, valor)

            lista_matrices.agregar(nombre, matriz)
        return lista_matrices

    except FileNotFoundError:
        print("ERROR: El archivo no se encuentra.")
        print(" ")
    except ET.ParseError:
        print("ERROR: Error al parsear el archivo XML.")
        print(" ")
    except Exception as e:
        print(f"ERROR: {str(e)}")
        print(" ")
