def main():
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
                cargar_archivo()
            case 2:
                procesar_archivo()
            case 3:
                escribir_archivo()
            case 4:
                print('------------------------------------')
                print('|DATOS DEL ESTUDIANDTE             |')
                print('|Carnet: 201701010                 |')
                print('|Nombre: Bryant Herrera Rubio      |')
                print('------------------------------------')
                print(" ")
            case 5:
                generar_grafica()
            case 6:
                print("Saliendo...")    
            case _:
                print("ERROR: Opción no válida")
                print(" ")

def cargar_archivo():
    print("Cargando archivo...")
    print(" ")

def procesar_archivo():
    print("Procesando archivo...")
    print(" ")

def escribir_archivo():
    print("Escribiendo archivo...")
    print(" ")

def generar_grafica():
    print("Generando gráfica...")
    print(" ")

if __name__ == '__main__':
    main()

