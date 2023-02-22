#╔═════════════════╗
#║   Practica 1    ║
#║ Javier Yllescas ║
#║    201906795    ║
#╚═════════════════╝

from mensajes import *
from cargaarchivo import *
from validadores import *

#Variables Globales
ListaPeliculas = None



################################################################


#Pantalla Inicial
# print(pantallapricipal())
# input()

################################################################

#Menu Principal
#print(menuprincipal())

################################################################

#Observar seleccion
opcion = 0
cargaexitosaarchivo = False
while opcion != 5:

    if cargaexitosaarchivo == False:
        #Menu Principal
        print(menuprincipal())
    else:
        print(menu2())
    
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
        
        ListaPeliculas = cargarArchivo()

        if (ListaPeliculas != None) :
            print(m2_cargaexitosa())
            cargaexitosaarchivo = True
            

        input()


    elif (opcion == 2):
        print("dos")
    elif (opcion == 3):
        print("tres")
    elif (opcion == 4):
        print("cuatro")

    


print("Fin")
