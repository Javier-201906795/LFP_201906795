from validadores import *
from mensajes import *

def filtraadoporactor(ListaPeliculas):
    print(Titulo_filtroActor())
    #Nueva Lista
    listaActores = ["test1","tes2"]
    
    #Recorre las peliculas
    for i in ListaPeliculas:
        temp_lista_actores = i.actores
        #obtener actores
        for actor in temp_lista_actores:
            
            if validadorrepetido(actor,temp_lista_actores):
                #guardar
                listaActores.append(actor)
                    
            
    print("----")
    for j in listaActores:
        print(j)
    
    print("----")
    input()

def filtradoporanio(ListaPeliculas):
    print("Filtrado por año")
    input()

def filtradoporgenero(ListaPeliculas):
    print("Filtrado por Genero")
    input()