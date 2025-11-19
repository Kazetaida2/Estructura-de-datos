
#area de funciones
class Estilo():
    def __init__(self):
        self.info=None
        self.palclaves=[]

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

#programa principal
migenero=Estilo()
agregar(migenero,"fantasia","Medio")
agregar(migenero,"comedia","Alto")
agregar(migenero,"supenso","Bajo")
agregar(migenero,"animacion","Alto")
agregarpal(migenero,"Destruccion")
agregarpal(migenero,"Detective")
agregarpal(migenero,["La Patagonia","Fauna Argentina"])
imprimir(migenero)
