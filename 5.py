from tkinter import *

# Crear una ventana con el título "Factorial"
formulario=Tk()
formulario.title("Calculadora")

num1=""
num2=""
res=0
r=StringVar()

def sumar():
    """
    Toma el valor de la variable global cont, le suma 1 y luego establece el valor de la variable global c a la versión de la cadena del nuevo valor de cont
    """
    global res,r
    _num1=int(ent.get())
    _num2=int(ent2.get())
    res=_num1+_num2
    r.set(str(res))

def restar():
    """
    Toma los dos números de los cuadros de entrada, los resta y pone el resultado en la etiqueta.
    """
    global res,r
    _num1=int(ent.get())
    _num2=int(ent2.get())
    res=_num1-_num2
    r.set(str(res))

def multiplicar():
    """
    Toma los dos números de las casillas de entrada, los multiplica y luego establece el resultado en la etiqueta.
    """
    global res,r
    _num1=int(ent.get())
    _num2=int(ent2.get())
    res=_num1*_num2
    r.set(str(res))

def dividir():
    """
    Toma los dos números de las casillas de entrada, los divide y luego establece el resultado en la etiqueta.
    """
    global res,r
    _num1=int(ent.get())
    _num2=int(ent2.get())
    res=_num1/_num2
    r.set(str(res))

def por():
    """
    Toma los valores de las dos casillas de entrada, los multiplica, los divide por 100, y luego pone el
    resultado en la etiqueta.
    """
    global res,r
    _num1=int(ent.get())
    _num2=int(ent2.get())
    res=(_num1*_num2)/100
    r.set(str(res))

def reset():
    """
    Establece las variables globales res, r, num1 y num2 a 0 y luego establece el texto de la etiqueta r a
    la versión de cadena de res
    """
    global res,r,num1,num2
    res=0
    r.set(str(res))

# Crear una etiqueta con el texto "Primer numero" y colocarla en la primera columna y la primera fila.
lb1=Label(formulario,text="Primer numero")
lb1.grid(column=1,row=1)

# Crea un cuadro de entrada y lo coloca en la segunda columna y primera fila.
ent=Entry(formulario,width=10,textvariable=num1)
ent.grid(column=2,row=1)

# Crea una etiqueta con el texto "Segundo número" y colócala en la primera columna y segunda fila.
lb2=Label(formulario,text="Segundo numero")
lb2.grid(column=1,row=2)

# Crea un cuadro de entrada y lo coloca en la segunda columna y la segunda fila.
ent2=Entry(formulario,width=10,textvariable=num2)
ent2.grid(column=2,row=2)

# Crea una etiqueta con el texto "Resultado" y colócala en la primera columna y tercera fila.
lb3=Label(formulario,text="Resultado")
lb3.grid(column=1,row=3)

# Crea una etiqueta y la coloca en la segunda columna y tercera fila.
lb4=Label(formulario,textvariable=r)
lb4.grid(column=2,row=3)

# Crea un botón con el texto "+", el comando sumar, y un ancho de 10. A continuación, coloca el botón en la primera columna y en la cuarta fila.
btn=Button(formulario,text="+",command=sumar,width="10")
btn.grid(column=1,row=4)

# Crea un botón con el texto "-", el comando restar, y un ancho de 10. A continuación, coloca el botón en la segunda columna y la cuarta fila.
btn2=Button(formulario,text="-",command=restar,width="10")
btn2.grid(column=2,row=4)

# Crea un botón con el texto "*", el comando multiplicar y un ancho de 10. A continuación, coloca el botón en la primera columna y la quinta fila.
btn3=Button(formulario,text="*",command=multiplicar,width="10")
btn3.grid(column=1,row=5)

# Crea un botón con el texto "/", el comando dividir y un ancho de 10. A continuación, coloca el botón en la segunda columna y la quinta fila.
btn4=Button(formulario,text="/",command=dividir,width="10")
btn4.grid(column=2,row=5)

# Crea un botón con el texto "%", el comando por, y un ancho de 10. A continuación, coloca el botón en la primera columna y sexta fila.
btn5=Button(formulario,text="%",command=por,width="10")
btn5.grid(column=1,row=6)

# Crea un botón con el texto "CLEAR", el comando reset, y un ancho de 10. A continuación, coloca el botón en la segunda columna y sexta fila.
btn6=Button(formulario,text="CLEAR",command=reset,width="10")
btn6.grid(column=2,row=6)

# Hacer que la ventana permanezca abierta hasta que el usuario la cierre.
formulario.mainloop()