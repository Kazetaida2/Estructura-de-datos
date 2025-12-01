def dfs(nodo, grafo, visitado, pila):
    visitado.append(nodo)  #marca al nodo como visitado
    for vecino in grafo[nodo]:#recorre los vecinos
        if vecino not in visitado:# si el vecino no fue vistado
            dfs(vecino, grafo, visitado, pila)
    pila.append(nodo)  

def ordenamiento_topologico_dfs(grafo):
    visitado = []  #lista 
    pila = [] #aca va el orden topologico

    for nodo in grafo: #aca revisa cada nodo
        if nodo not in visitado:
            dfs(nodo, grafo, visitado, pila)

    return pila[::-1]  


grafo = {
    'hp la piedra filosofal': ['hp la cámara secreta'],
    'hp la cámara secreta': ['hp el prisionero de azkaban'],
    'hp el prisionero de azkaban': [],
}

resultado = ordenamiento_topologico_dfs(grafo)
print("Ordenamiento topológico (harry potter):", resultado)
