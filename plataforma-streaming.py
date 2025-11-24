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
            """
            print(menu_usuario)
            opcion_usuario=int(input())
            if opcion_usuario==1:
                for preferencia in usuario_actual.preferencias:
                    resultados_series=buscar_contenido(preferencia,plataforma.catalogo_series.info,"serie")
                    resultados_peliculas=buscar_contenido(preferencia,plataforma.catalogo_peliculas.info,"película")
                    print("Resultados para la preferencia '"+preferencia+"':")
                    print("Series:")
                    for serie in resultados_series:
                        print("- "+serie.titulo)
                    print("Películas:")
                    for pelicula in resultados_peliculas:
                        print("- "+pelicula.titulo)
            elif opcion_usuario==2:
                print("Historial de visualización:")
                for titulo in usuario_actual.historial:
                    print("- "+titulo)
        else:
            print("Usuario no encontrado.")
    print(menu)
    opcion=int(input())
print("Gracias por usar WonderlandTV. ¡Hasta luego!")


