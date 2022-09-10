from tkinter import *

# Crear una ventana con el título "Factorial"
formulario=Tk()
formulario.title("Calculadora 2")

num1=""
num2=""
res=0
r=StringVar()
opcion=IntVar()

def selec():
    global res,r
    _num1=int(ent1.get())
    _num2=int(ent2.get())

    if opcion.get() ==1:
        res=_num1+_num2
        r.set(str(res))
    elif opcion.get() ==2:
        res=_num1-_num2
        r.set(str(res))
    elif opcion.get() ==3:
        res=_num1*_num2
        r.set(str(res))
    else:
        res=_num1/_num2
        r.set(str(res))

# Crear un widget de etiqueta y colocarlo en la ventana.
lb1=Label(formulario,text="Operaciones")
lb1.grid(row=1,column=3)

rbtn1=Radiobutton(formulario,text="Sumar",variable=opcion,value=1)
rbtn1.grid(row=2,column=3)

rbtn2=Radiobutton(formulario,text="Restar",variable=opcion,value=2)
rbtn2.grid(row=3,column=3)

rbtn3=Radiobutton(formulario,text="Multiplicar",variable=opcion,value=3)
rbtn3.grid(row=4,column=3)

rbtn4=Radiobutton(formulario,text="Dividir",variable=opcion,value=4)
rbtn4.grid(row=5,column=3)

# Crear un widget de etiqueta y colocarlo en la ventana.
lb2=Label(formulario,text="Valor 1")
lb2.grid(row=2,column=1)

# Crear un widget de etiqueta y colocarlo en la ventana.
lb3=Label(formulario,text="Valor 2")
lb3.grid(row=3,column=1)

# Crear un widget de etiqueta y colocarlo en la ventana.
lb4=Label(formulario,text="Resultado")
lb4.grid(row=4,column=1)

# Crear un widget de etiqueta y colocarlo en la ventana.
ent1=Entry(formulario,width=10,textvariable=num1)
ent1.grid(row=2,column=2)

# Crear un widget de etiqueta y colocarlo en la ventana.
ent2=Entry(formulario,width=10,textvariable=num2)
ent2.grid(row=3,column=2)

# Crear un widget de etiqueta y colocarlo en la ventana.
ent3=Entry(formulario,width=10,textvariable=r)
ent3.grid(row=4,column=2)

# Creating a button widget and placing it in the window.
btn1=Button(formulario,text="Calcular",command=selec)
btn1.grid(row=6,column=2)

# Hacer que la ventana permanezca abierta hasta que el usuario la cierre.
formulario.mainloop()