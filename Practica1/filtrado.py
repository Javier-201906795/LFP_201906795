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
    newlistado = []
    for i in range(len(ListaPeliculas)):
        for j in range(i+1, len(ListaPeliculas)):
            # Si el elemento en la posición j es mayor que el elemento en la posición i
            if convertiranumero(ListaPeliculas[j].anio) > convertiranumero(ListaPeliculas[i].anio):
                print(ListaPeliculas[j].anio, " >  ", ListaPeliculas[i].anio)
                # Intercambiamos los valores de posición
                temp = ListaPeliculas[j]
                ListaPeliculas[j] = ListaPeliculas[i]
                ListaPeliculas[i] = temp

    for i in ListaPeliculas:
        print("  [  ",i.anio,"  ]  ")
        print(i.nombre, " | ",i.genero)
        print("--------------------")

def filtradoporgenero(ListaPeliculas):
    print("Filtrado por Genero")

    nuevalista = []
    lista2 = []

    for i in ListaPeliculas:
        nuevalista.append([" "," "])


    for i in range(0,len(ListaPeliculas)):
        genero = ListaPeliculas[i].genero
        genero1 = nuevalista[i][0]
        # print(genero, genero1)
        # print(i,"------")
        if genero == genero1:
            # print("igual")
            nuevalista[i][1] += ", "+ ListaPeliculas[i].nombre
        else:
            #Agregar
            nuevalista[i][0] = ListaPeliculas[i].genero
            nuevalista[i][1] = ListaPeliculas[i].nombre

    for i in range(1,len(nuevalista)):
        genero = nuevalista[i - 1][0]
        genero1 = nuevalista[i][0]
        if genero == genero1:
            #combinar
            peliculas = nuevalista[i-1][1] + ", "+nuevalista[i][1]
            lista2.append([genero,peliculas])
        

    #imprimir
    print("------")
    for i in nuevalista:
        print(i)


    print("*****")
    for i in lista2:
        print(i)






    # cont = 0 


    # for i in ListaPeliculas:
    #     if cont == 0:
    #         print(i.genero)
    #         nuevalista.append([i.genero,i.nombre])
    #     elif cont < len(ListaPeliculas):
    #         generolista = ListaPeliculas[cont].genero
    #         newcont = cont - 1
    #         generonuevalista = nuevalista[newcont][0]
    #         print(cont - 1)
    #         print(generonuevalista)
    #         if generolista == nuevalista[cont - 1][0]:
    #             print("igual")
    #         else:
    #             print(generolista)

    #     cont += 1