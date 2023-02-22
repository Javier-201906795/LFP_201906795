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
while opcion != 5:
    
    #Lee la opcion elegida
    entrada = input()

    #Valida si es una opcion
    if validadoropciones(entrada) == False:
        opcion = 0
        print(menuprincipal())
    else:
        #guarda la opcion
        opcion = int(entrada)



    if (opcion == 1):
        print(m1_cargadearchivios())
        #Carga de archivo
        cargarArchivo()
        #test1
        #testpeli()

    elif (opcion == 2):
        print("dos")
    elif (opcion == 3):
        print("tres")
    elif (opcion == 4):
        print("cuatro")

    


print("Fin")
