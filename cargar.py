import xml.etree.ElementTree as ET

def cargar_archivo():
    archivo = input("Ingrese la ruta del archivo XML: ")
    try:
        tree = ET.parse(archivo)
        root = tree.getroot()
        print("Archivo cargado exitosamente.")
        print(" ")
        return root
    except FileNotFoundError:
        print("ERROR: El archivo no se encuentra.")
        print(" ")
    except ET.ParseError:
        print("ERROR: Error al parsear el archivo XML.")
        print(" ")
    except Exception as e:
        print(f"ERROR: {str(e)}")
        print(" ")
