
import xml.etree.ElementTree as ET
from xml.dom import minidom

def escribir_archivo_salida(matriz, ruta_salida):
    # Crear la estructura XML
    matriz_element = ET.Element("matriz", nombre=matriz.nombre, n=str(matriz.n), m=str(matriz.m), g=str(matriz.n))
    
    actual = matriz.head
    while actual:
        # Crear el elemento <dato> con atributos x, y y el valor correspondiente
        dato_element = ET.SubElement(matriz_element, "dato", x=str(actual.x), y=str(actual.y))
        dato_element.text = str(actual.valor)
        actual = actual.siguiente

    # Añadir los elementos <frecuencia> al final, contando correctamente los grupos
    grupo = 1
    actual = matriz.head
    while actual:
        if actual.y == matriz.m + 1:  # Frecuencia está almacenada en la última "columna" como se define en generar_matriz_reducida
            frecuencia_element = ET.SubElement(matriz_element, "frecuencia", g=str(grupo))
            frecuencia_element.text = str(actual.valor)
            grupo += 1
        actual = actual.siguiente

    # Crear el árbol XML
    tree = ET.ElementTree(matriz_element)

    # Formatear el XML con sangrías
    xml_str = minidom.parseString(ET.tostring(matriz_element)).toprettyxml(indent="   ")

    # Escribir el archivo XML
    with open(ruta_salida, "w") as f:
        f.write(xml_str)

    print(f"Archivo de salida escrito correctamente en {ruta_salida}")

