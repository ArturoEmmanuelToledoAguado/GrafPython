from tkinter import *

# Crear una ventana con el título "Factorial"
formulario=Tk()
formulario.title("Peliculas")

pelicula=""

def vPel():
    """
    Toma el texto del widget de entrada, lo pone en una lista, y luego inserta el texto en el listbox.
    """
    print("El la funcion")
    global pelicula
    _pelicula=ent1.get()
    lista=[]
    lista.append(_pelicula)
    print(len(lista))

    for item in lista:
        libx.insert(END,item)
        ent1.delete(0,END)


# Crear un widget de etiqueta y colocarlo en la ventana.
lb1=Label(formulario,text="Escribe el titulo de una pelicula")
lb1.grid(row=2,column=1)

# Crear un widget de etiqueta y colocarlo en la ventana.
lb2=Label(formulario,text="Peliculas")
lb2.grid(row=2,column=4)

# Crear un widget de etiqueta y colocarlo en la ventana.
ent1=Entry(formulario,width=10,textvariable=pelicula)
ent1.grid(row=4,column=1)

# Creating a button widget and placing it in the window.
btn1=Button(formulario,text="Añadir",command=vPel)
btn1.grid(row=5,column=1)

# Crear un widget listbox y colocarlo en la ventana.
libx=Listbox(formulario)
libx.grid(row=5,column=4)

# Hacer que la ventana permanezca abierta hasta que el usuario la cierre.
formulario.mainloop()