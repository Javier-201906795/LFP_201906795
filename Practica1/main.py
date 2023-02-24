#╔═════════════════╗
#║   Practica 1    ║
#║ Javier Yllescas ║
#║    201906795    ║
#╚═════════════════╝

from mensajes import *
from cargaarchivo import *
from validadores import *
from gestionarpeliculas import *

#Variables Globales
ListaPeliculas = None



################################################################


#Pantalla Inicial
# print(pantallapricipal())
# input()

################################################################

#Menu Principal
print(menuprincipal())

################################################################

#Observar seleccion
opcion = 0
cargaexitosaarchivo = False
while opcion != 5:
    
    #Lee la opcion elegida
    entrada = input()

    #Valida si es una opcion
    if validadoropciones(entrada) == False:
        opcion = 0
    else:
        #guarda la opcion
        opcion = int(entrada)


    #Carga de archivo
    if (opcion == 1):
        print(m1_cargadearchivios())
        #Carga las peliculas a una lista
        ListaPeliculas = cargarArchivo()
        #Valida si no esta vacio
        if (ListaPeliculas != None) :
            print(m2_cargaexitosa())
            cargaexitosaarchivo = True
            print(menu2())


    #Gestionar Peliculas
    elif (opcion == 2):
        print(menu3())
        #Ingresa una opcion
        opciongestiones = validaopciones2()
        #Valida si hay listado
        if cargaexitosaarchivo == True:
            if opciongestiones == "a" or opciongestiones == "A":
                mostrarpeliculas(ListaPeliculas)
            else:
                mostraractores(ListaPeliculas)
                print(menu2())
        else:
            mensajeError("No hay peliculas cargadas.")
        

    elif (opcion == 3):
        print("tres")
        print(menu4())
    elif (opcion == 4):
        print("cuatro")

    # if cargaexitosaarchivo == False:
    #     #Menu Principal
    #     print(menuprincipal())
    # else:
    #     print(menu2())


print("Fin")
