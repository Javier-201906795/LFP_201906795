from validadores import *


def mostrarpeliculas(ListaPeliculas):
    print("\n \n")
    for i in ListaPeliculas:
        i.imprimir()
        print("--------------------")
    print("\n \n")
    input()
    return None

def mostraractores(ListaPeliculas):
    
    print("\n \n")
    cont = 1
    for i in ListaPeliculas:
        print("#",cont," | ",i.nombre)
        print("--------------------")
        cont += 1
    print("\n \n")

    print("Seleccione una pelicula para ver sus actores. ")
    #Evalu si existe la opcion
    opcion = None
    while True:
        opcion = input("Pelicula a Buscar: ")
        if opcion == "exit":
            break
        if validadoropcionespelicuals(opcion,len(ListaPeliculas)):
            break
    #Imprime los actores
    print("---------[ ACTORES ]---------")
    for i in ListaPeliculas[int(opcion)-1].actores:
        print(i)
    # print(ListaPeliculas[int(opcion)].actores)
    print("--------------------------------")
    input()
    return None