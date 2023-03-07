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

        mainFrame = ttk.Frame(raiz, padding="10 10 10 10") #se crea el objeto, padding da margenes
        #padding ejemplo orden: 300 "izquierda", 30 "arriba", 15 "derecha", 120 "abajo"
        mainFrame.grid(column=0, row=0) #coordenada donde se ubica

        piesEntry = ttk.Entry(mainFrame,width=20, textvariable=self.pies) #width es el tamaño con el que se mostrara la ventana de largo
        piesEntry.grid(column=1, row=0, sticky=(W, E)) #sticky acomoda en el eje que se quiere poner W, E, N y S
        #sticky=(N,S,W,E)
        
        ttk.Label(mainFrame, text="Pies").grid(column=2, row=0)#aparecera el texto en la ubicacion puesta
        ttk.Label(mainFrame, text="Son equivalentes a: ").grid(column=0,row=1)
        ttk.Label(mainFrame, text="Resultado:", textvariable=self.metros).grid(column=1,row=1)
        ttk.Label(mainFrame, text="Metros").grid(column=2,row=1)

        ttk.Button(mainFrame, text="Calcular", command=self.calcular).grid(column=2,row=2)

        #Hacer la operacion presionando enter
        raiz.bind("<Return>",self.calcular)

        piesEntry.focus() #widget mas focus es para se ponga el cursor aliniciarse dentro de esa parte, o se ponga como seleccionado al iniciarse

        #command nos va apermitir ejecutar un metodo
        #args habilita argumentos para que pueda recibir una serie de parametros
    def calcular(self, *args):
        print("Boton presionado")
        #piesusuario = float(self.pies.get()) #siempre devuelve cadena
        piesusuario = self.pies.get()
        print("pies ingresados", piesusuario)
        try:
            piesFlotante = float(piesusuario) #conversion de cadena a flotante
            metros = piesFlotante * 0.3048
            print("Pies ingresados", self.pies.get())
            print("metros: ",metros)
            self.metros.set(metros)
        except:
            print("Ingresa un dato valido")
            self.metros.set("ingresa un dato valido")
       


if __name__=="__main__":
    print("Este es el archivo principal.")
    print("Nada mas se mostrara esto si es el archivo principal.")

#7/marzo/2023 se agrego try except, focus, sticky, padding 
