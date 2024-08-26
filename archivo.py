import xml.etree.ElementTree as ET

class Archivo:
    def __init__(self):
        self.ruta_archivo = ''

    def cargar_archivo(self):
        ruta = input("Ingrese la ruta completa del archivo XML: ")
        try:
            with open(ruta, 'r') as file:
                print("Archivo cargado con éxito")
                print(" ")
                self.ruta_archivo = ruta
        except FileNotFoundError:
            print("ERROR: No se pudo encontrar el archivo en la ruta proporcionada")
            print("")
            self.ruta_archivo = ''
            return ''
    
    def escribir_archivo(self):
        print("Escribiendo archivo...")
        print(" ")
