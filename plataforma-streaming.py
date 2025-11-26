#TP de promoción
#asignatura: Estructuras de datos
#alumnos: Marcos Argüello, Lucas Vergara, Fiona Muñoz

#Area de clases y funciones
class PlataformaStreaming():
    def __init__(self):
        self.catalogo_series=Catalogo()
        self.catalogo_peliculas=Catalogo()
        self.usuarios=Usuarios()

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

#Funciones para gestionar usuarios y contenido
def crear_contenido():
    titulo=input("Ingrese el título del contenido: ")
    genero=input("Ingrese el género del contenido (separados por comas): ")
    while genero not in ["Accion", "Animacion", "Ciencia Ficcion", "Comedia", "Crimen", "Drama", "Fantasia", "Romance", "Suspenso", "Terror"] or "," not in genero:
        genero=input("Género o sintaxis inválidas. Ingrese el género del contenido (separados por comas): ")
    genero=genero.split(",")
    tipo=input("Ingrese el tipo de contenido (serie o película): ")
    while tipo not in ["serie","película"]:
        tipo=input("Tipo inválido. Ingrese el tipo de contenido (serie o película): ")
    if tipo=="película":
        tipo="película"
        n_contenido=Contenido(peliculas=True,series=False,titulo=titulo,genero=genero)
    else:
        tipo="serie"
        n_contenido=Contenido(peliculas=False,series=True,titulo=titulo,genero=genero)
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

def crear_usuario():
    n_nombre=input("Ingrese el nombre del usuario: ")
    n_edad=int(input("Ingrese la edad del usuario: "))
    n_preferencias=input("Ingrese las preferencias del usuario (separadas por comas): ")
    while n_preferencias not in ["Accion", "Animacion", "Ciencia Ficcion", "Comedia", "Crimen", "Drama", "Fantasia", "Romance", "Suspenso", "Terror"] or "," not in n_preferencias:
        n_preferencias=input("Preferencia o sintaxis inválidas. Ingrese las preferencias del usuario (separadas por comas): ")
    n_preferencias=n_preferencias.split(",")
    usuario=Usuario(n_nombre,n_edad,n_preferencias)
    return usuario

def mostrar_datos_usuario(usuario):
    str="Nombre: "+usuario.nombre+" \nEdad: "+str(usuario.edad)+" \nPreferencias: "+" "+usuario.preferencias+" \nHistorial: "+" "+usuario.historial
    return str

def gestionar_usuarios(plataforma,usuario,accion):
    #si se desea agregar un usuario
    if accion=="agregar":
        if plataforma.usuarios.tamaño==0:
            plataforma.usuarios.info=usuario
        else:
            actual=plataforma.usuarios.info
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
        lista.append(nodo.contenido.titulo + " (Popularidad: " + str(nodo.contenido.popularidad) + ")")
        recorrer_inorder(nodo.der, lista)
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
def buscar_contenido(preferencia,catalogo,tipo):
    resultados=[]
    if catalogo.contenido is not None:
        if tipo=="serie":
            if preferencia in catalogo.contenido.genero:
                resultados.append(catalogo.contenido)
                catalogo.izq=buscar_contenido(preferencia,catalogo.izq,tipo)
                catalogo.der=buscar_contenido(preferencia,catalogo.der,tipo)
                
        else:
            if preferencia in catalogo.contenido.genero:
                resultados.append(catalogo.contenido)
                catalogo.izq=buscar_contenido(preferencia,catalogo.izq,tipo)
                catalogo.der=buscar_contenido(preferencia,catalogo.der,tipo)
    else:
        return resultados

#funcion para clasificar contenido segun popularidad (de forma recursiva)
def clasificar_contenido(contenido):
    resultado=[]
    if contenido == []:
        return []  # caso base: lista vacía
    else:
        mayor = contenido[0]
        for c in contenido:
            if c.popularidad > mayor.popularidad:
                mayor = c
        resultado.append(mayor)
        contenido.remove(mayor)  # quitamos el de mayor popularidad
        # Recursión para clasificar el resto
        resultado +=clasificar_contenido(contenido)
    return resultado

def generar_recomendaciones(plataforma):
    todas_series=[]
    todas_peliculas=[]
    recorrer_inorder(plataforma.catalogo_series.contenido,todas_series)
    recorrer_inorder(plataforma.catalogo_peliculas.contenido,todas_peliculas)
    series_ordenadas=clasificar_contenido(todas_series)
    peliculas_ordenadas=clasificar_contenido(todas_peliculas)
    return series_ordenadas[:5],peliculas_ordenadas[:5]

#Programa principal
plataforma=Catalogo()
usuario1=Usuario("Alice",25,["Ciencia Ficcion","Drama"])
usuario2=Usuario("Bob",30,["Accion","Comedia"])
usuario3=Usuario("Charlie",28,["Suspenso","Terror"])
gestionar_usuarios(plataforma,usuario1,"agregar")
gestionar_usuarios(plataforma,usuario2,"agregar")
gestionar_usuarios(plataforma,usuario3,"agregar")

pelicula1=Contenido(peliculas=True,series=False,titulo="Inception",genero=["Ciencia Ficcion","Accion"])
pelicula2=Contenido(peliculas=True,series=False,titulo="The Godfather",genero=["Crimen","Drama"])
serie1=Contenido(peliculas=False,series=True,titulo="Stranger Things",genero=["Ciencia Ficcion","Suspenso"])
serie2=Contenido(peliculas=False,series=True,titulo="Breaking Bad",genero=["Crimen","Drama"])
insertar_contenido(plataforma,pelicula1,"película")
insertar_contenido(plataforma,pelicula2,"película")
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
        """
        opcion_usuario=int(input(menu_usuarios))
        if opcion_usuario==1:
            nuevo_usuario=crear_usuario()
            gestionar_usuarios(plataforma,nuevo_usuario,"agregar")
        elif opcion_usuario==2:
            nombre_eliminar=input("Ingrese el nombre del usuario a eliminar: ")
            usuario_eliminar=Usuario(nombre_eliminar,0,[])
            gestionar_usuarios(plataforma,usuario_eliminar,"eliminar")
        elif opcion_usuario==3:
            nombre_mostrar=input("Ingrese el nombre del usuario a mostrar: ")
            usuario_mostrar=Usuario(nombre_mostrar,0,[])
            datos=gestionar_usuarios(plataforma,usuario_mostrar,"mostrar")
            if datos is not None:
                print(datos)
            else:
                print("Usuario no encontrado.")
        else:
            print("Opción inválida.")
    elif opcion==2:
        menu_contenido="""
        Gestión de contenido:
        1.Agregar contenido
        2.Ver catálogo
        """
        opcion_contenido=int(input(menu_contenido))
        if opcion_contenido==1:
            nuevo_contenido=crear_contenido()
            tipo=nuevo_contenido.serie and "serie" or "película"
            insertar_contenido(plataforma,nuevo_contenido,tipo)
        elif opcion_contenido==2:
            tipo_catalogo=input("Ingrese el tipo de catálogo a mostrar (serie o película): ")
            while tipo_catalogo not in ["serie","película"]:
                tipo_catalogo=input("Tipo inválido. Ingrese el tipo de catálogo a mostrar (serie o película): ")
            catalogo=mostrar_catalogo(plataforma,tipo_catalogo)
            print("Catálogo de "+tipo_catalogo+"s:\n"+catalogo)
        else:
            print("Opción inválida.")
    elif opcion==3:
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
            """
            print(menu_usuario)
            opcion_usuario=int(input())
            if opcion_usuario==1:
                for preferencia in usuario_actual.preferencias:
                    resultados_series=buscar_contenido(preferencia,plataforma.catalogo_series.contenido,"serie")
                    resultados_peliculas=buscar_contenido(preferencia,plataforma.catalogo_peliculas.contenido,"película")
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
                series_ordenadas, peliculas_ordenadas = generar_recomendaciones(plataforma)
                print("Recomendaciones de series:")
                for serie in series_ordenadas[:5]:
                    print("- "+serie.titulo)
                print("Recomendaciones de películas:")
                for pelicula in peliculas_ordenadas[:5]:
                    print("- "+pelicula.titulo)
        else:
            print("Usuario no encontrado.")
    print(menu)
    opcion=int(input())
print("Gracias por usar WonderlandTV. ¡Hasta luego!")


