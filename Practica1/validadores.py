


def validarint(valorint):
    valor = valorint
    esunnumero = False
    try:
        valor = int(valorint)        
        esunnumero = True
        return esunnumero
    except:
        esunnumero = False
        return esunnumero
    

def validadoropciones(valor):

    #Valida si es un numero
    if validarint(valor) == False:
        #No es un numero 
        opcion = 0
        return False
    else:
        numero = int(valor)
        #Evaluar si es una opcion valida
        if (numero >0 and numero <6):
            return True
        else:
            return False
        

def validaopciones2():
    opciongestion = None
    while True:
        opciongetion = input("Ingrese una Opcion: ")
        if opciongetion == "A" or opciongetion == "a" or opciongetion == "B" or opciongetion == "b":
            break
    return opciongetion


def validaopciones3():
    opciongestion = None
    while True:
        opciongetion = input("Ingrese una Opcion: ")
        if opciongetion == "A" or opciongetion == "a" or opciongetion == "B" or opciongetion == "b" or opciongetion == "C" or opciongetion == "c":
            break
    return opciongetion

def validadoropcionespelicuals(valor,max):

    #Valida si es un numero
    if validarint(valor) == False:
        #No es un numero 
        return False
    else:
        numero = int(valor)
        #Evaluar si es una opcion valida
        if (numero >0 and numero <= max):
            return True
        else:
            return False


def validadorrepetido(dato,lista):
    contador = 0
    for elemento in lista:
        if elemento == dato:
            contador += 1
            if contador >= 1:
                return True
    return False


def validadoropcionesnumericas(valor,max):
    #El valor inicial es uno

    #Valida si es un numero
    if validarint(valor) == False:
        #No es un numero 
        opcion = 0
        return False
    else:
        numero = int(valor)
        #Evaluar si es una opcion valida
        if (numero >0 and numero <= max):
            return True
        else:
            return False
        
def quitarespacioalprincipio(texto):
    cont = 0
    newtext = ""
    for i in texto:
        #primeros caractes
        if cont <=1:
            #validar
            if i == "" or i == " ":
                pass
            else:
                newtext += i
        else:
            #resto de caracteres
            newtext += i
        cont += 1
    return newtext