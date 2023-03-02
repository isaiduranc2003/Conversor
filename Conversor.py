# aplicacion para convertir pies a metros usando tkinter
#Durán Calderón Isaí Gamaliel
#23/febrero/2023

from tkinter import *
from tkinter import ttk


#init funciona como constructor
class Conversor:
    #tipo constructor de la clase
    def __init__(self,raiz):
        #crear atributos
        #poner titulo a la ventana
        raiz.title("Pies a metros")

        #definir variables
        self.pies = StringVar()
        self.metros = StringVar()

        mainFrame = ttk.Frame(raiz) #se crea el objeto
        mainFrame.grid(column=0, row=0) #coordenada donde se ubica

        piesEntry = ttk.Entry(mainFrame, textvariable=self.pies)
        piesEntry.grid(column=1, row=0)
        
        ttk.Label(mainFrame, text="Pies").grid(column=2, row=0)#aparecera el texto en la ubicacion puesta
        ttk.Label(mainFrame, text="Son equivalentes a: ").grid(column=0,row=1)
        ttk.Label(mainFrame, text="Resultado:", textvariable=self.metros).grid(column=1,row=1)
        ttk.Label(mainFrame, text="Metros").grid(column=2,row=1)

        ttk.Button(mainFrame, text="Calcular", command=self.calcular).grid(column=2,row=2)

        #Hacer la operacion presionando enter
        raiz.bind("<Return>",self.calcular)

        #command nos va apermitir ejecutar un metodo
        #args habilita argumentos para que pueda recibir una serie de parametros
    def calcular(self, *args):
        print("Boton presionado")
        #piesusuario = float(self.pies.get()) #siempre devuelve cadena
        piesusuario = self.pies.get()
        print("pies ingresados", piesusuario)
        piesFlotante = float(piesusuario) #conversion de cadena a flotante
        metros = piesFlotante * 0.3048
        #print("Pies ingresados", self.pies.get())
        print("metros: ",metros)
        self.metros.set(metros)

        
       


if __name__=="__main__":
    print("Este es el archivo principal.")
    print("Nada mas se mostrara esto si es el archivo principal.")

