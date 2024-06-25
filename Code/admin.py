import tkinter as tk
from tkinter import messagebox
from tkinter import *
from PIL import Image, ImageTk
from app_main import HMS
from constants import *
import csv
from file_manager import FileManager

class Admin(tk.Toplevel):
    def __init__(self, master=None):
        super().__init__(master)

        fields_x = 390
        fields_width = 405
        fields_height = 57.5
        fields_y = 285

        file_manager = FileManager()

        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()

        position_top = int(screen_height / 3 - window_height / 3)
        position_right = int(screen_width / 2 - window_width / 2)

        # Set the position of the window to the center of the screen
        self.geometry(f"{window_width}x{window_height}+{position_right}+{position_top}")
        self.title("ADMIN LOGIN (admin.py)")

        self.canvas = tk.Canvas(self, width=window_width, height=window_height)
        self.canvas.pack(fill=tk.BOTH, expand=True)

        image = Image.open('Images/Admin_Login_page.png')
        image = image.resize((window_width, window_height), Image.BICUBIC)
        self.image = ImageTk.PhotoImage(image) # Convert the PIL image to a PhotoImage

        self.canvas.create_image(0, 0, image=self.image, anchor='nw')

#-------------------------------Entry Box-------------------------------------------------------------------------------------------------------------------------------------

        username_var = tk.StringVar()
        username_entry = Entry(self,textvariable=username_var,font=("Roboto",25))
        username_entry.place(width=fields_width,height=fields_height,x=fields_x,y=fields_y)

        passwrd_var = tk.StringVar()
        passwrd_entry = Entry(self,show="*",textvariable=passwrd_var,font=("Roboto",25))
        passwrd_entry.place(width=fields_width,height=fields_height,x=fields_x,y=fields_y+111.4)

#----------------------------------------------------Buttons---------------------------------------------------------------------------------------------------------------

        self.photo = ImageTk.PhotoImage(Image.open("Images/adm_login_button.png"))
        self.photo1 = ImageTk.PhotoImage(Image.open("Images/back_button.png"))


        # self.loginbutton = Button(self,image=self.photo,borderwidth=0,highlightthickness=0,command=lambda: authenticate(username_entry.get(),passwrd_entry.get()))
        self.loginbutton = Button(self,image=self.photo,borderwidth=0,highlightthickness=0,command=lambda: file_manager.authenticate(self,username_entry.get(),passwrd_entry.get(),'admin'))

        self.loginbutton.place(width=140,height=47,x=528,y=533.3)

        self.backbutton = Button(self,image=self.photo1,borderwidth=0,highlightthickness=0,command=self.back_button)
        self.backbutton.place(width=45,height=30,x=22.5,y=21)
        
        global username
        username = username_entry.get()
        global password
        password = passwrd_entry.get()
#----------------------------------------------------TEXT FILE DATABASE CONNECTION--------------------------------------------------------------------------------------------------------
        
        # def authenticate(username, password):
        #     with open('database/admin.csv', 'r') as f:
        #         reader = csv.DictReader(f)
        #         for row in reader:
        #             if row['username'] == username and row['password'] == password:
        #                 messagebox.showinfo("Login", "Login successful!")
        #                 self.login_button(username, password)
        #                 return
        #     messagebox.showwarning("Login", "Invalid username or password!")

#-------------------------------------------------------------defined functions-------------------------------------------------------------------------------------------------

    def back_button(self):
        self.destroy()
        self.master.destroy()
        back = HMS()
        back.mainloop()

    def login_button(self,username,password):
        from admin_main import Admin_Main
        self.withdraw()
        login = Admin_Main(username,password)
        login.mainloop()

# if __name__ == "__main__":
#     app = Admin()
#     app.mainloop()