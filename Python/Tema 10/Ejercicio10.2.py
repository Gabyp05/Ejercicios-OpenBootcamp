from tkinter import *
master = Tk()
elemento = StringVar()
listbox = Listbox(master)
for item in ["Gabriela", "Aly", "Genesis", "Richard", "Carlos", "Mathias", "Alexander"]:
 listbox.insert(END, item)
listbox.pack()
label = Label(text="Lista de nombres")
label.pack()
master.mainloop()
