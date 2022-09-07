from tkinter import *

# Crear una ventana con el título "Factorial"
formulario=Tk()
formulario.title("Contador")

cont=0
c=StringVar()

# Crear una etiqueta con el texto "Contador" y colocarla en la primera columna y la primera fila.
lb1=Label(formulario,text="Contador")
lb1.grid(column=1,row=1)

# Crear una etiqueta donde se muestra el valor del "Contador" y colocarla en la segunda columna y primera fila.
lb2=Label(formulario,width=10,textvariable=c)
lb2.grid(column=2,row=1)

def sumar():
    """
    Toma el valor de la variable global cont, le suma 1 y luego establece el valor de la variable global c a la versión de la cadena del nuevo valor de cont
    """
    global c,cont
    cont=cont+1
    c.set(str(cont))

# Crear un botón con el texto "Siguiente" y colocarlo en la quinta columna y primera fila.
btn=Button(formulario,text="Count Up",command=sumar)
btn.grid(column=3,row=1)

def restar():
    global c,cont
    cont=cont-1
    c.set(str(cont))

btn2=Button(formulario,text="Count Down",command=restar)
btn2.grid(column=4,row=1)

def reset():
    global c,cont
    cont=0
    c.set(str(cont))

btn3=Button(formulario,text="Reset",command=reset)
btn3.grid(column=5,row=1)

# Hacer que la ventana permanezca abierta hasta que el usuario la cierre.
formulario.mainloop()