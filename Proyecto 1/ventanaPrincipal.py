import tkinter 

def ventanprincipal(ventana):
    ventana.title("[LFP]Proyecto1_201906795")
    ventana.geometry("500x500")

    cabezera = tkinter.Label(ventana, text = "Archivo")
    cabezera.config(bg="#FFFF00", font=("Arial",24))
    cabezera.place(relx=0.01, rely=0.05, anchor='sw')

    # tkinter.Label(ventana, text="Position 1 : x=0, y=0", bg="#FFFF00", fg="white").place(x=50, y=50)