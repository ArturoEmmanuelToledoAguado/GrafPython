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
    global res,r
    _num1=int(ent.get())
    _num2=int(ent2.get())
    res=_num1-_num2
    r.set(str(res))

def multiplicar():
    global res,r
    _num1=int(ent.get())
    _num2=int(ent2.get())
    res=_num1*_num2
    r.set(str(res))

def dividir():
    global res,r
    _num1=int(ent.get())
    _num2=int(ent2.get())
    res=_num1/_num2
    r.set(str(res))

def por():
    global res,r
    _num1=int(ent.get())
    _num2=int(ent2.get())
    res=(_num1*_num2)/100
    r.set(str(res))

def reset():
    global res,r,num1,num2
    res=0
    r.set(str(res))

# Crear una etiqueta con el texto "Primer numero" y colocarla en la primera columna y la primera fila.
lb1=Label(formulario,text="Primer numero")
lb1.grid(column=1,row=1)

ent=Entry(formulario,width=10,textvariable=num1)
ent.grid(column=2,row=1)

lb2=Label(formulario,text="Segundo numero")
lb2.grid(column=1,row=2)

ent2=Entry(formulario,width=10,textvariable=num2)
ent2.grid(column=2,row=2)

lb3=Label(formulario,text="Resultado")
lb3.grid(column=1,row=3)

lb4=Label(formulario,textvariable=r)
lb4.grid(column=2,row=3)

# Crear un botón con el texto "Siguiente" y colocarlo en la quinta columna y primera fila.
btn=Button(formulario,text="+",command=sumar,width="10")
btn.grid(column=1,row=4)

btn2=Button(formulario,text="-",command=restar,width="10")
btn2.grid(column=2,row=4)

btn3=Button(formulario,text="*",command=multiplicar,width="10")
btn3.grid(column=1,row=5)

btn4=Button(formulario,text="/",command=dividir,width="10")
btn4.grid(column=2,row=5)

btn5=Button(formulario,text="%",command=por,width="10")
btn5.grid(column=1,row=6)

btn6=Button(formulario,text="CLEAR",command=reset,width="10")
btn6.grid(column=2,row=6)

# Hacer que la ventana permanezca abierta hasta que el usuario la cierre.
formulario.mainloop()