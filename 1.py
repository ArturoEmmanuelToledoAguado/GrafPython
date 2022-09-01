from tkinter import *

root=Tk()
contador = 0
v = StringVar()
etiqueta = Label(root, textvariable=v, font="Helvetica 48")
etiqueta.pack()

def sumar():    
    global v, contador    
    contador = contador + 1    
    v.set(str(contador))

button1 = Button(root, text='sumar', width=25, command=sumar)
button1.pack()
root.mainloop() 