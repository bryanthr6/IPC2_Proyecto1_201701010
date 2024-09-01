import xml.etree.ElementTree as ET
from cargar import cargar_archivo
from matriz import Matriz
from xml.dom import minidom
from procesador import ProcesadorMatriz

def main():
    archivo_xml = None
    matriz = None
    procesador = None

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
                    n, m, datos = ProcesadorMatriz.procesar_datos_xml(archivo_xml)
                    if n is not None and m is not None:
                        matriz_binaria = ProcesadorMatriz(datos).convertir_a_matriz_binaria()
                        print("Realizando agrupamiento...")
                        grupos = ProcesadorMatriz(datos).agrupar_tuplas(matriz_binaria)
                        print("Realizando suma de tuplas...")
                        matriz_reducida = ProcesadorMatriz(datos).crear_matriz_reducida(grupos)
                        matriz = Matriz("Matriz_Salida", len(matriz_reducida), len(matriz_reducida[0]))
                        for i in range(len(matriz_reducida)):
                            for j in range(len(matriz_reducida[i])):
                                matriz.agregar_dato(matriz_reducida[i][j], i, j)
                        procesador = ProcesadorMatriz(matriz_reducida)
                        print("Archivo procesado.")
                else:
                    print("ERROR: No se ha cargado ningún archivo.")
            case 3:
                if matriz is not None:
                    nombre_archivo = "Matriz_Salida"
                    ProcesadorMatriz.escribir_archivo_salida(nombre_archivo, matriz.obtener_matriz(), procesador.agrupar_tuplas(matriz_binaria))
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
