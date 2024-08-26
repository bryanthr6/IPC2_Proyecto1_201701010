from archivo import Archivo
from procesador import Procesador
from grafica import GeneradorGrafica

def main():
    archivo = Archivo()
    procesador = Procesador()
    generador_grafica = GeneradorGrafica()

    opcion = 0
    while opcion != 6:
        print("Menu Principal")
        print("1. Cargar Archivo")
        print("2. Procesar Archivo")
        print("3. Escribir Archivo de Salida")
        print("4. Mostrar Datos del Estudiante")
        print("5. Generar Gráfica")
        print("6. Salir")
        try:
            opcion = int(input("Seleccione una opción: "))
        except ValueError:
            print("ERROR: No ingresó un número entero")
            print(" ")
            continue

        match opcion:
            case 1:
                ruta = archivo.cargar_archivo()
            case 2:
                if archivo.ruta_archivo:
                    procesador.procesar_archivo(archivo.ruta_archivo)
                else:
                    print(" ")
                    print("ERROR: No hay archivo cargado")
                    print(" ")
            case 3:
                archivo.escribir_archivo()
            case 4:
                print('------------------------------------')
                print('|DATOS DEL ESTUDIANTE               |')
                print('|Carnet: 201701010                  |')
                print('|Nombre: Bryant Herrera Rubio       |')
                print('------------------------------------')
                print(" ")
            case 5:
                generador_grafica.generar_grafica()
            case 6:
                print("Saliendo...")
            case _:
                print("ERROR: Opción no válida")
                print(" ")

if __name__ == '__main__':
    main()
