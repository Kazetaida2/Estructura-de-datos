X=input("ingrese genero a buscar: ")
grafo = {
    '1': ['viaje al futuro', 'michael j', 'ciencia ficcion'],
    '2': ['matrix', 'keanu reeves', 'ciencia ficcion'],
    '3': ['john wick', 'keanu reeves', 'accion']
}

visitado = set()

def dfs_recursiva(visitado, grafo, nodo):
    if nodo not in visitado:
        # Solo imprimir si el nodo es de ciencia ficción
        if X in grafo[nodo]:
        #if 'ciencia ficcion' in grafo[nodo]:
            print(grafo[nodo][0])  # Imprimir el título de la película
        visitado.add(nodo)
        for vecino in grafo:
            if vecino not in visitado:
                dfs_recursiva(visitado, grafo, vecino)

print("Recorrido DFS recursivo (películas de ciencia ficción):")
dfs_recursiva(visitado, grafo, '1')
