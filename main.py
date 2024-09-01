import xml.etree.ElementTree as ET
from cargar import cargar_archivo
from matriz import Matriz
from xml.dom import minidom

def convertir_a_matriz_binaria(matriz):
    filas = len(matriz)
    columnas = len(matriz[0])
    matriz_binaria = [[1 if valor > 0 else 0 for valor in fila] for fila in matriz]
    return matriz_binaria

def agrupar_tuplas(matriz_binaria):
    grupos = {}
    patrones = {}
    for i, fila in enumerate(matriz_binaria):
        patron = tuple(fila)
        if patron not in patrones:
            patrones[patron] = len(grupos) + 1
            grupos[len(grupos) + 1] = []
        grupos[patrones[patron]].append(i)
    return grupos

def crear_matriz_reducida(matriz, grupos):
    n_reducida = len(grupos)
    m = len(matriz[0])
    matriz_reducida = [[0] * m for _ in range(n_reducida)]
    for g, indices in grupos.items():
        for idx in indices:
            for j in range(m):
                matriz_reducida[g-1][j] += matriz[idx][j]
    return matriz_reducida

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

def main():
    archivo_xml = None  # Variable para almacenar la referencia al archivo XML
    matriz_enlazada = None

    opcion = 0
    while opcion != 6:
        print("Menu Principal")
        print("1. Cargar Archivo")
        print("2. Procesar Archivo")
        print("3. Escribir Archivo de Salida")
        print("4. Mostrar datos del estudiante")
        print("5. Generar gráfica")
        print("6. Salir")
        try:
            opcion = int(input("Seleccione una opción: "))
        except ValueError:
            print("ERROR: No ingresó un número entero")
            print(" ")
            continue

        match opcion:
            case 1:
                archivo_xml = cargar_archivo()
            case 2:
                if archivo_xml is not None:
                    print("Calculando matriz binaria...")
                    n, m, datos = procesar_datos_xml(archivo_xml)
                    if n is not None and m is not None:
                        matriz_binaria = convertir_a_matriz_binaria(datos)
                        print("Realizando agrupamiento...")
                        grupos = agrupar_tuplas(matriz_binaria)
                        print("Realizando suma de tuplas...")
                        matriz_reducida = crear_matriz_reducida(datos, grupos)
                        matriz_enlazada = matriz_reducida
                        print("Archivo procesado.")
                else:
                    print("ERROR: No se ha cargado ningún archivo.")
            case 3:
                if matriz_enlazada is not None:
                    nombre_archivo = "Matriz_Salida"
                    escribir_archivo_salida(nombre_archivo, matriz_enlazada, agrupar_tuplas(convertir_a_matriz_binaria(datos)))
                else:
                    print("ERROR: No se ha procesado ningún archivo.")
            case 4:
                print("********************************************************")
                print("*              Datos del estudiante                    *")
                print("*Nombre: Bryant Herrera Rubio                          *")
                print("*Carnet: 201701010                                     *")
                print("*Curso: Introducción a la Programación y Computación 2 *")
                print("*Sección: N                                            *")
                print("*Ingeniería en Ciencias y Sistemas                     *")
                print("********************************************************")
                print(" ")
            case 5:
                print("Generando gráfica...")
            case 6:
                print("Saliendo del programa...")
            case _:
                print("ERROR: Opción no válida")
                print(" ")
            

if __name__ == '__main__':
    main()
