from validadores import *
from mensajes import *

def filtraadoporactor(ListaPeliculas):
    print(Titulo_filtroActor())
    #Nueva Lista
    listaActores = []
    lista_Peliculas_Orden1 = []
    lista_Actor_Peliculas = []
    
    temp_listaActores = []
    
    #Recorre las peliculas
    for i in ListaPeliculas:
        temp_lista_actores = i.actores
        #obtener actores
        for actor in temp_lista_actores:
            validador = validadorrepetido(actor,listaActores)
            print(actor, " | ", validador)
            if validador == False:
                #guardar
                listaActores.append(actor)
                lista_Peliculas_Orden1.append([i.nombre])
            else:
                #Buscar
                posicion = listaActores.index(actor)
                #obtiene la variable
                variable = lista_Peliculas_Orden1[posicion] 
                variable.append(i.nombre)
        
        

        print("----")
        cont = 0
        for j in listaActores:
            cont += 1
            print(cont," | ", j)
        print("----")
    
        print("----")
        cont = 0
        for j in lista_Peliculas_Orden1:
            cont += 1
            print(cont," | ", j)
        print("----")

    #Unir Listas
    cont = 0
    for j in listaActores:
        lista_Actor_Peliculas.append([j,lista_Peliculas_Orden1[cont]])
        cont += 1

    for j in lista_Actor_Peliculas:
        print(j)

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