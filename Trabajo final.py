"""
Definir la estructura adecuada para una plataforma de streaming. Cuenta con un catálogo de series,
películas y documentales. Cada uno de los elementos del catálogo cuenta con una serie de etiquetas
que permiten saber el nivel del género (comedia, acción, terror, etc), los niveles pueden ser bajo,
medio, alto y palabras claves que describen el contenido.

De los documentales de conocer, nombre, etiquetas, palabras claves, duración, fecha, director.

De las películas, se conoce, nombre, director, actorxs (considerar todos los actorxs que aparecen en la
misma), año, producción, etiquetas, palabras claves.

De las series se conoce nombre, género, etiquetas, palabras claves, temporadas (considere que una
serie puede darse durante diferentes temporadas) y tener diferente cantidad de capítulos.

También se desea modelar los clientes a los cuales se le brinda el servicio, de cada cliente de conoce
nombre, apellido, NRO cliente, preferencias (género, actor, director), por cada una de las preferencias
se tiene un porcentaje que permite determinar el nivel de preferencia, tipo de servicio que consume,
fecha de alta fecha de baja.    

"""

#Apartado de etiquetas
class Estilo():
    info=None
    palclaves=[]
class Genero():
    genero=None
    nivel=None
    sig=None

#Temporadas
class Temporadas:
    info=None
    tamaño=0
class temporada:
    nombre=None
    capitulos=None
    sig=None

#por verse
class Actores():
    nombre=None
    papel=None
    sig=None
    tamaño=0

#series
class Catalogo():
    def __init__(self):
        self.info=None
        self.tamaño=0
class Serie():
    Nombre=None
    Estilo=None
    Temporadas=None
    sig=None

class Documentales():
    nombre=None
    estilo=None
    duracion=None
    fecha=None
    director=None
    sig=None
    tamaño=0

class Peliculas():
    nombre=None
    estilo=None
    director=None
    actores=None
    año=None
    produccion=None
    sig=None
    tamaño=0

class Clientes():
    nombre=None
    apellido=None
    ncliente=None
    preferencias=[]
    consumo=None
    fecha_alta=None
    fecha_baja=None
    sig=None
    tamaño=0