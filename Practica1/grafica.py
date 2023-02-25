import os
import random



def grafica(ListaPeliculas):
    print("Graficando...")

    archivoDOT = open("imagen.dot","w")
    archivoDOT.write("digraph { \n")
    archivoDOT.write('rankdir = LR \n' )
    archivoDOT.write('node[shape=circle, fontname="Arial Black", fontsize=16]\n')


    listacolores = ["red", "yellow", "blue","black"]
    cont=0
    for i in ListaPeliculas:
        nombre = str(i.nombre)
        anio = str(i.anio)
        genero = str(i.genero)


        #Random
        color = random.choice(listacolores)

        
        linea = 'pelicula'+str(cont)+'[shape=record, color = '+str(color)+', label="'+ nombre +' | {'+anio+' | '+genero+' } "]\n'
        archivoDOT.write(linea)
        cont+=1


    archivoDOT.write("} \n")

    archivoDOT.close()


    os.system("dot.exe -Tpdf imagen.dot -o  Peliculas.pdf")

    ruta = 'Peliculas.pdf'
    os.system(ruta)

    print("Grafica creada revisar archivo Peliculas.pdf")



