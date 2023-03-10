
from tkinter import *
from tkinter import ttk

class ejerciciowidget:
    def __init__(self,raiz):
        raiz.title("Muestra widgets")

        self.nombre = StringVar()
        self.apaterno = StringVar()
        self.amaterno = StringVar()
        self.correo = StringVar()
        self.movil = StringVar()

        mainFrame = ttk.Frame(raiz,padding="20 20 20 20")
        mainFrame.grid()

        mainFrame2 = ttk.Frame(mainFrame,padding="10 10 10 10",relief="raised")
        mainFrame2.grid(pady=20)

        mainFrame3 = ttk.Frame(mainFrame,padding="30 20 35 20",relief="raised")
        mainFrame3.grid(pady=20,padx=15)

        mainFrame4 = ttk.Frame(mainFrame)
        mainFrame4.grid(column=2,row=0)

        mainFrame5 = ttk.Frame(mainFrame)
        mainFrame5.grid(column=2,row=1)

        mainFramebutton = ttk.Frame(mainFrame)
        mainFramebutton.grid(column=0,row=5,padx=30)
        ttk.Button(mainFramebutton, text="Guardar").grid(column=0,row=2,sticky=(S,W))
        ttk.Label(mainFramebutton, text="               ").grid(column=1,row=2)
        ttk.Button(mainFramebutton, text="Cancelar").grid(column=2,row=2,sticky=(S))

        

        ttk.Label(mainFrame2, text="Nombre:").grid(column=0,row=0)
        ttk.Label(mainFrame2, text="").grid(column=0,row=1)
        ttk.Label(mainFrame2, text="A.Paterno:").grid(column=0,row=2)
        ttk.Label(mainFrame2, text="").grid(column=0,row=3)
        ttk.Label(mainFrame2, text="A.Materno:").grid(column=0,row=4)
        ttk.Label(mainFrame2, text="").grid(column=0,row=5)
        ttk.Label(mainFrame2, text="Correo:").grid(column=0,row=6)
        ttk.Label(mainFrame2, text="").grid(column=0,row=7)
        ttk.Label(mainFrame2, text="Movil:").grid(column=0,row=8)


        nombreEntry = ttk.Entry(mainFrame2,width=30)
        nombreEntry.grid(column=1,row=0)
        apaternoEntry = ttk.Entry(mainFrame2,width=30)
        apaternoEntry.grid(column=1,row=2)
        amaternoEntry = ttk.Entry(mainFrame2,width=30)
        amaternoEntry.grid(column=1,row=4)
        correoEntry = ttk.Entry(mainFrame2,width=30)
        correoEntry.grid(column=1,row=6)
        movilEntry = ttk.Entry(mainFrame2,width=30)
        movilEntry.grid(column=1,row=8)

        ttk.Label(mainFrame3, text="Aficiones:").grid(column=0,row=0,sticky=(E))
        aficiones = StringVar()

        leer = ttk.Checkbutton(mainFrame3,text="leer").grid(column=0,row=2)
        musica = ttk.Checkbutton(mainFrame3,text="musica").grid(column=1,row=2)
        videojuegos = ttk.Checkbutton(mainFrame3,text="videojuegos").grid(column=2,row=2)



        ttk.Label(mainFrame4, text="").grid(column=0,row=0,sticky=(E))
        eed = StringVar()
        estudiante = ttk.Radiobutton(mainFrame4,text="estudiante",variable=eed,value='estudiante').grid(column=0,row=0,sticky=W)
        empleado = ttk.Radiobutton(mainFrame4,text="Empleado",variable=eed,value='empelado').grid(column=0,row=1,sticky=W)
        desempleado = ttk.Radiobutton(mainFrame4,text="Desempleado",variable=eed,value='desempleado').grid(column=0,row=2,sticky=W)

        estado = StringVar()
        comboEstados = ttk.Combobox(mainFrame5, textvariable=estado)
        comboEstados.grid()
        comboEstados['values']= ("Jalisco", "Nayarit", "Colima","Michoacan","Estados(32)")
        


raiz = Tk()
ejerciciowidget(raiz)
raiz.mainloop()