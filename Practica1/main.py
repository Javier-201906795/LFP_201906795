#╔═════════════════╗
#║   Practica 1    ║
#║ Javier Yllescas ║
#║    201906795    ║
#╚═════════════════╝

from mensajes import *
from cargaarchivo import *
from validadores import *
from gestionarpeliculas import *
from filtrado import *
from grafica import *

#Variables Globales
ListaPeliculas = None



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
        #[F]Obtener ruta
        ruta = ingresarruta()
        ruta = validararchivolfp(ruta)
        #Carga las peliculas a una lista
        ListaPeliculas = cargarArchivo(ruta)
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
            print(menuprincipal())
        

    #Filtrado Peliculas
    elif (opcion == 3):
        print(menu4())
        #[F] Ingresa una opcion
        opciongestiones = validaopciones3()
        
        #Valida si hay listado
        if cargaexitosaarchivo == True:
            if opciongestiones == "a" or opciongestiones == "A":
                filtraadoporactor(ListaPeliculas)
                input()
            elif opciongestiones == "b" or opciongestiones == "B":
                filtradoporanio(ListaPeliculas)
                input()
            elif opciongestiones == "c" or opciongestiones == "C":
                filtradoporgenero(ListaPeliculas)
                #input()
            
            print(menu2())
        else:
            mensajeError("No hay peliculas cargadas.")
            print(menuprincipal())


    elif (opcion == 4):
        print("cuatro")
        if cargaexitosaarchivo == True:
            grafica(ListaPeliculas)
            print(menuprincipal())
        else:
            mensajeError("No hay peliculas cargadas.")
            print(menuprincipal())


print("Fin, Grcias")
