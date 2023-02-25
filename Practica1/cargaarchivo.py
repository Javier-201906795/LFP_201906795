
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
def listaPelis(listatxt):
    listPeli = []

    for i in listatxt:
        i = i.split(';')

        cont = 1
        temp_nombre = None
        temp_actores = None
        temp_anio = None
        temp_genero = None
        for j in i:
            if cont == 1:
                temp_nombre = j
            elif cont == 2:
                listaactores = j.split(',')
                temp_actores = listaactores
            elif cont == 3:
                temp_anio = j
            elif cont == 4:
                temp_genero = j
            cont += 1
        
        pelicula = Pelicula(temp_nombre,temp_actores,temp_anio,temp_genero)
        #Validar si existe la pelicula
        cont2 = 0
        for h in listPeli:
            if (h.nombre == pelicula.nombre) :
                #Elimina si hay una pelicula igual
                listPeli.pop(cont2)
            cont2 += 1

        #Agrega la Pelicual al listado
        listPeli.append(pelicula)
    return listPeli
#####################################

#####################################
def cargarArchivo(ruta):

    listatexto = leerarchivolfp(ruta)
    listaPeliculas = None
    listaPeliculas = listaPelis(listatexto)

    
    return listaPeliculas
    
#####################################