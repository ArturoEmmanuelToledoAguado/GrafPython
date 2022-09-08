from tkinter import *
import random

# Crear una ventana con el título "Factorial"
formulario=Tk()
formulario.title("Generador de numeros")

num1=""
num2=""
res=0
r=StringVar()

def rnd():
    """
    Toma los valores de las dos casillas de entrada, los convierte en enteros y luego utiliza el módulo random
    para generar un número aleatorio entre los dos valores.
    """
    global res,r
    _num1=int(ent.get())
    _num2=int(ent2.get())
    res=random.randint(_num1,_num2)
    r.set(str(res))

# Crear una etiqueta con el texto "Numero 1" y colocarla en la primera columna y la primera fila.
lb1=Label(formulario,text="Numero 1")
lb1.grid(column=1,row=1)

# Crea un cuadro de entrada y lo coloca en la segunda columna y primera fila.
ent=Entry(formulario,width=10,textvariable=num1)
ent.grid(column=2,row=1)

# Crea una etiqueta con el texto "Numero 2" y colócala en la primera columna y segunda fila.
lb2=Label(formulario,text="Numero 2")
lb2.grid(column=1,row=2)

# Crea un cuadro de entrada y lo coloca en la segunda columna y la segunda fila.
ent2=Entry(formulario,width=10,textvariable=num2)
ent2.grid(column=2,row=2)

# Crea una etiqueta con el texto "Numero Generado" y colócala en la primera columna y tercera fila.
lb3=Label(formulario,text="Numero Generado")
lb3.grid(column=1,row=3)

# Crea una etiqueta y la coloca en la segunda columna y tercera fila.
lb4=Label(formulario,textvariable=r)
lb4.grid(column=2,row=3)

# Crea un botón con el texto "Generar" y el ancho de 10. A continuación, coloca el botón en la primera columna y la cuarta fila
btn=Button(formulario,text="Generar",command=rnd,width="10")
btn.grid(column=1,row=4)

# Hacer que la ventana permanezca abierta hasta que el usuario la cierre.
formulario.mainloop()