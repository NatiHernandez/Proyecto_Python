import mysql.connector
from tkinter import messagebox

def crearbase():
    try:
        mibase = mysql.connector.connect(
        host="localhost",
        user="root",
        passwd=""
        )
        micursor = mibase.cursor()

        micursor.execute("CREATE DATABASE IF NOT EXISTS mi_plantilla3")
    except:
        messagebox.showinfo(message="La base ha sido creada", title="Título")
    try:
        mibase = mysql.connector.connect(
        host="localhost",
        user="root",
        passwd="",
        database="mi_plantilla3"
        )
        micursor = mibase.cursor()

        micursor.execute("CREATE TABLE producto( id int(11) NOT NULL PRIMARY KEY AUTO_INCREMENT, titulo VARCHAR(128) COLLATE utf8_spanish2_ci NOT NULL, descripcion text COLLATE utf8_spanish2_ci NOT NULL )")
    except:
        messagebox.showinfo(message="La tabla ha sido creada", title="Título")

