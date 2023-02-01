from tkinter import *
import sqlite3
from tkinter import messagebox as mensaje
from PIL import Image,ImageTk
import ttkbootstrap as ttkb
from ttkbootstrap.constants import *
from ttkbootstrap.dialogs.dialogs import Messagebox as mesageboot


class Login_Alt(object):
    width = 500
    height = 400
    

    def create_GUI(self):

        self.ventana = ttkb.Window(size=(self.width,self.height),themename="darkly")

        self.ventana.title("Login")
        self.ventana.resizable(False, False)

        #-------------------------Global vars--------------------------#

        self.user_name = StringVar() # keeps the content of the formulary Entry (User_name)
        self.password = StringVar() # keeps the content of the formulary Entry (pass)

        #-------------------------Actions------------------------------#

        def login_event():
            try:

                login = (self.username_entry.get(), self.password_entry.get())

                Data = sqlite3.connect("DB.sqlite3")

                cursor = Data.cursor()

                cursor.execute("SELECT * FROM USERS WHERE NOMBRE_USUARIO = ? AND PASS = ?", login)

                usuario = cursor.fetchall()

                Data.commit()

                Data.close()

                if len(usuario) == 0 :
                    mesageboot.show_error(title="Error", message="El Usuario o contraseña introducidos no son correctos", parent=self.ventana)
                    return False
                else:
                    mesageboot.show_info(title="Bienvenido", message="Bienvenido "+self.username_entry.get(), parent=self.ventana)
                    self.ventana.destroy()
            except Exception as e:
                mesageboot.show_error(title="Error", message="Error: {}".format(e), parent=self.ventana)

        #-------------------------GUI----------------------------------#

        # load and create background image
        self.bg = Image.open("images/bg_gradient.jpg")
        self.photho = ImageTk.PhotoImage(self.bg)
        self.bg_image_label = ttkb.Label(self.ventana, image=self.photho, width=self.width+5)
        self.bg_image_label.place(x=-2,y=-2)

        # create login frame
        self.login_frame = ttkb.Frame(self.ventana, height=self.height,bootstyle="dark")
        self.login_frame.pack(anchor=CENTER)
        self.login_label = ttkb.Label(self.login_frame, foreground="white", background='#303030', text="Login System", font=ttkb.font.Font(size=20, weight="bold"), justify=CENTER)
        self.login_label.grid(row=0, column=0, padx=30, pady=(80,15))
        self.login_sublabel = ttkb.Label(self.login_frame, foreground="white", background='#303030', text="Please Insert Your Credentials", font=ttkb.font.Font(size=10), justify=CENTER)
        self.login_sublabel.grid(row=1, column=0, padx=30, pady=(2,15))
        self.username_label = ttkb.Label(self.login_frame,foreground="white", background='#303030', text="Usuario:")
        self.username_label.grid(row=2,column=0,padx=27, sticky="w")
        self.username_entry = ttkb.Entry(self.login_frame, width=50,bootstyle="info")
        self.username_entry.grid(row=3, column=0, padx=30, pady=(1, 15))
        self.password_label = ttkb.Label(self.login_frame,foreground="white", background='#303030', text="Contraseña:")
        self.password_label.grid(row=4,column=0,padx=27, sticky="w")
        self.password_entry = ttkb.Entry(self.login_frame, width=50, show="*",bootstyle="info")
        self.password_entry.grid(row=5, column=0, padx=30, pady=(1, 15))
        self.login_button = ttkb.Button(self.login_frame, text="Login", command=login_event, width=20)
        self.login_button.grid(row=6, column=0, padx=30, pady=(15, 95))
        self.ventana.mainloop()


login = Login_Alt()
login.create_GUI() 