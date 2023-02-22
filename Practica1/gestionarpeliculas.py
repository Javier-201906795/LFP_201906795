from validadores import *


def mostrarpeliculas(ListaPeliculas):
    print("\n \n")
    for i in ListaPeliculas:
        i.imprimir()
        print("--------------------")
    print("\n \n")
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
    
    while True:
        opcion = input("Pelicula a Buscar: ")
        if opcion == 5 or opcion == "5":
            break
        if validadoropcionespelicuals(opcion,len(ListaPeliculas)):
            break

    return None