from cargar import cargar_archivo
from procesar import ProcesadorMatriz
from escribir import escribir_archivo_salida
from generar_grafica import generar_grafica_doble  # Nueva importación

def imprimir_matriz(matriz):
    actual = matriz.head
    for i in range(1, matriz.n + 1):
        fila = ""
        for j in range(1, matriz.m + 1):
            valor = matriz.obtener_dato(i, j)
            fila += f"{valor} "
        print(fila.strip())

def main():
    lista_matrices = None

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
                if lista_matrices is None:
                    lista_matrices = cargar_archivo()
                else:
                    nuevas_matrices = cargar_archivo()
                    if nuevas_matrices:
                        actual = nuevas_matrices.head
                        while True:
                            lista_matrices.agregar(actual.nombre, actual.matriz)
                            actual = actual.siguiente
                            if actual == nuevas_matrices.head:
                                break
            case 2:
                if lista_matrices:
                    lista_matrices.mostrar()
                    nombre_matriz = input("Ingrese el nombre de la matriz a procesar: ")
                    matriz = lista_matrices.buscar(nombre_matriz)
                    if matriz:
                        print("Matriz Original:")
                        imprimir_matriz(matriz.matriz)
                        
                        procesador = ProcesadorMatriz(matriz.matriz)
                        
                        matriz_patrones = procesador.generar_matriz_patrones()
                        print("\nMatriz de Patrones de Acceso:")
                        imprimir_matriz(matriz_patrones)
                        
                        matriz_reducida = procesador.procesar()
                        print("\nMatriz Reducida:")
                        imprimir_matriz(matriz_reducida)

                        # Asociar la matriz reducida con la original
                        matriz.matriz_reducida = matriz_reducida
                        
                        print("Matriz procesada correctamente.")
                    else:
                        print("ERROR: No se encontró la matriz especificada.")
                else:
                    print("ERROR: No se ha cargado ningún archivo.")
            case 3:
                if lista_matrices:
                    lista_matrices.mostrar()
                    nombre_matriz = input("Ingrese el nombre de la matriz a procesar para escribir archivo: ")
                    matriz = lista_matrices.buscar(nombre_matriz)
                    if matriz and matriz.matriz_reducida:
                        ruta_salida = input("Ingrese la ruta donde desea guardar el archivo XML de salida: ")
                        escribir_archivo_salida(matriz.matriz_reducida, ruta_salida)
                    else:
                        print("ERROR: No se ha procesado ninguna matriz o no se encontró la matriz especificada.")
                else:
                    print("ERROR: No se ha cargado ningún archivo.")
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
                if lista_matrices:
                    lista_matrices.mostrar()
                    nombre_matriz = input("Ingrese el nombre de la matriz para generar gráfica: ")
                    matriz = lista_matrices.buscar(nombre_matriz)
                    if matriz and matriz.matriz_reducida:
                        archivo_salida = input("Ingrese el nombre del archivo de salida para la gráfica: ")
                        generar_grafica_doble(matriz.matriz, matriz.matriz_reducida, archivo_salida)
                    else:
                        print("ERROR: No se ha procesado ninguna matriz o no se encontró la matriz especificada.")
                else:
                    print("ERROR: No se ha cargado ningún archivo.")
            case 6:
                print("Saliendo del programa...")
            case _:
                print("ERROR: Opción no válida")
                print(" ")

if __name__ == '__main__':
    main()
