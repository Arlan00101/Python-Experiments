import os
import pathlib
from tkinter import *
from tkinter import filedialog

ini_dir = os.curdir

try:
    config = open('config.ini','r+',encoding='UTF-8')
    for i in config:
        if i[0:14] == 'initial_dir = ':
            ini_dir = i[14::]
    config.close()
except:
    pass

def abrir_directorio():
    try:
        archivo = filedialog.askdirectory(title="Carpeta Para Ordenar", initialdir=ini_dir)
        config = open('config.ini','w',encoding='UTF-8')
        config.write(f'initial_dir = {archivo}')
        config.close()
        return archivo
    except:
        log_message("Seleccione un directorio")

def ordenar_archivos(dir,nomb,ext):
    cant = 0
    contenido = []
    try:
        with os.scandir(dir) as directorio:
            for archivos in directorio:
                archivo = pathlib.Path(archivos.path)
                if archivo.suffix == ext:
                    contenido.append(archivos)
        
        for e in contenido:
            cant += 1
            os.rename(e.path,dir + f'\{nomb} - {cant:03d}{ext}')

        log_message(f'Operación Completada con éxito.\nRenombrados: {cant} ficheros','green')
    
    except Exception as e:
        
        if str(e) == "[WinError 3] El sistema no puede encontrar la ruta especificada: ''":
            log_message('Seleccione una Carpeta Válida','red')

        elif str(e)[0:58] == '[WinError 183] No se puede crear un archivo que ya existe:':
            log_message('Error al Renombrar','red')
        else:
            log_message(e,'red')

def log_message(msg,fg):
    log.configure(state=NORMAL, fg=fg)
    log.insert(INSERT,f'{msg}\n')
    log.configure(state=DISABLED)


root = Tk()

WIDTH = 800

HEIGHT = 400

nombre = StringVar()

extension = StringVar()

root.title("Ordenador de Archivos en Serie (OAS)")

root.geometry(f"{WIDTH}x{HEIGHT}+100+50")

root.resizable(0,0)

main_frame = Frame(root,width=WIDTH, height=HEIGHT).pack()

marco = Canvas(main_frame, width = 700, height = 30)
marco.place(x = 40, y = 60)
marco.create_line(0,25,800,25, fill="black")

title_label = Label(main_frame, text="Ordenador de Archivos en Serie (OAS)", font=('Arial',24,'bold'))
title_label.place(x=100,y=30)

name_label = Label(main_frame, text="Nombre:", font=('Arial',14))
name_label.place(x=50,y=100)

ext_label = Label(main_frame, text="Extensión:", font=('Arial',14))
ext_label.place(x=400,y=100)

name_entry = Entry(main_frame, textvariable=nombre, font=('Arial',14))
name_entry.place(x=140,y=105)

ext_entry = Entry(main_frame, textvariable=extension, justify=CENTER, font=('Arial',14), width=6)
ext_entry.place(x=500,y=105)

srch_button = Button(main_frame, text="Buscar Carpeta", width=15, height=2, command=lambda:ordenar_archivos(abrir_directorio(),nombre.get(),extension.get()))
srch_button.place(x=620,y=100)

log = Text(main_frame, width=95, height=14, fg="black")
log.insert(INSERT,"Bienvenido, Introduce un Nombre para la Serie \ny la extensión de los archivos que serán afectados\nno olvides el (.) ej (.mp4)\n")
log.config(state=DISABLED)
log.place(x=15, y=150)

root.mainloop()