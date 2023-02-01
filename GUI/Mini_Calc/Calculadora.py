from tkinter import *


raiz=Tk()

raiz.title("Calculadora")


mainFrame=Frame(raiz)

mainFrame.config(bg = "orange", bd = "20")

mainFrame.pack()

raiz.resizable(0,0)

#---------------------------Variables----------------------
numero = StringVar()

operacion = ""

operacionact= ""

resultado=0 

#---------------------------Pantalla----------------------
Pantalla=Entry(mainFrame,textvariable=numero)
Pantalla.grid(row=1,column=1,padx=10,pady=10,columnspan=6)
Pantalla.config(width = "45", bg="black",fg="lightgreen",justify="right", bd=3)

#---------------------------Funciones----------------------


def numeropulsado(num):
    global operacion

    if operacion != "" or operacion == "igualdad":
        numero.set(num)
        operacion=""
    else:
        numero.set(numero.get() + num)
        
def suma(num):
    global operacion
    global resultado
    global operacionact

    if operacion == "suma":
        resultado += float(num)
    else:
        resultado = float(num)
    
    operacion="suma"
    operacionact = "+"
    numero.set(resultado)

def resta(num):
    global operacion
    global resultado
    global operacionact

    if operacion == "resta":
        resultado -= float(num)
    else:
        resultado = float(num)

    operacion="resta"
    operacionact = "-"
    numero.set(resultado)

def mult(num):
    global operacion
    global resultado
    global operacionact

    if operacion == "multiplicacion":
        resultado *= float(num)
    else:
        resultado = float(num)

    operacion="multiplicacion"
    operacionact = "*"
    numero.set(resultado)

def div(num):
    global operacion
    global resultado
    global operacionact

    if operacion == "division":
        resultado /= float(num)
    else:
        resultado = float(num)

    operacion="division"
    operacionact = "/"
    numero.set(resultado)

def igual():
    global operacion
    global resultado
    global operacionact

    try:
        numero.set(eval(str(resultado)+operacionact+str(float(numero.get()))))
    except Exception as e:
        numero.set(e)
    
    resultado=0
    operacion="igualdad"

def clean():
    global operacion
    global resultado
    global operacionact

    numero.set("")
    operacion = ""
    operacionact = ""
    resultado = 0

def desarrollo():
    global operacion
    global resultado
    global operacionact
    
    numero.set("En desarrollo")
    operacion = ""
    operacionact = ""
    resultado=0

#---------------------------Fila1----------------------
boton7=Button(mainFrame,text="7",width=3, command=lambda:numeropulsado("7"))
boton7.grid(row=2,column=1,padx=2,pady=2)
boton7.config(bg="lightgreen")

boton8=Button(mainFrame,text="8",width=3,command=lambda:numeropulsado("8"))
boton8.grid(row=2,column=2,padx=2,pady=2)
boton8.config(bg="lightgreen")

boton9=Button(mainFrame,text="9",width=3,command=lambda:numeropulsado("9"))
boton9.grid(row=2,column=3,padx=2,pady=2)
boton9.config(bg="lightgreen")

botonMult=Button(mainFrame,text="x",width=3,command=lambda:mult(numero.get()))
botonMult.grid(row=2,column=4,padx=2,pady=2)
botonMult.config(bg="lightgreen")

botonPot=Button(mainFrame,text="^",width=3,command=desarrollo)
botonPot.grid(row=2,column=5,padx=2,pady=2)
botonPot.config(bg="lightgreen")

botonSin=Button(mainFrame,text="sin",width=3,command=desarrollo)
botonSin.grid(row=2,column=6,padx=2,pady=2)
botonSin.config(bg="lightgreen")

#---------------------------Fila2----------------------
boton4=Button(mainFrame,text="4",width=3,command=lambda:numeropulsado("4"))
boton4.grid(row=3,column=1,padx=2,pady=2)
boton4.config(bg="lightgreen")

boton5=Button(mainFrame,text="5",width=3,command=lambda:numeropulsado("5"))
boton5.grid(row=3,column=2,padx=2,pady=2)
boton5.config(bg="lightgreen")

boton6=Button(mainFrame,text="6",width=3,command=lambda:numeropulsado("6"))
boton6.grid(row=3,column=3,padx=2,pady=2)
boton6.config(bg="lightgreen")

botonDiv=Button(mainFrame,text="/",width=3,command=lambda:div(numero.get()))
botonDiv.grid(row=3,column=4,padx=2,pady=2)
botonDiv.config(bg="lightgreen")

botonRaiz=Button(mainFrame,text="sqrt",width=3,command=desarrollo)
botonRaiz.grid(row=3,column=5,padx=2,pady=2)
botonRaiz.config(bg="lightgreen")

botonCos=Button(mainFrame,text="cos",width=3,command=desarrollo)
botonCos.grid(row=3,column=6,padx=2,pady=2)
botonCos.config(bg="lightgreen")

#---------------------------Fila3----------------------
boton1=Button(mainFrame,text="1",width=3,command=lambda:numeropulsado("1"))
boton1.grid(row=4,column=1,padx=2,pady=2)
boton1.config(bg="lightgreen")

boton2=Button(mainFrame,text="2",width=3,command=lambda:numeropulsado("2"))
boton2.grid(row=4,column=2,padx=2,pady=2)
boton2.config(bg="lightgreen")

boton3=Button(mainFrame,text="3",width=3,command=lambda:numeropulsado("3"))
boton3.grid(row=4,column=3,padx=2,pady=2)
boton3.config(bg="lightgreen")

botonSum=Button(mainFrame,text="+",width=3,command=lambda:suma(numero.get()))
botonSum.grid(row=4,column=4,padx=2,pady=2)
botonSum.config(bg="lightgreen")

botonLog=Button(mainFrame,text="log",width=3,command=desarrollo)
botonLog.grid(row=4,column=5,padx=2,pady=2)
botonLog.config(bg="lightgreen")

botonTan=Button(mainFrame,text="tan",width=3,command=desarrollo)
botonTan.grid(row=4,column=6,padx=2,pady=2)
botonTan.config(bg="lightgreen")

#---------------------------Fila4----------------------
boton0=Button(mainFrame,text="0",width=3,command=lambda:numeropulsado("0"))
boton0.grid(row=5,column=1,padx=2,pady=2)
boton0.config(bg="lightgreen")

botoncomma=Button(mainFrame,text=",",width=3,command=lambda:numeropulsado("."))
botoncomma.grid(row=5,column=2,padx=2,pady=2)
botoncomma.config(bg="lightgreen")

botonequal=Button(mainFrame,text="=",width=3,command=lambda:igual())
botonequal.grid(row=5,column=3,padx=2,pady=2)
botonequal.config(bg="lightgreen")

botonRes=Button(mainFrame,text="-",width=3,command=lambda:resta(numero.get()))
botonRes.grid(row=5,column=4,padx=2,pady=2)
botonRes.config(bg="lightgreen")

botonFact=Button(mainFrame,text="!",width=3,command=desarrollo)
botonFact.grid(row=5,column=5,padx=2,pady=2)
botonFact.config(bg="lightgreen")

botonClean=Button(mainFrame,text="C",width=3,command=lambda:clean())
botonClean.grid(row=5,column=6,padx=2,pady=2)
botonClean.config(bg="lightgreen")

raiz.mainloop()