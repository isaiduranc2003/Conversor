
from tkinter import *
from tkinter import ttk

raiz = Tk()
etqTexto = ttk.Label(raiz, text="logo cadillac")
etqTexto.grid()

imagen = PhotoImage(file="cadillac.png")

etqImagen = ttk.Label(raiz)
etqImagen.grid()
etqImagen['image'] = imagen

etqCombinada = ttk.Label(raiz, text="EtqCombinada",compound="center")
etqCombinada.grid()
etqCombinada['image'] = imagen

raiz.mainloop()
