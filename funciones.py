from tkinter import *
from tkinter import ttk
from temas import *
import mysql.connector
from tkinter import Label, messagebox
import modulo_base_datos
from tkinter.messagebox import showerror
from modulo_validacion.validar import validar
from view import *


class Funcion():

    def __init__(self, root):
        self.root = root
        self.app = Aplicacion(self.root)
        self.app.boton1.config( command = self.mostrarRegistro)
        self.app.boton2.config( command = self.crear_base)
        self.app.boton3.config( command = self.alta)

        self.app.tema1.config( variable= self.app.eleccion, text="Tema Oscuro", value = 1,command = self.radio_value)
        self.app.tema2.config( variable= self.app.eleccion, text="Tema Clásico", value = 2,command = self.radio_value)
        self.app.tema3.config(variable= self.app.eleccion, text="Tema Sorpresa", value = 3,command = self.radio_value)


    def radio_value(self):
       EleccionTemas(self, self.app.eleccion, self.root, self.app.tit, self.app.tabla, self.app.temas, self.app.desc, self.app.tema1, self.app.tema2, self.app.tema3, self.app.boton1, self.app.boton2, self.app.boton3)
    
    
    def crear_base(self):
        try:
            modulo_base_datos.crearbd(self)
        except:
            showerror("Error", "La base de datos ya existe")

#VALIDAR Y DAR DE ALTA
    def alta(self):
        mibase = mysql.connector.connect(
            host="localhost",
            user="root",
            passwd="",
            database="mi_plantilla3"
            )
        micursor = mibase.cursor()
        dato1 = self.app.titulo.get()
        dato2 = self.app.descripcion.get()  
        sql = "INSERT INTO producto (titulo, descripcion) VALUES (%s, %s)"
        validar(dato1, dato2, micursor, sql, mibase, self.app.titulo, self.app.descripcion)



    def mostrarRegistro(self):
        mibase = mysql.connector.connect(
            host="localhost",
            user="root",
            passwd="",
            database="mi_plantilla3"
            )
        micursor = mibase.cursor()
        sql = "SELECT * FROM producto"
        micursor.execute(sql)
        resultado = micursor.fetchall()
        for i in self.root.Tabla.get_children():
            self.root.Tabla.delete(i)
        for i in resultado:
            self.root.Tabla.insert('','end',value=i)
        for x in resultado:
            print(x)

