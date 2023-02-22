
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
    ruta = None
    flagexit = False
    
    while flagexit != True :
        ruta = ingresarruta()
        #Valida si esta vacio
        if ruta == None or ruta == "" or ruta == " ":
            flagexit = False
        else:
            flagexit = True
            #Validar si es archivo LFP
            extencion = ruta[-4:]
            if (extencion == ".lfp" or extencion == ".LFP" or extencion == ".Lfp"):
                flagexit = True
            else:
                flagexit = False
            
            


    print(lista)
    print("---FIN--")
    
#####################################