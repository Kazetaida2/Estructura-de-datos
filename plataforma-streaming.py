#TP de promoción
#asignatura: Estructuras de datos
#alumnos: Marcos Argüello, Lucas Vergara, Fiona Muñoz

#Area de clases y funciones
class PlataformaStreaming():
    def __init__(self):
        self.catalogo_series=Catalogo()
        self.catalogo_peliculas=Catalogo()
        self.usuarios=Usuarios()
        self.grafo = GrafoContenido()
        self.id_contenido = 0  # Para numerar los nodos del grafo


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
    def __init__(self, pelicula, serie, titulo, genero=None, popularidad=0, likes=0):
        self.pelicula = pelicula
        self.serie = serie
        self.titulo = titulo
        self.temporadas = 0           
        self.episodios = []           
        self.duracion = 0             
        if genero:
            self.genero = genero
        else:
            self.genero = ["Accion", "Animacion", "Ciencia Ficcion", "Comedia", "Crimen", "Drama", "Fantasia", "Romance", "Suspenso", "Terror"]
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

#Funciones para gestionar usuarios y contenido
def crear_contenido():
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
    tipo=input("Ingrese el tipo de contenido (serie o película): ")
    
    tipo = tipo.strip().lower()
    if tipo in ["pelicula","película"]:
        tipo = "pelicula"
    while tipo not in ["serie","pelicula"]:
        tipo=input("Tipo inválido. Ingrese el tipo de contenido (serie o película): ")
    if tipo=="pelicula":
        n_contenido=Contenido(pelicula=True,serie=False,titulo=titulo,genero=generos)
    else:
        tipo="serie"
        n_contenido=Contenido(pelicula=False,serie=True,titulo=titulo,genero=generos)
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


def crear_usuario():
    generos_validos = ["Accion", "Animacion", "Ciencia Ficcion", "Comedia", "Crimen", "Drama", "Fantasia", "Romance", "Suspenso", "Terror"]
    n_nombre = input("Ingrese el nombre del usuario: ")
    n_edad = int(input("Ingrese la edad del usuario: "))
    n_preferencias = input("Ingrese las preferencias del usuario (separadas por comas): ")
    lista_preferencias = [p.strip().title() for p in n_preferencias.split(",")]
    while not all(pref in generos_validos for pref in lista_preferencias):
        print("Preferencia o sintaxis inválidas. Intente nuevamente.")
        n_preferencias = input("Ingrese las preferencias del usuario (separadas por comas): ")
        lista_preferencias = [p.strip().title() for p in n_preferencias.split(",")]
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
    actual=plataforma.usuarios.info
    while actual is not None:
        print("- "+actual.nombre)
        actual=actual.sig
    
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
    resultado = ""
    for item in lista_ordenada:
        resultado = resultado + item + "\n"
    
    return resultado

#funcion para buscar contenido segun preferencias (de forma recursiva)
def buscar_contenido(preferencia, catalogo, tipo):
    """
    Busca contenido en un árbol (Catalogo node) según la preferencia de género.
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
serie1=Contenido(pelicula=False,serie=True,titulo="Stranger Things",genero=["Ciencia Ficcion","Suspenso"])
serie2=Contenido(pelicula=False,serie=True,titulo="Breaking Bad",genero=["Crimen","Drama"])
insertar_contenido(plataforma,pelicula1,"pelicula")
insertar_contenido(plataforma,pelicula2,"pelicula")
insertar_contenido(plataforma,serie1,"serie")
insertar_contenido(plataforma,serie2,"serie")

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
        opcion_usuario=int(input(menu_usuarios))
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
        elif opcion_usuario==4:
            pass  # Volver al menú principal
        else:
            print("Opción inválida.")
    elif opcion==2:
        menu_contenido="""
        Gestión de contenido:
        1.Agregar contenido
        2.Ver catálogo
        3.Atrás    
        """
        opcion_contenido=int(input(menu_contenido))
        if opcion_contenido==1:
            nuevo_contenido=crear_contenido()
            tipo=nuevo_contenido.serie and "serie" or "pelicula"
            insertar_contenido(plataforma,nuevo_contenido,tipo)
        elif opcion_contenido==2:
            tipo_catalogo=input("Ingrese el tipo de catálogo a mostrar (serie o película): ")
            while tipo_catalogo not in ["serie","pelicula"]:
                tipo_catalogo=input("Tipo inválido. Ingrese el tipo de catálogo a mostrar (serie o película): ")
            catalogo=mostrar_catalogo(plataforma,tipo_catalogo)
            print("Catálogo de "+tipo_catalogo+"s:\n"+catalogo)
        elif opcion_contenido==3:
            pass  # Volver al menú principal
        else:
            print("Opción inválida.")
    elif opcion==3:
        usuarios_existentes(plataforma)
        nombre_usuario=input("Ingrese su nombre de usuario: ")
        actual=plataforma.usuarios.info
        usuario_actual=None
        while actual is not None:
            if actual.nombre==nombre_usuario:
                usuario_actual=actual
            actual=actual.sig
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
                if usuario_actual.historial is None:
                    print("No hay historial de visualización.")
                else:
                    print("Historial de visualización:")
                    for titulo in usuario_actual.historial:
                        print("- "+titulo)
            elif opcion_usuario==3:
                series_ordenadas = generar_recomendaciones(plataforma, "serie")
                peliculas_ordenadas = generar_recomendaciones(plataforma, "pelicula")
                print("Recomendaciones de series:")
                for serie in series_ordenadas[:5]:
                    print("- "+serie.titulo)
                print("Recomendaciones de películas:")
                for pelicula in peliculas_ordenadas[:5]:
                    print("- "+pelicula.titulo)
                print("Recomendaciones basadas en contenido similar:")
                for item in usuario_actual.historial:
                    # Buscamos el contenido real con ese título
                    for idc, cont in plataforma.grafo.nodos.items():
                        if cont.titulo == item:
                            recomendaciones = recomendar_por_grafo(plataforma, cont)
                            print(f"A partir de '{item}': {', '.join(recomendaciones)}")
            elif opcion_usuario==4:
                menu_peli_serie="""
                1.Ver catálogo de películas
                2.Ver catálogo de series
                3.Atrás
                """
                print(menu_peli_serie)
                opcion_peli_serie=int(input())
                if opcion_peli_serie==1:
                    catalogo=mostrar_catalogo(plataforma,"pelicula")
                    print("Catálogo de películas:\n"+catalogo)
                    print("¿Qué película le gustaría ver?")
                    opcion_pelicula=input()
                    if opcion_pelicula not in catalogo:
                        print("Película no encontrada en el catálogo.")
                        catalogo=mostrar_catalogo(plataforma,"pelicula")
                        print("Catálogo de películas:\n"+catalogo)
                        print("¿Qué película le gustaría ver?")
                        opcion_pelicula=input()
                    # Buscar la película en el catálogo
                    pelicula_encontrada=None
                    while pelicula_encontrada is None:
                        for idc, cont in plataforma.grafo.nodos.items(): 
                            if cont.titulo == opcion_pelicula and cont.pelicula:
                                pelicula_encontrada=cont
                    if pelicula_encontrada is not None:
                        ver_contenido(usuario_actual,pelicula_encontrada)
                        print(f"Disfrutando de '{pelicula_encontrada.titulo}'...")
                        puntuar_contenido(pelicula_encontrada)
                        agregar_comentario(pelicula_encontrada)
                elif opcion_peli_serie==2:
                    catalogo=mostrar_catalogo(plataforma,"serie")
                    print("Catálogo de series:\n"+catalogo)
                    print("¿Qué serie le gustaría ver?")
                    opcion_serie=input()
                    # Buscar la serie en el catálogo
                    if opcion_serie not in catalogo:
                        print("Serie no encontrada en el catálogo.")
                        catalogo=mostrar_catalogo(plataforma,"serie")
                        print("Catálogo de series:\n"+catalogo)
                        print("¿Qué serie le gustaría ver?")
                        opcion_serie=input()
                    serie_encontrada=None
                    while serie_encontrada is None:
                        for idc, cont in plataforma.grafo.nodos.items(): 
                            if cont.titulo == opcion_serie and cont.serie:
                                serie_encontrada=cont
                    if serie_encontrada is not None:
                        ver_contenido(usuario_actual,serie_encontrada)
                        print(f"Disfrutando de '{serie_encontrada.titulo}'...")
                        puntuar_contenido(serie_encontrada)
                        agregar_comentario(serie_encontrada)
                elif opcion_peli_serie==3:
                    pass  # Volver al menú principal
                else:
                    print("Opción inválida.")
            elif opcion_usuario==5:
                pass  # Volver al menú principal
        else:
            print("Usuario no encontrado.")
    print(menu)
    opcion=int(input())
    while opcion not in [1,2,3,4]:
        print("Opción inválida.")
        print(menu)
        opcion=int(input())
print("Gracias por usar WonderlandTV. ¡Hasta luego!")


