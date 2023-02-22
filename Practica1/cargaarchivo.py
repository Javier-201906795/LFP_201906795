
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

#####################################
def ingresarruta():
    tempruta = input("• Ingrese la ruta del Archivo LFP: ")
    #Verifica si esta vacio
    while True:
        if tempruta == None or tempruta == "" or tempruta == " ":
            tempruta = input("• Ingrese la ruta del Archivo LFP: ")
        else:
            break

    return tempruta

#####################################
def validararchivolfp(rut):
    while True:
            #Validar si es archivo LFP
            extencion = rut[-4:]
            if (extencion == ".lfp" or extencion == ".LFP" or extencion == ".Lfp"):
                break
            else:
                print("■ ■ Ingrese un archivo con extension .lfp ■ ■")
                rut = input("• Ingrese la ruta del Archivo LFP: ")
    return rut

#####################################
def leerarchivolfp(rut):
    try:
        archivo = open(rut, 'r')
        listatexto = archivo.readlines()
        return listatexto
    except:
        print("■ ■ No se pudo leer el archivo LFP | [leerarchivolfp] ■ ■")
#####################################

#####################################
def cargarArchivo(lista):

    # ruta = ingresarruta()
    # ruta = validararchivolfp(ruta)

    ruta = "entrada.lfp"
    listatexto = leerarchivolfp(ruta)
    print(listatexto)
    print(listatexto[1])
    

            


    print(lista)
    print("---FIN--")
    
#####################################