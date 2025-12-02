import heapq

def dijkstra(grafo, nodo_origen):
    #inicicalizar las distancias, acá pone en infinito
    distancias = {nodo: float('inf') for nodo in grafo}
    distancias[nodo_origen] = 0

    cola_prioridad = [(0, nodo_origen)]# (peso, nodo)

    #rastrea la rutas mas corta

    rutas = {nodo: [] for nodo in grafo}
    rutas[nodo_origen] = [nodo_origen]

    while cola_prioridad:
        distancia_Actual, nodo_actual = heapq.heappop(cola_prioridad)
        #si la distancia es mayor se ignora
        if distancia_Actual > distancias[nodo_actual]:
            continue


        #verifica los vecinos del nodo actual 
        for vecino, peso in grafo[nodo_actual].items():
            distancia = distancia_Actual + peso


            #si encuentra una distancia menor, la actualizamos 
            if distancia < distancias[vecino]:
                distancias[vecino] = distancia
                heapq.heappush(cola_prioridad, (distancia, vecino))


                #actualiza la ruta
                rutas[vecino] = rutas[nodo_actual] + [vecino]
    return distancias, rutas


grafo = {
    'A': {'B': 1, 'C': 4},
    'B': {'A': 1, 'C': 2, 'D': 5},
    'C': {'A': 4, 'B': 2},
    'D': {'B': 5}
}

# Ejecución del algoritmo
nodo_inicio = 'A'
distancias = dijkstra(grafo, nodo_inicio)

# Mostrar resultados
print(f"Distancias desde el nodo {nodo_inicio}: {distancias}")
