#╔═════════════════╗
#║   Practica 1    ║
#║ Javier Yllescas ║
#║    201906795    ║
#╚═════════════════╝

from mensajes import *
from cargaarchivo import *


#Pantalla Inicial
print(pantallapricipal())
input()

#Menu Principal
print(menuprincipal())


#Observar seleccion
opcion = 0
while opcion != 5:
    opcion = int(input())
    if (opcion == 1):
        print(m1_cargadearchivios())
        #Carga de archivo

        #test1
        testpeli()
        
    elif (opcion == 2):
        print("dos")
    elif (opcion == 3):
        print("tres")
    elif (opcion == 4):
        print("cuatro")


print("Fin")
