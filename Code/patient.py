import tkinter as tk
from tkinter import messagebox
from tkinter import *
from PIL import Image, ImageTk
from app_main import HMS
from constants import *
import csv
from file_manager import FileManager

class Patient(tk.Toplevel):
    def __init__(self, master=None):
        super().__init__(master)

        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()

        position_top = int(screen_height / 3 - window_height / 3)
        position_right = int(screen_width / 2 - window_width / 2)

        # Set the position of the window to the center of the screen
        self.geometry(f"{window_width}x{window_height}+{position_right}+{position_top}")
        self.title("PATIENT LOGIN (patient.py)")

        self.canvas = tk.Canvas(self, width=window_width, height=window_height)
        self.canvas.pack(fill=tk.BOTH, expand=True)

        image = Image.open('Images/Login_page.png')
        image = image.resize((window_width, window_height), Image.BICUBIC)
        self.image = ImageTk.PhotoImage(image) # Convert the PIL image to a PhotoImage

        self.canvas.create_image(0, 0, image=self.image, anchor='nw')

        file_manager = FileManager()

#-------------------------------Entry Box-----------------------------------------------------------------

        username_var = tk.StringVar()
        username_entry = Entry(self,textvariable=username_var,font=("Roboto",25))
        username_entry.place(width=405,height=60,x=390,y=285)

        passwrd_var = tk.StringVar()
        passwrd_entry = Entry(self,show="*",textvariable=passwrd_var,font=("Roboto",25))
        passwrd_entry.place(width=405,height=60,x=390,y=285+60+50)

#----------------------------------------------------Buttons-----------------------------

        self.photo = ImageTk.PhotoImage(Image.open("Images/adm_login_button.png").resize((170,47), Image.BICUBIC))
        self.photo1 = ImageTk.PhotoImage(Image.open("Images/adm_signup_button.png").resize((170,47), Image.BICUBIC))
        self.photo2 = ImageTk.PhotoImage(Image.open("Images/back_button.png").resize((45,30), Image.BICUBIC))


        self.loginbutton = Button(self,image=self.photo,borderwidth=0,highlightthickness=0,command=lambda: file_manager.authenticate(self,username_entry.get(),passwrd_entry.get(),'patient'))
        self.loginbutton.place(width=170,height=47,x=507,y=485)

        self.signupbutton = Button(self,image=self.photo1,borderwidth=0,highlightthickness=0,command=self.signup_button)
        self.signupbutton.place(width=170,height=47,x=507,y=485+47+47)

        self.backbutton = Button(self,image=self.photo2,borderwidth=0,highlightthickness=0,command=self.back_button)
        self.backbutton.place(width=45,height=30,x=22.5,y=21)


        # get_username = username_entry.get()
        # get_password = passwrd_entry.get()

        # def authenticate(username, password):
        #     with open('database/patient.csv', 'r') as csv_file:
        #         reader = csv.DictReader(csv_file)
        #         for row in reader:
        #             if row['username'] == username and row['password'] == password:
        #                 messagebox.showinfo("Login", "Login successful!")
        #                 self.login_button(username, password)
        #                 return

        #     messagebox.showwarning("Login", "Invalid username or password!")


    def back_button(self):
        self.destroy()
        self.master.destroy()
        back = HMS()
        back.mainloop()


    def login_button(self,username,password):
        from patient_main import pat_Main
        self.withdraw()
        login = pat_Main(username,password)
        login.mainloop()
        

    def signup_button(self):
        from pat_signup import Pat_Signup
        self.destroy()
        signup = Pat_Signup()
        signup.mainloop()

# if __name__ == "__main__":
#     app = Patient()
#     app.mainloop()
