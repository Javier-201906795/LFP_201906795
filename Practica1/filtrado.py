from validadores import *
from mensajes import *

def filtraadoporactor(ListaPeliculas):
    print(Titulo_filtroActor())
    #Nueva Lista
    listaActores = []
    listaActores1 = []
    
    
    #Recorre las peliculas
    cont = 0
    for i in ListaPeliculas:
        temp_lista_actores = i.actores
        #obtener actores
        for actor in temp_lista_actores:
            validador = validadorrepetido(actor,listaActores)
            print(actor, " | ", validador)
            if validador == False:
                #guardar
                listaActores.append(actor)
        
        print("----")
        cont = 0
        for j in listaActores:
            cont += 1
            print(cont," | ", j)
        print("----")
    
    #Imprimir
    # print("----")
    # cont = 0
    # for j in temp_listaActores:
    #     cont += 1
    #     print(cont," | ", j)
    # print("----")


def filtradoporanio(ListaPeliculas):
    print("Filtrado por año")
    input()

def filtradoporgenero(ListaPeliculas):
    print("Filtrado por Genero")
    input()