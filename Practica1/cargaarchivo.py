
from mensajes import *


class Pelicula:
    def __init__(self, nombre, actores, anio, genero):
        self.nombre = nombre
        self.actores = actores
        self.anio = anio
        self.genero = genero

    def imprimir(self):
        m =  "Nombre: " + str(self.nombre)+ "\n"
        m += "Actores: " + str(self.actores)+ "\n"
        m += "Año: " + str(self.anio)+ "\n"
        m += "Genero: " + str(self.genero)+ "\n"
        print(m)


def ingresarruta():
    tempruta = input("• Ingrese la ruta del Archivo LFP: ")
    return tempruta

def leerArchivo(rut):

    pass

#####################################
def cargarArchivo(lista):
    ruta = ingresarruta()
    print(ruta)
    if ruta == None or ruta == "" or ruta == " ":
        ingresarruta()
    else:
        print(ruta)
        leerArchivo(ruta)

    print(lista)
    print("---FIN--")
    
#####################################