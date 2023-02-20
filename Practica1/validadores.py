


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
    
