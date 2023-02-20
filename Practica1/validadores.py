


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
        opcion = 0
        return False
    else:
        numero = int(valor)
        #Evaluar si es una opcion valida
        # if (numero >0)