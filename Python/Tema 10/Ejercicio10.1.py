from tkinter import *

def seleccionar():
    monitor.config(text="{}".format(opcion.get()))
def reset():
    opcion.set(None)
    monitor.config(text="")

root = Tk()
opcion = StringVar()
opcion.set(None)
Radiobutton(root, text="Uno", variable=opcion, 
            value='Uno', command=seleccionar).pack(anchor=W)

Radiobutton(root, text="Dos", variable=opcion, 
            value='Dos', command=seleccionar).pack(anchor=W)
Radiobutton(root, text="Tres", variable=opcion,   
            value='Tres', command=seleccionar).pack(anchor=W)
Radiobutton(root, text="Cuatro", variable=opcion,   
            value='Cuatro', command=seleccionar).pack(anchor=W)

monitor = Label(root)
monitor.pack()
Button(root, text="Reiniciar", command=reset).pack()

root.mainloop()
