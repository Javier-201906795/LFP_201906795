import tkinter



ventana = tkinter.Tk()
ventana.title("[LFP]Proyecto1_201906795")
ventana.geometry("500x500")

cabezera = tkinter.Label(ventana, text = "Bienvenidos").pack()

def saludo():
    tkinter.Label(ventana, text = "Hola mundo").pack()

def salir():
    ventana.destroy()

boton = tkinter.Button(ventana,text="Hola", command = saludo, fg="red")
boton.pack()
boton.place(x=200, y=100)

ventana.mainloop()



