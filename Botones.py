#radio boton solo permite seleccionar alguno de estos botones, asignando la misma variable
#entry caja de texto
#combo box es una lista desplegable 
#() cuando esta entre parentesis es tupla [] corechete
from tkinter import *
from tkinter import ttk

raiz = Tk()
boton = ttk.Button(raiz, text="Boton solo texto")
boton.grid()

imagen = PhotoImage(file="cadillac.png")

btnImagen = ttk.Button(raiz)
btnImagen.grid()
btnImagen['image']=imagen

btnCombinada = ttk.Button(raiz, text="Boton combinado",compound="bottom")
btnCombinada.grid()
btnCombinada['image'] = imagen

chkBoton = ttk.Checkbutton(raiz, text="Opcion 1")
chkBoton.grid()

raiz.mainloop()
