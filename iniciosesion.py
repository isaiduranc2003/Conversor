# aplicacion para convertir pies a metros usando tkinter
#Durán Calderón Isaí Gamaliel
#23/febrero/2023

from tkinter import *
from tkinter import ttk


#init funciona como constructor
class iniciosesion:
    #tipo constructor de la clase
    def __init__(self,raiz):
        #crear atributos
        #poner titulo a la ventana
        raiz.title("Inicio de Sesion")

        #definir variables
        self.usuario = StringVar()
        self.contraseña = StringVar()

        mainFrame = ttk.Frame(raiz, padding="30 30 30 30") #se crea el objeto, padding da margenes
        #padding ejemplo orden: 300 "izquierda", 30 "arriba", 15 "derecha", 120 "abajo"
        mainFrame.grid(column=0, row=0) #coordenada donde se ubica

        usuarioEntry = ttk.Entry(mainFrame,width=20) #width es el tamaño con el que se mostrara la ventana de largo
        usuarioEntry.grid(column=1, row=0, sticky=(W, E)) #sticky acomoda en el eje que se quiere poner W, E, N y S
        contraseñaEntry = ttk.Entry(mainFrame)
        contraseñaEntry.grid(column=1, row=2)
        
        ttk.Label(mainFrame, text="Usuario").grid(column=0, row=0)#aparecera el texto en la ubicacion puesta
        ttk.Label(mainFrame, text="").grid(column=0,row=1)

        ttk.Label(mainFrame, text="Contraseña").grid(column=0,row=2)
        ttk.Label(mainFrame, text="").grid(column=0,row=3)

        ttk.Button(mainFrame, text="Ingresar").grid(column=1,row=4,sticky=(E))

        #Hacer la operacion presionando enter
        raiz.bind("<Return>")

        usuarioEntry.focus() #widget mas focus es para se ponga el cursor aliniciarse dentro de esa parte, o se ponga como seleccionado al iniciarse

        #command nos va apermitir ejecutar un metodo
        #args habilita argumentos para que pueda recibir una serie de parametros
   


if __name__=="__main__":
    print("Este es el archivo principal.")
    print("Nada mas se mostrara esto si es el archivo principal.")

raiz = Tk()
iniciosesion(raiz)
raiz.mainloop()