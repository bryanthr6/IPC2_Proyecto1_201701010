import graphviz

def generar_grafica_doble(matriz_original, matriz_reducida, nombre_archivo):
    dot = graphviz.Digraph(comment=f'{matriz_original.nombre} y {matriz_reducida.nombre}')
    
    # Subgrafo para la matriz original
    with dot.subgraph(name='cluster_original') as c:
        c.attr(label=f'{matriz_original.nombre} (Matriz Original)')
        c.node('matriz_original', 'Matriz Original', shape='ellipse')  # Cambiado a "Matriz Original"
        c.node('matriz_seleccionada', matriz_original.nombre, shape='ellipse')
        c.edge('matriz_original', 'matriz_seleccionada')

        c.node('n_filas', f'n={matriz_original.n}', shape='doublecircle', color='red')
        c.node('m_columnas', f'm={matriz_original.m}', shape='doublecircle', color='red')
        c.edge('matriz_seleccionada', 'n_filas')
        c.edge('matriz_seleccionada', 'm_columnas')

        for fila in range(1, matriz_original.n + 1):
            for col in range(1, matriz_original.m + 1):
                valor = matriz_original.obtener_dato(fila, col)
                nodo_id = f'valor_original_{fila}_{col}'
                c.node(nodo_id, str(valor), shape='circle')
                
                if fila == 1:
                    c.edge('matriz_seleccionada', nodo_id)
                else:
                    nodo_anterior = f'valor_original_{fila-1}_{col}'
                    c.edge(nodo_anterior, nodo_id)
    
    # Subgrafo para la matriz reducida
    with dot.subgraph(name='cluster_reducida') as c:
        c.attr(label=f'{matriz_reducida.nombre} (Matriz Reducida)')
        c.node('matriz_reducida', 'Matriz Reducida', shape='ellipse')  # Cambiado a "Matriz Reducida"
        c.node('matriz_reducida_seleccionada', matriz_reducida.nombre, shape='ellipse')
        c.edge('matriz_reducida', 'matriz_reducida_seleccionada')

        c.node('n_filas_reducida', f'n={matriz_reducida.n}', shape='doublecircle', color='red')
        c.node('m_columnas_reducida', f'm={matriz_reducida.m}', shape='doublecircle', color='red')
        c.edge('matriz_reducida_seleccionada', 'n_filas_reducida')
        c.edge('matriz_reducida_seleccionada', 'm_columnas_reducida')

        for fila in range(1, matriz_reducida.n + 1):
            for col in range(1, matriz_reducida.m + 1):
                valor = matriz_reducida.obtener_dato(fila, col)
                nodo_id = f'valor_reducida_{fila}_{col}'
                c.node(nodo_id, str(valor), shape='circle')
                
                if fila == 1:
                    c.edge('matriz_reducida_seleccionada', nodo_id)
                else:
                    nodo_anterior = f'valor_reducida_{fila-1}_{col}'
                    c.edge(nodo_anterior, nodo_id)
    
    # Guardar y renderizar el archivo
    dot.render(f'{nombre_archivo}.gv', view=True, format='png')

    print(f"Gráfica doble generada en {nombre_archivo}.gv.png")
