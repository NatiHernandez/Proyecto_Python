from tkinter import * 
from tkinter import ttk


class Aplicacion():

    def __init__(self, root):

        self.root = root

        self.tabla = Label(self.root, text="Ingrese sus datos", background = "red", bd = 7, foreground = "white", width = 85 )
        self.tabla.grid(row=0, column=0, sticky=NW , columnspan=11)

        self.tit = Label(self.root, text="Titulo", foreground = "black", justify = "center" )
        self.tit.grid(row=1, column=0,)

        self.titulo = Entry(self.root, bd = 7, foreground = "black")
        self.titulo.grid(row=1, column=1, pady = 5)

        self.desc = Label(self.root, text="Descripcion", foreground = "black" )
        self.desc.grid(row=2, column=0, pady = 5)

        self.descripcion = Entry(self.root, bd = 7, foreground = "black" )
        self.descripcion.grid(row=2, column=1, padx = 5)

        self.temas = Label(self.root, text="Temas", background = "red", bd = 7, foreground = "white", width = 85 )
        self.temas.grid(row=9, column=0, sticky=NW , columnspan=11)
        

    #CREAR EL TREVIEW
        self.root.Tabla = ttk.Treeview(self.root, columns=("size", "lastmod"))
        self.root.Tabla.grid(row=7, columnspan=3,)

        self.root.Tabla["columns"] = ("1", "2", "3")
        self.root.Tabla['show'] = 'headings'
        self.root.Tabla.heading("1", text="ID")
        self.root.Tabla.heading("2", text="Titulo")
        self.root.Tabla.heading("3", text="Descripción")


        self.boton1 = Button(self.root, text = "Mostrar registro", width= 20, background = "black", foreground = "white" )
        self.boton1.grid(row = 3, column = 1, pady = 10)

        self.boton2 = Button(self.root, text = "Crear Base",  width = 10, background = "black", foreground = "white")
        self.boton2.grid(row = 4, column = 0, pady = 5)

        self.boton3 = Button(self.root, text = "Alta", width = 10, background = "black", foreground = "white")
        self.boton3.grid(row = 4, column = 2)

        self.eleccion =IntVar()

        self.tema1 = Radiobutton(self.root)
        self.tema1.grid(row = 10, column = 1)
        self.tema2 = Radiobutton(self.root)
        self.tema2.grid(row =13, column = 1)
        self.tema3 = Radiobutton(self.root)
        self.tema3.grid(row = 14, column =1)




