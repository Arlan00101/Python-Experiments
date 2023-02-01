from tkinter import *


def login():
    username = user.get()
    usr_password = password.get()
    
    print(username,usr_password)

def register():
    print('register')

root = Tk()
root.title("Login")
root.geometry("300x200")
root.resizable(0,0)
main_frame = Frame(root,bg="lightgrey")
main_frame.grid(row=1,column=0)
form_frame = Frame(main_frame, bg="#5B5757")
form_frame.grid(row=0,column=0,padx=80)
buttons_frame = Frame(form_frame, bg="#5B5757")
buttons_frame.grid(row=5,column=0)

user = StringVar()
password = StringVar()

titulo = Label(form_frame, text="Login Usuario", font=("Arial",14), bg="#5B5757", fg="white")
titulo.grid(row=0, column=0, pady=5)

nombre_label = Label(form_frame, text="Usuario:", bg="#5B5757", fg="white")
nombre_label.grid(column=0, padx=8,row=1,sticky=W)

nombre_entry = Entry(form_frame, textvariable=user)
nombre_entry.grid(column=0,row=2)


pass_label = Label(form_frame, text="Contraseña:", bg="#5B5757", fg="white")
pass_label.grid(column=0,row=3, padx=8,sticky=W)

pass_entry = Entry(form_frame, textvariable=password, show="*")
pass_entry.grid(column=0,row=4)


login_button = Button(buttons_frame,text="Acceder", bg='lightgreen', command=login)
login_button.grid(column=0,row=0,ipadx=5,ipady=5, padx=5, pady=20)

register_button = Button(buttons_frame,text="Registrar", bg='orange', command=register)
register_button.grid(column=1,row=0,ipadx=5,ipady=5, padx=5,pady=25)

root.mainloop()