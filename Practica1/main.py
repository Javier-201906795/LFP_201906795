#╔═════════════════╗
#║   Practica 1    ║
#║ Javier Yllescas ║
#║    201906795    ║
#╚═════════════════╝

from mensajes import *
from cargaarchivo import *
from validadores import *

#Variables Globales
ListaPeliculas = []


#Pantalla Inicial
# print(pantallapricipal())
# input()

#Menu Principal
print(menuprincipal())


#Observar seleccion
opcion = 0
while opcion != 5:
    #Lee la opcion elegida
    entrada = input()
    #Intenta ver si es una opcion elegible
    try:
        opcion = int(entrada)        
    except:
        opcion = 0
        #Menu Principal
        print(menuprincipal())
    



    if (opcion == 1):
        print(m1_cargadearchivios())
        #Carga de archivo
        cargarArchivo(ListaPeliculas)
        #test1
        #testpeli()

    elif (opcion == 2):
        print("dos")
    elif (opcion == 3):
        print("tres")
    elif (opcion == 4):
        print("cuatro")


print("Fin")
