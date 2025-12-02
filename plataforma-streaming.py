#TP de promoción
#asignatura: Estructuras de datos
#alumnos: Marcos Argüello, Lucas Vergara, Fiona Muñoz

#Area de clases y funciones
class PlataformaStreaming():
    def __init__(self):
        self.catalogo_series=Catalogo()
        self.arbol_series=ArbolSeries()
        self.catalogo_peliculas=Catalogo()
        self.usuarios=Usuarios()
        self.grafo = GrafoContenido()
        self.id_contenido = 0  # Para numerar los nodos del grafo
        self.grafo_episodios = GrafoEpisodios()

class Usuarios():
    def __init__(self):
        self.info=None
        self.sig=None
        self.tamaño=0

class Usuario():
    def __init__(self,nombre,edad,preferencias):
        self.nombre=nombre
        self.edad=edad
        self.preferencias=preferencias
        self.historial=[]
        self.sig=None

class Contenido():
    def __init__(self, pelicula, serie, titulo, genero, popularidad=0, likes=0):
        self.pelicula = pelicula
        self.serie = serie
        self.titulo = titulo
        self.temporadas = 0           
        self.episodios = []           
        self.duracion = 0             
        self.genero=genero
        self.popularidad = popularidad  # Aumenta cuando los usuarios lo ven
        self.likes = likes              # Aumenta según puntaje dado por usuarios
        self.comentarios = []           # Lista de comentarios de usuarios


class Catalogo():
    def __init__(self):
        self.contenido = None   # Nodo raíz
        self.izq = None
        self.der = None
        self.tamanio = 0

class NodoCatalogo:
    def __init__(self, contenido):
        self.contenido = contenido
        self.izq = None
        self.der = None

class GrafoContenido:
    def __init__(self):
        self.nodos = {}      # {id: Contenido}
        self.aristas = {}    # {id: [ids_relacionados]}

    def agregar_nodo(self, id_contenido, contenido):
        self.nodos[id_contenido] = contenido
        self.aristas[id_contenido] = []

    def agregar_relacion(self, id1, id2):
        if id1 in self.nodos and id2 in self.nodos:
            self.aristas[id1].append(id2)
            self.aristas[id2].append(id1)  # Conexión bidireccional

    def obtener_relacionados(self, id_contenido):
        return [self.nodos[id] for id in self.aristas.get(id_contenido, [])]

class GrafoEpisodios:
    def __init__(self):
        self.grafo = {}  # {episodio: [episodios_que_dependen_de_él]}

    def agregar_episodio(self, episodio):
        if episodio not in self.grafo:
            self.grafo[episodio] = []

    def agregar_dependencia(self, episodio1, episodio2):
        # episodio1 -> episodio2
        self.grafo[episodio1].append(episodio2)

class NodoSerie:
    def __init__(self, nombre):
        self.nombre = nombre
        self.hijos = []  # Temporadas y episodios


class ArbolSeries:
    def __init__(self):
        self.series = {}  # {titulo: nodo_raiz}

    def agregar_serie(self, titulo):
        self.series[titulo] = NodoSerie(titulo)
        return self.series[titulo]

    def agregar_temporada(self, titulo_serie, nombre_temporada):
        temporada = NodoSerie(nombre_temporada)
        self.series[titulo_serie].hijos.append(temporada)
        return temporada     

    def agregar_episodio(self, nodo_temporada, nombre_episodio):
        nodo_temporada.hijos.append(NodoSerie(nombre_episodio))


#Funciones para gestionar usuarios y contenido
def crear_contenido(plataforma):
    titulo=input("Ingrese el título del contenido: ").title()
    generos_disponibles=[[1,"Accion"],[2,"Animacion"] ,[3,"Ciencia Ficcion"] , [4,"Comedia"], [5,"Crimen"], [6,"Drama"], [7,"Fantasia"], [8,"Romance"], [9,"Suspenso"], [10,"Terror"]]
    generos=[]
    cantidad=int(input("Ingrese la cantidad de géneros que tiene el contenido(max. 3): "))
    while cantidad<1 or cantidad>3:
        cantidad=int(input("Cantidad inválida. Ingrese la cantidad de géneros que tiene el contenido(max. 3): "))
    for i in range(cantidad):
        for g in generos_disponibles:
            print(g)
        genero=int(input(f"Ingrese el género {i+1} del contenido: "))
        while genero <1 or genero>10:
            genero=int(input(f"Género inválido. Ingrese el género {i+1} del contenido: "))
        for g in generos_disponibles:
            if g[0]==genero:
                genero=g[1]
        generos.append(genero)
        for i in generos_disponibles:
            if i[1]==genero:
                generos_disponibles.remove(i)
    tipos="""
    1. Película
    2. Serie
    """
    print(tipos)
    tipo=int(input("Ingrese el tipo de contenido: "))
    while tipo not in [1,2]:
        print(tipos)
        tipo=int(input("Ingrese el tipo de contenido: "))
    if tipo==1:
        n_contenido=Contenido(pelicula=True,serie=False,titulo=titulo,genero=generos)
        dur=int(input("Ingrese la duración de la película(en minutos): "))
        n_contenido.duracion=dur
    else:
        n_contenido=Contenido(pelicula=False,serie=True,titulo=titulo,genero=generos)
        plataforma.arbol_series.agregar_serie(titulo)
        temp=int(input("Ingrese la cantidad de temporadas que tiene la serie: "))
        epi=int(input("Ingrese la cantidad de episodios que tiene cada temporada: "))
        for t in range(temp):
            n_temp=f"Temporada {t+1}"
            nodo_temporada = plataforma.arbol_series.agregar_temporada(titulo, n_temp)
            for e in range(epi):
                n_epi="Episodio "+str(e+1)
                plataforma.arbol_series.agregar_episodio(nodo_temporada, n_epi)
            n_contenido.temporadas+=1
    return n_contenido

def insertar_en_arbol(nodo, contenido):
    if nodo is None:
        nuevo = Catalogo()
        nuevo.contenido = contenido
        return nuevo

    if contenido.popularidad < nodo.contenido.popularidad:
        nodo.izq = insertar_en_arbol(nodo.izq, contenido)
    else:
        nodo.der = insertar_en_arbol(nodo.der, contenido)

    return nodo

def insertar_contenido(plataforma, contenido, tipo):
    if tipo == "serie":
        plataforma.catalogo_series.contenido = insertar_en_arbol(plataforma.catalogo_series.contenido, contenido)
        plataforma.catalogo_series.tamanio += 1
        plataforma.arbol_series.agregar_serie(contenido.titulo)
    else:
        plataforma.catalogo_peliculas.contenido = insertar_en_arbol(plataforma.catalogo_peliculas.contenido, contenido)
        plataforma.catalogo_peliculas.tamanio += 1
    # Agregar contenido al grafo
    plataforma.id_contenido += 1
    id_actual = plataforma.id_contenido
    plataforma.grafo.agregar_nodo(id_actual, contenido)
    # Crear relaciones con todo lo que tenga género en común
    for id_existente, cont_existente in plataforma.grafo.nodos.items():
        if id_existente != id_actual:
            if any(genero in cont_existente.genero for genero in contenido.genero):
                plataforma.grafo.agregar_relacion(id_actual, id_existente)

def navegar_series(plataforma, usuario=None):
    print("Series disponibles:")
    lista_titulos=list(plataforma.arbol_series.series.keys())
    if lista_titulos ==[]:
        print("No hay series registradas en la plataforma.")
        return
    for idx, titulo in enumerate(lista_titulos, start=1):
        print(f"{idx}. {titulo}")
    serie = int(input("Elija una serie: "))
    while serie not in range(1, len(lista_titulos)+1):
        print("Serie inexistente.")
        for idx, titulo in enumerate(lista_titulos, start=1):
            print(f"{idx}. {titulo}")
        serie = int(input("Elija una serie: "))
    nodo_serie = plataforma.arbol_series.series[lista_titulos[serie-1]]

    print("\nTemporadas:")
    if nodo_serie.hijos ==[]:
        print("No hay temporadas disponibles para esta serie.")
        return
    for idx, t in enumerate(nodo_serie.hijos, start=1):
        print(f"{idx}. {t.nombre}")
    temp_num = int(input("Seleccione temporada: "))
    while temp_num not in range(1, len(nodo_serie.hijos) + 1):
        print("Opción inválida")
        for idx, t in enumerate(nodo_serie.hijos, start=1):
            print(f"{idx}. {t.nombre}")
        temp_num = int(input("Seleccione temporada: "))

    nodo_temporada = nodo_serie.hijos[temp_num - 1]
    print("\nEpisodios:")
    if not nodo_temporada.hijos:
        print("No hay episodios disponibles para esta temporada.")
        return
    for idx, e in enumerate(nodo_temporada.hijos, start=1):
        print(f"{idx}. {e.nombre}")
    epi_num = int(input("Seleccione episodio: "))
    while epi_num not in range(1, len(nodo_temporada.hijos) + 1):
        print("Opción inválida")
        for idx, e in enumerate(nodo_temporada.hijos, start=1):
            print(f"{idx}. {e.nombre}")
        epi_num = int(input("Seleccione episodio: "))
    print(f"\n► Reproduciendo {nodo_temporada.hijos[epi_num - 1].nombre}...")
    # Buscamos el objeto Contenido en el grafo por título de la serie
    titulo_serie = lista_titulos[serie-1]
    serie_encontrada = None
    for idc, cont in plataforma.grafo.nodos.items():
        if cont.titulo == titulo_serie and cont.serie:
            serie_encontrada = cont
            break
    if serie_encontrada is not None and usuario is not None:
        ver_contenido(usuario, serie_encontrada)
        puntuar_contenido(serie_encontrada)
        agregar_comentario(serie_encontrada)
    
def crear_usuario():
    generos_validos = [[1,"Accion"],[2,"Animacion"] ,[3,"Ciencia Ficcion"] , [4,"Comedia"], [5,"Crimen"], [6,"Drama"], [7,"Fantasia"], [8,"Romance"], [9,"Suspenso"], [10,"Terror"]]
    n_nombre = input("Ingrese el nombre del usuario: ")
    n_edad = int(input("Ingrese la edad del usuario: "))
    for g in generos_validos:
        print(g)
    n_preferencias = int(input("Ingrese la cantidad de preferencias del usuario(max. 3): "))
    lista_preferencias = []
    while n_preferencias <1 or n_preferencias >3:
        print("Cantidad de preferencias inválida. Intente nuevamente.")
        for g in generos_validos:
            print(g)
        n_preferencias = int(input("Ingrese la cantidad de preferencias del usuario(max. 3): "))
    for p in range(n_preferencias):
        pref=int(input(f"Ingrese la preferencia N°{p+1}: "))
        while pref not in range(len(generos_validos)):
            print("Opción inválida")
            pref=int(input(f"Ingrese la preferencia N°{p+1}: "))
        for i in generos_validos:
            if i[0]==pref:
                genero_p=i[1]
                generos_validos.remove(i)
        lista_preferencias.append(genero_p)
        
    usuario = Usuario(n_nombre, n_edad, lista_preferencias)
    return usuario

def mostrar_datos_usuario(usuario):
    datos="Nombre: "+usuario.nombre+"\n"
    datos+="Edad: "+str(usuario.edad)+"\n"
    datos+="Preferencias: "+", ".join(usuario.preferencias)+"\n"
    datos+="Historial de visualización: "
    if usuario.historial is not None and len(usuario.historial)>0:
        datos+="\n- " + "\n- ".join(usuario.historial)+"\n"
    else:
        datos+="No hay historial de visualización.\n"
    return datos

def usuarios_existentes(plataforma):
    print("Usarios existentes:")
    usuarios=[]
    indice=1
    actual=plataforma.usuarios.info
    while actual is not None:
        usuario=[indice,actual.nombre]
        usuarios.append(usuario)
        actual=actual.sig
        indice+=1
    return usuarios

def obtener_usuario(plataforma, idc):
    """
    Devuelve el objeto Usuario correspondiente al índice (1-based) mostrado por usuarios_existentes.
    Retorna None si no existe.
    """
    actual = plataforma.usuarios.info
    contador = 1
    while actual is not None:
        if contador == idc:
            return actual
        actual = actual.sig
        contador += 1
    return None
    
def gestionar_usuarios(plataforma,usuario,accion):
    #si se desea agregar un usuario
    if accion=="agregar":
        if plataforma.usuarios.info is None:  # Corrección aquí
            plataforma.usuarios.info=usuario
        else:
            actual=plataforma.usuarios.info  # Y aquí
            while actual.sig is not None:
                actual=actual.sig
            actual.sig=usuario
        plataforma.usuarios.tamaño+=1
    #si se desea eliminar un usuario
    elif accion=="eliminar":
        actual=plataforma.usuarios.info
        previo=None
        while actual is not None and actual.nombre!=usuario.nombre:
            previo=actual
            actual=actual.sig
        if actual is not None:
            if previo is None:
                plataforma.usuarios.info=actual.sig
            else:
                previo.sig=actual.sig
            plataforma.usuarios.tamaño-=1
    #si se desea mostrar los datos del usuario
    else:
        actual=plataforma.usuarios.info
        while actual is not None:
            if actual.nombre==usuario.nombre:
                return mostrar_datos_usuario(actual)
            actual=actual.sig
        return None

#Funciones para interactuar con el contenido
def ver_contenido(usuario,contenido):
    usuario.historial.append(contenido.titulo)
    contenido.popularidad+=1

def puntuar_contenido(contenido):
    pregunta=int(input("Ingrese su puntuación del 1 al 10: "))
    if 1<=pregunta<=10:
        contenido.likes+=pregunta
    else:
        print("Puntuación inválida.")

def agregar_comentario(contenido):
    comentario=input("Ingrese su comentario: ")
    contenido.comentarios.append(comentario)

#Función para mostrar el catálogo
def recorrer_inorder(nodo, lista):
    if nodo is not None:
        recorrer_inorder(nodo.izq, lista)
        lista.append(nodo.contenido.titulo + "- Popularidad: " + str(nodo.contenido.popularidad))
        recorrer_inorder(nodo.der, lista)
    return lista

def recorrer_inorder_obj(nodo, lista):
    """
    Recorre el árbol inorder y agrega los objetos Contenido a la lista (no strings).
    """
    if nodo is not None:
        recorrer_inorder_obj(nodo.izq, lista)
        lista.append(nodo.contenido)
        recorrer_inorder_obj(nodo.der, lista)
    return lista

def mostrar_catalogo(plataforma, tipo):
    lista_ordenada = []
    if tipo == "serie":
        if plataforma.catalogo_series.contenido is None:
            return None
        recorrer_inorder(plataforma.catalogo_series.contenido, lista_ordenada)
    else:
        if plataforma.catalogo_peliculas.contenido is None:
            return None
        recorrer_inorder(plataforma.catalogo_peliculas.contenido, lista_ordenada)
    resultado = []
    indice = 1
    for item in lista_ordenada:
        cont=[indice,item]
        resultado.append(cont)
        indice =indice+ 1
    return resultado

#funcion para buscar contenido segun preferencias (de forma recursiva)
def buscar_contenido(preferencia, catalogo, tipo):
    """
    Busca contenido en un árbol (Catalogo nodo) según la preferencia de género.
    catalogo: una instancia de Catalogo (nodo) o None.
    """
    resultados = []
    # Caso base: nodo vacío
    if catalogo is None:
        return resultados
    # Si el nodo contiene contenido, chequear y recorrer subárboles
    if catalogo.contenido is not None:
        if preferencia in catalogo.contenido.genero:
            resultados.append(catalogo.contenido)
    # Recorremos recursivamente
    resultados += buscar_contenido(preferencia, catalogo.izq, tipo)
    resultados += buscar_contenido(preferencia, catalogo.der, tipo)
    return resultados

#funcion para clasificar contenido segun popularidad (de forma recursiva)
def clasificar_contenido(contenido):
    resultado=[]
    if contenido == []:
        return []  # caso base: lista vacía
    else:# quitamos el de mayor popularidad
        mayor_popularidad = -1
        indice_mayor = None
        for i in range(len(contenido)):
            if contenido[i].popularidad > mayor_popularidad:
                mayor_popularidad = contenido[i].popularidad
                indice_mayor = i
        resultado.append(contenido[indice_mayor])
        contenido.pop(indice_mayor)
        # Recursión para clasificar el resto
        resultado +=clasificar_contenido(contenido)
    return resultado

def generar_recomendaciones(plataforma,tipo):
    if tipo=="serie":
        todas_series=[]
        recorrer_inorder_obj(plataforma.catalogo_series.contenido,todas_series)
        # clasificar_contenido muta la lista, pasar copia para no afectar otras listas
        series_ordenadas=clasificar_contenido(todas_series.copy())
        return series_ordenadas[:5]
    else:
        todas_peliculas=[]
        recorrer_inorder_obj(plataforma.catalogo_peliculas.contenido,todas_peliculas)
        peliculas_ordenadas=clasificar_contenido(todas_peliculas.copy())
        return peliculas_ordenadas[:5]

def recomendar_por_grafo(plataforma, contenido):
    for id_cont, cont in plataforma.grafo.nodos.items():
        if cont == contenido:
            relacionados = plataforma.grafo.obtener_relacionados(id_cont)
            return [c.titulo for c in relacionados][:5]  # Máx. 5 recomendaciones
    return []

def dfs_grafo(plataforma, nodo_inicial, visitado=None):
    if visitado is None:
        visitado = set()

    if nodo_inicial not in visitado:
        visitado.add(nodo_inicial)
        print(plataforma.grafo.nodos[nodo_inicial].titulo)  # Mostrar película o serie

        for vecino in plataforma.grafo.aristas[nodo_inicial]:
            if vecino not in visitado:
                dfs_grafo(plataforma, vecino, visitado)

def bfs_grafo(plataforma, nodo_inicial):
    visitado = set()
    cola = [nodo_inicial]

    while cola !=[]:
        nodo_actual = cola.pop(0)
        if nodo_actual not in visitado:
            visitado.add(nodo_actual)
            print(plataforma.grafo.nodos[nodo_actual].titulo)  # Mostrar película o serie

            for vecino in plataforma.grafo.aristas[nodo_actual]:
                if vecino not in visitado:
                    cola.append(vecino)

def dfs_topologico(nodo, grafo, visitado, pila):
    visitado.add(nodo)
    for vecino in grafo[nodo]:
        if vecino not in visitado:
            dfs_topologico(vecino, grafo, visitado, pila)
    pila.append(nodo)

def ordenamiento_topologico(grafo):
    visitado = set()
    pila = []

    for nodo in grafo:
        if nodo not in visitado:
            dfs_topologico(nodo, grafo, visitado, pila)

    return pila[::-1]

# Programa principal
plataforma=PlataformaStreaming()
usuario1=Usuario("Alice",25,["Ciencia Ficcion","Drama"])
usuario2=Usuario("Bob",30,["Accion","Comedia"])
usuario3=Usuario("Charlie",28,["Suspenso","Terror"])
gestionar_usuarios(plataforma,usuario1,"agregar")
gestionar_usuarios(plataforma,usuario2,"agregar")
gestionar_usuarios(plataforma,usuario3,"agregar")

pelicula1=Contenido(pelicula=True,serie=False,titulo="Inception",genero=["Ciencia Ficcion","Accion"])
pelicula2=Contenido(pelicula=True,serie=False,titulo="The Godfather",genero=["Crimen","Drama"])
pelicula3=Contenido(pelicula=True,serie=False,titulo="Matrix",genero=["Ciencia Ficcion","Accion"])
pelicula4=Contenido(pelicula=True,serie=False,titulo="John Wick",genero=["Accion","Crimen"])
serie1=Contenido(pelicula=False,serie=True,titulo="Stranger Things",genero=["Ciencia Ficcion","Suspenso"])
serie2=Contenido(pelicula=False,serie=True,titulo="Breaking Bad",genero=["Crimen","Drama"])
serie3=Contenido(pelicula=False,serie=True,titulo="Heartstopper",genero=["Romance","Drama"])
serie4=Contenido(pelicula=False,serie=True,titulo="The witcher",genero=["Fantasia","Drama"])
plataforma.arbol_series.agregar_serie(serie1.titulo)
plataforma.arbol_series.agregar_serie(serie2.titulo)
plataforma.arbol_series.agregar_serie(serie3.titulo)
plataforma.arbol_series.agregar_serie(serie4.titulo)
cant_temp_general=5
cant_epi_general=10
for t in range(cant_temp_general):
    titulo_temp="Temporada "+str(t+1)
    nodo_temp1 = plataforma.arbol_series.agregar_temporada(serie1.titulo,titulo_temp)
    nodo_temp2 = plataforma.arbol_series.agregar_temporada(serie2.titulo,titulo_temp)
    nodo_temp3 = plataforma.arbol_series.agregar_temporada(serie3.titulo,titulo_temp)
    nodo_temp4 = plataforma.arbol_series.agregar_temporada(serie4.titulo,titulo_temp)
    for e in range(cant_epi_general):
        titulo_epi="Episodio "+str(e+1)
        plataforma.arbol_series.agregar_episodio(nodo_temp1,titulo_epi)
        plataforma.arbol_series.agregar_episodio(nodo_temp2,titulo_epi)
        plataforma.arbol_series.agregar_episodio(nodo_temp3,titulo_epi)
        plataforma.arbol_series.agregar_episodio(nodo_temp4,titulo_epi)

insertar_contenido(plataforma,pelicula1,"pelicula")
insertar_contenido(plataforma,pelicula2,"pelicula")
insertar_contenido(plataforma,pelicula3,"pelicula")
insertar_contenido(plataforma,pelicula4,"pelicula")
insertar_contenido(plataforma,serie1,"serie")
insertar_contenido(plataforma,serie2,"serie")
insertar_contenido(plataforma,serie3,"serie")
insertar_contenido(plataforma,serie4,"serie")

print("Bienvenido a la plataforma de streaming WonderlandTV.")
menu="""
Por favor, seleccione una opción:
1.gestionar usuarios
2.gestionar contenido
3.Acceder como un usuario
4.salir
"""
print(menu)
opcion=int(input())
while opcion not in [1,2,3,4]:
    print("Opción inválida.")
    print(menu)
    opcion=int(input())
while opcion != 4:
    if opcion==1:
        menu_usuarios="""
        Gestión de usuarios:
        1.Agregar usuario
        2.Eliminar usuario
        3.Mostrar datos de usuario
        4.Atrás
        """
        print(menu_usuarios)
        opcion_usuario=int(input())
        while opcion_usuario not in [1,2,3,4]:
            print(menu_usuarios)
            print("Opción inválida.")
            opcion_usuario=int(input())
        while opcion_usuario != 4:
            if opcion_usuario==1:
                nuevo_usuario=crear_usuario()
                gestionar_usuarios(plataforma,nuevo_usuario,"agregar")
            elif opcion_usuario==2:
                usuarios_existentes(plataforma)
                nombre_eliminar=input("Ingrese el nombre del usuario a eliminar: ")
                usuario_eliminar=Usuario(nombre_eliminar,0,[])
                gestionar_usuarios(plataforma,usuario_eliminar,"eliminar")
            elif opcion_usuario==3:
                usuarios_existentes(plataforma)
                nombre_mostrar=input("Ingrese el nombre del usuario a mostrar: ")
                usuario_mostrar=Usuario(nombre_mostrar,0,[])
                datos=gestionar_usuarios(plataforma,usuario_mostrar,"mostrar")
                if datos is not None:
                    print(datos)
                else:
                    print("Usuario no encontrado.")
            print(menu_usuarios)
            opcion_usuario=int(input())
            while opcion_usuario not in [1,2,3,4]:
                print(menu_usuarios)
                print("Opción inválida.")
                opcion_usuario=int(input())
    elif opcion==2:
        menu_contenido="""
        Gestión de contenido:
        1.Agregar contenido
        2.Ver catálogo
        3.Atrás    
        """
        print(menu_contenido)
        opcion_contenido=int(input())
        while opcion_contenido not in [1,2,3]:
            print(menu_contenido)
            print("Opción inválida.")
            opcion_contenido=int(input())
        while opcion_contenido != 3:
            if opcion_contenido==1:
                nuevo_contenido=crear_contenido(plataforma)
                if nuevo_contenido.pelicula==True:
                    tipo="pelicula"
                else:
                    tipo="serie"
                insertar_contenido(plataforma,nuevo_contenido,tipo)
                print("Nuevo contenido disponible para los usuarios")
            elif opcion_contenido==2:
                tipo_catalogo=input("Ingrese el tipo de catálogo a mostrar (serie o película): ")
                while tipo_catalogo not in ["serie","pelicula"]:
                    tipo_catalogo=input("Tipo inválido. Ingrese el tipo de catálogo a mostrar (serie o película): ")
                catalogo=mostrar_catalogo(plataforma,tipo_catalogo)
                if not catalogo:
                    print(f"No hay {tipo_catalogo}s en el catálogo.")
                else:
                    print(f"Catálogo de {tipo_catalogo}s:")
                    for idx, item in catalogo:
                        print(f"{idx}. {item}")
            print(menu_contenido)
            opcion_contenido=int(input())
            while opcion_contenido not in [1,2,3]:
                print(menu_contenido)
                print("Opción inválida.")
                opcion_contenido=int(input())
    elif opcion==3:
        us_ex=usuarios_existentes(plataforma)
        if us_ex==[]:
            print("No hay usuarios registrados. Por favor, cree al menos un usuario primero.")
        for u in us_ex:
            print(f"{u[0]} {u[1]}")
        op=int(input("Ingrese una opción: "))
        valid_indices = [u[0] for u in us_ex]
        while op not in valid_indices:
            print("Opción inválida")
            us_ex=usuarios_existentes(plataforma)
            for u in us_ex:
                print(f"{u[0]} {u[1]}")
            op=int(input("Ingrese una opción: "))
        usuario_actual = obtener_usuario(plataforma, op)
        if usuario_actual is not None:
            print("Bienvenido, "+usuario_actual.nombre+"!")
            menu_usuario="""
            Gestión de usuario:
            1.Ver catálogo según preferencias
            2.Ver historial
            3.Generar recomendaciones
            4.Ver peliculas o series
            5.Atrás
            """
            print(menu_usuario)
            opcion_usuario=int(input())
            while opcion_usuario not in [1,2,3,4,5]:
                print("Opción inválida.")
                print(menu_usuario)
                opcion_usuario=int(input())
            while opcion_usuario !=5:
                if opcion_usuario==1:
                    for preferencia in usuario_actual.preferencias:
                        resultados_series=buscar_contenido(preferencia,plataforma.catalogo_series.contenido,"serie")
                        resultados_peliculas=buscar_contenido(preferencia,plataforma.catalogo_peliculas.contenido,"pelicula")
                        print("Resultados para la preferencia '"+preferencia+"':")
                        print("Series:")
                        for serie in resultados_series:
                            print("- "+serie.titulo)
                        print("Películas:")
                        for pelicula in resultados_peliculas:
                            print("- "+pelicula.titulo)
                elif opcion_usuario==2:
                    if not usuario_actual.historial:
                        print("No hay historial de visualización.")
                    else:
                        print("Historial de visualización:")
                        for titulo in usuario_actual.historial:
                            print("- "+titulo)
                elif opcion_usuario==3:
                    menu_recomendaciones="""
                    1.Ver recomendaciones basadas en contenido similar
                    2.Buscar recomendaciones en base a lo último visto
                    3.Explorar contenido relacionado
                    4.Atrás
                    """
                    print(menu_recomendaciones)
                    opcion_recomendaciones=int(input())
                    while opcion_recomendaciones not in [1,2,3,4]:
                        print("Opción inválida")
                        print(menu_recomendaciones)
                        opcion_recomendaciones=int(input())
                    while opcion_recomendaciones != 4:
                        if opcion_recomendaciones==1:
                            print("Recomendaciones basadas en contenido similar:")
                            series_ordenadas = generar_recomendaciones(plataforma, "serie")
                            peliculas_ordenadas = generar_recomendaciones(plataforma, "pelicula")
                            print("Recomendaciones de series:")
                            for serie in series_ordenadas[:5]:
                                print("- "+serie.titulo)
                            print("Recomendaciones de películas:")
                            for pelicula in peliculas_ordenadas[:5]:
                                print("- "+pelicula.titulo)
                        elif opcion_recomendaciones ==2:
                            # Revisar historial antes de acceder al último visto
                            if not usuario_actual.historial:
                                print("No hay historial de visualización. Mire algo primero para obtener recomendaciones basadas en lo último visto.")
                            else:
                                ultimo_visto = usuario_actual.historial[-1]
                                # Buscar el nodo en el grafo por título
                                for idc, cont in plataforma.grafo.nodos.items():
                                    if cont.titulo==ultimo_visto:
                                        dfs_grafo(plataforma,idc)
                        elif opcion_recomendaciones==3:
                            # Revisar historial antes de explorar contenido relacionado
                            if usuario_actual.historial == []:
                                print("No hay historial de visualización. Mire algo primero para explorar contenido relacionado.")
                            else:
                                print("Contenido relacionado")
                                ultimo_visto=usuario_actual.historial[-1]
                                for idc,cont in plataforma.grafo.nodos.items():
                                    if cont.titulo==ultimo_visto:
                                        bfs_grafo(plataforma,idc)
                        print(menu_recomendaciones)
                        opcion_recomendaciones=int(input())
                elif opcion_usuario==4:
                    menu_peli_serie="""
                    1.Ver catálogo de películas
                    2.Ver catálogo de series
                    3.Atrás
                    """
                    print(menu_peli_serie)
                    opcion_peli_serie=int(input())
                    while opcion_peli_serie not in [1,2,3]:
                        print("Opción inválida.")
                        print(menu_peli_serie)
                        opcion_peli_serie=int(input())
                    while opcion_peli_serie in [1,2]:
                        if opcion_peli_serie==1:
                            catalogo=mostrar_catalogo(plataforma,"pelicula")
                            if catalogo is None:
                                print("No hay películas en el catálogo.")
                            else:
                                print("Catálogo de películas:")
                                for idx, item in catalogo:
                                    print(f"{idx}. {item}")
                            print("¿Qué película le gustaría ver?")
                            opcion_pelicula=int(input())
                            while opcion_pelicula not in range(1,len(catalogo)+1):
                                print("Película no encontrada en el catálogo.")
                                catalogo=mostrar_catalogo(plataforma,"pelicula")
                                if not catalogo:
                                    print("No hay películas en el catálogo.")
                                else:
                                    print("Catálogo de películas:")
                                    for idx, item in catalogo:
                                        print(f"{idx}. {item}")
                                print("¿Qué película le gustaría ver?")
                                opcion_pelicula=int(input())
                            # Buscar la película en el catálogo
                            pelicula_encontrada=None
                            for i in range(len(catalogo)):
                                if catalogo[i][0]==opcion_pelicula:
                                    titulo_buscar=catalogo[i][1].split("-")[0].strip()
                                    for idc, cont in plataforma.grafo.nodos.items(): 
                                        if cont.titulo == titulo_buscar and cont.pelicula:
                                            pelicula_encontrada=cont
                            if pelicula_encontrada is not None:
                                ver_contenido(usuario_actual,pelicula_encontrada)
                                print(f"Disfrutando de '{pelicula_encontrada.titulo}'...")
                                puntuar_contenido(pelicula_encontrada)
                                agregar_comentario(pelicula_encontrada)
                        elif opcion_peli_serie==2:
                            navegar_series(plataforma, usuario_actual)
                        print(menu_peli_serie)
                        opcion_peli_serie=int(input())
                        while opcion_peli_serie not in [1,2,3]:
                            print("Opción inválida.")
                            print(menu_peli_serie)
                            opcion_peli_serie=int(input())
                print(menu_usuario)
                opcion_usuario=int(input())
                while opcion_usuario not in [1,2,3,4,5]:
                    print("Opción inválida.")
                    print(menu_usuario)
                    opcion_usuario=int(input())
    print(menu)
    opcion=int(input())
    while opcion not in [1,2,3,4]:
        print("Opción inválida.")
        print(menu)
        opcion=int(input())
print("Gracias por usar WonderlandTV. ¡Hasta luego!")


