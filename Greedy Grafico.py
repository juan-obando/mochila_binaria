#INTERFAZ GRAFICA
#---------------------------------------
#Librerias
from tkinter import*
from greedy2 import*
import tkinter as tk
#---------------------------------------
Greedy=Tk()
Greedy.geometry("900x600")
Greedy.title("Greedy (Problema de la mochila binaria)")
Titulo= Label(Greedy,text="GREEDY",font=("Stencil",34),anchor="center",justify="center")
Titulo.place(x=360,y=10)
Titulo1= Label(Greedy,text="Problema de la mochila binaria",font=("Times New roman",14),anchor="e",justify="center")
Titulo1.grid(column=0,row=1,pady=60,padx=330)
#Espacio para agregar el costo 
Texto=Label(Greedy,text="Ingrese el costo de los elementos separados por espacio: [Ej: 7 8 1 2...]",font=("Times New roman",12),anchor="w",justify="left")
Texto.place(x=30,y=100)
ECosto=Entry(Greedy,width=102,justify=LEFT,font=("Times New roman",12))
ECosto.place(x=33,y=135)
#Espacio para ingresar el peso 
Texto=Label(Greedy,text="Ingrese el peso de los elementos separados por espacio: [Ej: 6 10 4 3...]",font=("Times New roman",12),anchor="w",justify="left")
Texto.place(x=30,y=170)
Epeso=Entry(Greedy,width=102,justify=LEFT,font=("Times New roman",12))
Epeso.place(x=33,y=200)
#Espacio para ingresar el volumen maximo 
Texto=Label(Greedy,text="Ingrese el volumen maximo de la mochila: ",font=("Times New roman",12),anchor="w",justify="left")
Texto.place(x=30,y=240)
EVmax=Entry(Greedy,width=7,justify=LEFT,font=("Times New roman",12))
EVmax.place(x=290,y=243)
#Espacio para ingresar restricciones
Texto=Label(Greedy,text="Ingrese el numero de restricciones:  ",font=("Times New roman",12),anchor="w",justify="left")
Texto.place(x=30,y=290)
EVmax=Entry(Greedy,width=7,justify=LEFT,font=("Times New roman",12))
EVmax.place(x=250,y=293)

Greedy.mainloop()

