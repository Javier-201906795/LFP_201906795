import tkinter
import tkinter.messagebox



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


def test1():
    tkinter.messagebox.showinfo("title", "MENSAJE NORMAL")

boton = tkinter.Button(ventana,text="TEST", command = test1, fg="red")
boton.pack()
boton.place(x=200, y=200)


def test2():
    respueta = tkinter.messagebox.askquestion("title", "MENSAJE NORMAL")
    if respueta == "yes":
        tkinter.messagebox.showinfo("title", "MENSAJE NORMAL")
    else:
        tkinter.messagebox.showinfo("title", "No")

boton = tkinter.Button(ventana,text="TEST2", command = test2, fg="red")
boton.pack()
boton.place(x=200, y=200)


ventana.mainloop()



