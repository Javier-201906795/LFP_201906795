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

    #Unir Listas
    cont = 0
    for j in listaActores:
        lista_Actor_Peliculas.append([j,lista_Peliculas_Orden1[cont]])
        cont += 1
    #Imprimir Opciones
    cont = 1
    for j in lista_Actor_Peliculas:
        print(cont," | ",j[0])
        cont += 1 
    print("\n")
    print("Seleccione una opcion del 1 al ",str(len(lista_Actor_Peliculas)), ":\n")
    #Valida opcion correcta
    opcion = None
    while True:
        opcion = input("Ingrese una opcion:")
        if validadoropcionesnumericas(opcion,len(lista_Actor_Peliculas)):
            break
    #Imprime datos del filtrado
    print("-----------------------")
    print("\n• PELICULAS DONDE PARTICIPO [", lista_Actor_Peliculas[int(opcion)-1][0] ,"]\n")
    for i in lista_Actor_Peliculas[int(opcion)-1][1]:
        print(i)
    print("\n-----------------------\n")
        

def filtradoporanio(ListaPeliculas):
    print("Filtrado por año")
    input()

def filtradoporgenero(ListaPeliculas):
    print("Filtrado por Genero")
    input()