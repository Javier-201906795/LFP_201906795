import os




def grafica():
    print("Graficando...")


    os.system("dot.exe -Tpdf imagen.dot -o  ReporteGrafico.pdf")



