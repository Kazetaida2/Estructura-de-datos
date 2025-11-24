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
    #Creamos la clase Contenido
    def __init__(self, pelicula, serie, titulo, genero = None, popularidad  = 0, likes = 0):
        #Agregamos información básica y otra que se usará posteriormente
        self.pelicula = pelicula
        self.serie = serie
        self.titulo = titulo
        self.temporadas = 0
        self.episodio = []
        self.duracion = 0
        self.genero = genero if genero else ["Accion", "Animacion", "Ciencia Ficcion", "Comedia", "Crimen", "Drama", "Fantasia", "Romance", "Suspenso", "Terror"]
        self.popularidad = popularidad
        self.likes = likes
        self.comentarios = []
        self.sig = None

class Catalogo():
    def __init__(self,usuario):
        self.usuario=usuario
        self.contenido=None
        self.izq=None
        self.der=None
        self.tamaño=0

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

def insertar_contenido(plataforma,contenido,tipo):
    if tipo=="serie":
        if plataforma.catalogo_series.tamaño==0:
            plataforma.catalogo_series.contenido=contenido
        else:
            actual=plataforma.catalogo_series.contenido
            while actual.sig is not None:
                actual=actual.sig
            actual.sig=contenido
        plataforma.catalogo_series.tamaño+=1
    else:
        if plataforma.catalogo_peliculas.tamaño==0:
            plataforma.catalogo_peliculas.contenido=contenido
        else:
            actual=plataforma.catalogo_peliculas.contenido
            while actual.sig is not None:
                actual=actual.sig
            actual.sig=contenido
        plataforma.catalogo_peliculas.tamaño+=1

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
def mostrar_catalogo(plataforma,tipo):
    resultado=""
    if tipo=="serie":
        actual=plataforma.catalogo_series.info
        while actual is not None:
            resultado+=actual.titulo+"\n"
            actual=actual.sig
    else:
        actual=plataforma.catalogo_peliculas.info
        while actual is not None:
            resultado+=actual.titulo+"\n"
            actual=actual.sig
    return resultado

#funcion para buscar contenido segun preferencias (de forma recursiva)
def buscar_contenido(preferencia,contenido,tipo):
    resultados=[]
    if contenido is not None:
        if tipo=="serie":
            if preferencia in contenido.genero:
                resultados.append(contenido)
        else:
            if preferencia in contenido.genero:
                resultados.append(contenido)
        return buscar_contenido(preferencia,contenido.sig,tipo)
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


#Programa principal
plataforma=PlataformaStreaming()
usuario1=crear_usuario()
usuario2=crear_usuario()
usuario3=crear_usuario()
gestionar_usuarios(plataforma,usuario1,"agregar")
gestionar_usuarios(plataforma,usuario2,"agregar")
gestionar_usuarios(plataforma,usuario3,"agregar")

pelicula1=crear_contenido()
pelicula2=crear_contenido()
serie1=crear_contenido()
serie2=crear_contenido()
insertar_contenido(plataforma,pelicula1,"película")
insertar_contenido(plataforma,pelicula2,"película")
insertar_contenido(plataforma,serie1,"serie")
insertar_contenido(plataforma,serie2,"serie")


menu="""
Bienvenido a la plataforma de streaming WonderlandTV. Por favor, seleccione una opción:
1.gestionar usuarios
2.gestionar contenido
"""


