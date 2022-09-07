from tkinter import *

# Crear una ventana con el título "Factorial"
formulario=Tk()
formulario.title("Factorial")

cont=-1
c=StringVar()
f=StringVar()

# Crear una etiqueta con el texto "n" y colocarla en la primera columna y la primera fila.
lb1=Label(formulario,text="n")
lb1.grid(column=1,row=1)

# Crear una etiqueta donde se muestra el valor de "n" y colocarla en la segunda columna y primera fila.
lb2=Label(formulario,width=10,textvariable=c)
lb2.grid(column=2,row=1)

# Crear una etiqueta con el texto "Factorial (n)" y colocarla en la tercera columna y primera fila.
lb3=Label(formulario,text="Factorial (n)")
lb3.grid(column=3,row=1)

# Crear una etiqueta que muestra el valor del factorial y colocarla en la cuarta columna y primera fila.
lb4=Label(formulario,width=40,textvariable=f)
lb4.grid(column=4,row=1)

def sumar():
    """
    Toma el valor de la variable global cont, le suma 1 y luego establece el valor de la variable global c a la versión de la cadena del nuevo valor de cont
    """
    global c,cont
    cont=cont+1
    c.set(str(cont))
    factorial(cont)

def factorial(cont):
    """
    Toma un número, lo multiplica por todos los números menores que él y devuelve el resultado (Factorial)
    """
    global f
    r=1
    if cont==0:
        f.set(str(1))
    else:
        while cont>1:
            r*=cont
            cont-=1
        f.set(str(r))

# Crear un botón con el texto "Siguiente" y colocarlo en la quinta columna y primera fila.
btn=Button(formulario,text="Siguiente",command=sumar)
btn.grid(column=5,row=1)

# Hacer que la ventana permanezca abierta hasta que el usuario la cierre.
formulario.mainloop()