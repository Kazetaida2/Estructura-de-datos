#Area de funciones
class Catalogo():
    def __init__(self):
        self.info=None
        self.tamaño=0
class Serie():
    Nombre=None
    Estilo=None
    Temporadas=None
    sig=None

def nuevaserie(ser,estilo,temporadas,nombre):
    caja=ser.info
    if caja==None:
        caja=Serie()
        caja.Nombre=nombre
        caja.Estilo=estilo
        caja.Temporadas=temporadas
    else:
        ncaja=Serie()
        ncaja.Nombre=nombre
        ncaja.Estilo=estilo
        ncaja.Temporadas=temporadas
        caja=ncaja
    ser.info=caja
    return ser

def catalogoseries(ser):
    actual=ser.info
    print("La serie es: " + actual.Nombre)
    print("esta tiene: ")
    leer(actual.Temporadas)
    print("Sus etiquetas son: ")
    imprimir(actual.Estilo)
    while actual.sig!=None:
        print("La serie es: " + actual.Nombre)
        print("esta tiene: ")
        leer(actual.Temporadas)
        print("Sus etiquetas son: ")
        imprimir(actual.Estilo)

#area de funciones estilo
class Estilo():
    info=None
    palclaves=[]

class Genero():
    genero=None
    nivel=None
    sig=None

def agregar(estilo,dato,lv):
    caja=estilo.info
    if caja==None:
        caja=Genero()
        caja.genero=dato
        caja.nivel=lv
    else:
        ncaja=Genero()
        ncaja.sig=caja
        ncaja.genero=dato
        ncaja.nivel=lv
        caja=ncaja
    estilo.info=caja
    return estilo

def imprimir(estilo):
    print("Estos son los generos: ")
    actual=estilo.info
    claves=estilo.palclaves
    print(actual.genero + " " + actual.nivel)
    while actual.sig!=None:
        print(actual.sig.genero + " " + actual.sig.nivel)
        actual=actual.sig
    print("Estas son las palabras claves: ")
    for i in claves:
        print (i)

def agregarpal(estilo,lista):
    if len(lista) > 1 and len(lista[0]) > 1:
        for i in lista:
            estilo.palclaves.append(i)
    else:
        estilo.palclaves.append(lista)
    return estilo

#area de funciones Temporadas
class Temporadas:
    info=None
    tamaño=0

class temporada:
    nombre=None
    capitulos=None
    sig=None

def agregartemp(serie,nombre,caps):
    temp=serie.info
    if temp==None:
        temp=temporada()
        temp.nombre=nombre
        temp.capitulos=caps
    else:
        if temp.sig == None:
            temp.sig=temporada()
            temp.sig.nombre=nombre
            temp.sig.capitulos=caps
        else:
            nuevo=temp
            while nuevo.sig != None:
                nuevo=nuevo.sig
            if nuevo.sig == None:
                nuevo.sig=temporada()
                nuevo.sig.nombre=nombre
                nuevo.sig.capitulos=caps
    serie.tamaño=serie.tamaño+1
    serie.info=temp
    return serie

def leer(serie):
    actual=serie.info
    print("Temporada " + actual.nombre + " tiene " + actual.capitulos + " capitulos")
    while actual.sig!=None:
        print("Temporada " + actual.sig.nombre + " tiene " + actual.sig.capitulos + " capitulos")
        actual=actual.sig
    print("La cantidad de temporadas es de: ",serie.tamaño)

#programa principal
pokemon=Temporadas()
migenero=Estilo()
agregartemp(pokemon,"Pokemon Jhoto", "52")
agregartemp(pokemon,"Pokemon Kanto", "60")
agregartemp(pokemon,"Pokemon Joen", "40")
agregartemp(pokemon,"Pokemon Diamante y perla", "62")
agregartemp(pokemon,"Pokemon blanco y negro", "100")

agregar(migenero,"fantasia","Medio")
agregar(migenero,"comedia","Alto")
agregar(migenero,"supenso","Bajo")
agregar(migenero,"animacion","Alto")
agregarpal(migenero,"Animales")
agregarpal(migenero,"Viaje")
agregarpal(migenero,["Amistad","Lucha"])

serie=Catalogo()
nuevaserie(serie,migenero,pokemon,"Pokemon")
catalogoseries(serie)


