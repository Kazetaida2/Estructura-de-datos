class Peliculas:
    def __init__(self):
        self.nodos = {}
        self.aristas = {}

    def agregar_nodo(self, id_pelicula, nombre, actor, genero):
        self.nodos[id_pelicula] = {"nombre": nombre, "actor": actor, "genero": genero}
        self.aristas[id_pelicula] = []

    def agregar_arista(self, id_pelicula1, id_pelicula2):
        if id_pelicula1 in self.aristas and id_pelicula2 in self.nodos:
            self.aristas[id_pelicula1].append(id_pelicula2)
            self.aristas[id_pelicula2].append(id_pelicula1)
            #tengo entendido que asi hace conexion bidireccional


    def mostrar_grafo(self):
        for id_pelicula in self.nodos:
            actor = self.nodos[id_pelicula]["actor"]
            genero = self.nodos[id_pelicula]["genero"]
            conexiones = self.aristas[id_pelicula]
            print(f"Película: {self.nodos[id_pelicula]['nombre']}, Actor: {actor}, Género: {genero}, Conexiones: {conexiones}")


grafo = Peliculas()
grafo.agregar_nodo(1, "Viaje al futuro", "Actor A", "Ciencia Ficción")
grafo.agregar_nodo(2, "Matrix", "Keanu Reeves", "Ciencia Ficción")
grafo.agregar_nodo(3, "John Wick", "Keanu Reeves", "Acción")


grafo.agregar_arista(2, 3)  
grafo.agregar_arista(2, 1)  

grafo.mostrar_grafo()
