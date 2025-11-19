#area de funciones
class Temporadas:
    def __init__ (self):
        self.info=None
        self.tamaño=0

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
agregartemp(pokemon,"Pokemon Jhoto", "52")
agregartemp(pokemon,"Pokemon Kanto", "60")
agregartemp(pokemon,"Pokemon Joen", "40")
agregartemp(pokemon,"Pokemon Diamante y perla", "62")
agregartemp(pokemon,"Pokemon blanco y negro", "100")
leer(pokemon)