from tkinter import *
from string import ascii_letters, digits, punctuation
from random import randint

root = Tk()

root.title("Generador de Contraseñas")

root.resizable(0,0) # dimensiones no editables

root.geometry("550x340+675+300") # dimensiones y posición en pantalla

# Variables Globales

complejidad = StringVar() # guarda la selección de la complejidad de la Contraseña
estado = StringVar() # mostrará el mensaje de exito al copiar
vista = StringVar() # guarda la contraseña para mostrar

# Funciones

def generar():
    try:

        largo = int(complejidad.get())
        estado.set("")

        #Probabilidad

        LETRA = 69 # 69% probabilidad

        NUMERO = 90 # 21% probabilidad

        SIGNO = 100 # 10% probabilidad

        password = ''

        for i in range(largo):
            tipo_dato = randint(1,100) # para determinar aleatoriamente que tipo de dato será usado
            if tipo_dato <= LETRA:
                password += ascii_letters[randint(0,51)]
            elif tipo_dato <= NUMERO:
                password += digits[randint(0,9)]
            else:
                password += punctuation[randint(0,31)]
        
        vista.set(password)
    except:
        vista.set("Seleccione una opción")

def copiar():
    if vista.get() != "" and vista.get() != "Seleccione una opción" and vista.get() != "Genera una Contraseña":
        root.clipboard_clear()
        root.clipboard_append(vista.get())
        estado.set("Copiado!!!")
    else:
        vista.set("Genera una Contraseña")



# Creando un lienzo y dibujando una linea separadora
marco = Canvas(root, width = 520, height = 30)
marco.place(x = 15, y = 35)
marco.create_line(0,25,520,25, fill="black")

# Etiquetas

etiqueta_titulo = Label(root, text="Generador de Contraseñas", font=("Helvetica",24)).place(x=80,y=15)

etiqueta_largo = Label(root, text="Tamaño:", font=("Helvetica",14)).place(x=20,y=80)

etiqueta_estado = Label(root, textvariable=estado, fg="green", font=("Helvetica",16)).place(x=220,y=280)

# Botones de selección de complejidad

boton_facil = Radiobutton(root, text="Facil", variable=complejidad, value="4",).place(x=100,y=120)
boton_medio = Radiobutton(root, text="Medio", variable=complejidad, value="8").place(x=185,y=120)
boton_dificil = Radiobutton(root, text="Dificil", variable=complejidad, value="12").place(x=285,y=120)

# Cuadro de Texto que mostrará la contraseña generada Bloqueada su edición

texto_password = Entry(root, textvariable=vista, state="disable", justify="center", font=("Helvetica",24)).place(x=90,y=180)

# Botones

boton_generar = Button(root, text="Generar", width=10, command=generar).place(x=137,y=240)

boton_copiar = Button(root, text="Copiar", width=10, command=copiar).place(x=300,y=240)

root.mainloop()