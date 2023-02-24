from validadores import *
from mensajes import *

def filtraadoporactor(ListaPeliculas):
    print(Titulo_filtroActor())
    #Nueva Lista
    listaActores = []
    
    #Recorre las peliculas
    for i in ListaPeliculas:
        temp_lista_actores = i.actores
        #obtener actores
        for actor in temp_lista_actores:
            print(actor)
            if validadorrepetido(actor,temp_lista_actores):
                #guardar
                listaActores.append(actor)
                    
    
    #Imprimir
    print("----")
    cont = 0
    for j in listaActores:
        cont += 1
        print(cont," | ", j)
        
    
    print("----")
    input()

def filtradoporanio(ListaPeliculas):
    print("Filtrado por año")
    input()

def filtradoporgenero(ListaPeliculas):
    print("Filtrado por Genero")
    input()