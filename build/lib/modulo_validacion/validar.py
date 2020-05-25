from tkinter import * 
from tkinter import messagebox

patron = re.compile("^[A-Za-z]+(?:[ _-][A-Za-z]+)*$")  

def validar(dato1, dato2, micursor, sql, mibase, titulo, descripcion):
    if patron.match(dato1) != None:
        datos = (dato1, dato2)
        micursor.execute(sql, datos)
        mibase.commit()
        print(datos)
        titulo.delete(0, END)
        descripcion.delete(0, END)
    else:
        messagebox.showinfo(message="Título inválido.\nIntroduzca otro título", title="Mensaje")