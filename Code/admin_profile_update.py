import tkinter as tk
from tkinter import messagebox
from tkinter import *
from PIL import Image, ImageTk
from tkinter import font
from constants import *
import csv
import shutil
from file_manager import FileManager

class Admin_Profile_update(tk.Toplevel):
    def __init__(self,username,password, master=None):
        super().__init__(master)

        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()

        position_top = int(screen_height / 3 - window_height / 3)
        position_right = int(screen_width / 2 - window_width / 2)

        # Set the position of the window to the center of the screen
        self.geometry(f"{window_width}x{window_height}+{position_right}+{position_top}")
        self.title("ADMIN-PROFILE (UPDATE) (admin_profile_update.py)")

        self.canvas = tk.Canvas(self, width=window_width, height=window_height)
        self.canvas.pack(fill=tk.BOTH, expand=True)

        image = Image.open('Images/Admin_Profile_Edit.png')
        image = image.resize((window_width, window_height), Image.BICUBIC)
        self.image = ImageTk.PhotoImage(image) # Convert the PIL image to a PhotoImage

        self.canvas.create_image(0, 0, image=self.image, anchor='nw')

        inter_font = font.Font(family="Inter")

        self.file_manager = FileManager()

#-------------------------------------------------------------- Entry box / button ---------------------------------------------------------------

        gap = 14

        self.username_var = tk.StringVar()
        username_entry = Entry(self,textvariable=self.username_var,font=(inter_font,25),state="readonly")
        username_entry.place(width=409,height=37.5,x=520,y=150)

        self.name_var = tk.StringVar()
        name_entry = Entry(self,textvariable=self.name_var,font=(inter_font,25))
        name_entry.place(width=409,height=37.5,x=520,y=150+37.5+gap)

        self.age_var = tk.StringVar()
        age_entry = Entry(self,textvariable=self.age_var,font=(inter_font,25))
        age_entry.place(width=409,height=37.5,x=520,y=150+((37.5+gap)*2))

        self.gender_var = tk.StringVar()
        gender_entry = Entry(self,textvariable=self.gender_var,font=(inter_font,25))
        gender_entry.place(width=409,height=37.5,x=520,y=150+((37.5+gap)*3))

        self.email_var = tk.StringVar()
        email_entry = Entry(self,textvariable=self.email_var,font=(inter_font,25))
        email_entry.place(width=409,height=37.5,x=520,y=150+((37.5+gap)*4))

        self.phone_var = tk.StringVar()
        phone_entry = Entry(self,textvariable=self.phone_var,font=(inter_font,25))
        phone_entry.place(width=409,height=37.5,x=520,y=150+((37.5+gap)*5))

        self.passwrd_var = tk.StringVar()
        passwrd_entry = Entry(self,textvariable=self.passwrd_var,font=(inter_font,25))
        passwrd_entry.place(width=409,height=37.5,x=520,y=150+((37.5+gap)*6))


        self.photo = ImageTk.PhotoImage(Image.open("Images/adm_pro_Save_details_button.png").resize((200,52), Image.BICUBIC))
        self.photo1 = ImageTk.PhotoImage(Image.open("Images/back_button.png"))

        self.save_detail_button = Button(self,image=self.photo,borderwidth=0,highlightthickness=0,command=self.save_details)
        self.save_detail_button.place(width=200,height=52,x=495,y=610)

        self.backbutton = Button(self,image=self.photo1,borderwidth=0,highlightthickness=0,command=lambda: self.back_button(username, password))
        self.backbutton.place(width=45,height=30,x=22.5,y=21)

#------------------------------------------------------csv connection----------------------------------------------------------
        with open('database/admin_details.csv', 'r') as f:
            reader = csv.DictReader(f)
            for row in reader:
                if row['username'] == username:
                    name = row['name']
                    age = row['age']
                    gender = row['gender']
                    email = row['email']
                    phone = row['phone']
                    password = row['password']
                    break

        self.username_var.set(username)
        self.name_var.set(name)
        self.age_var.set(age)
        self.gender_var.set(gender)
        self.email_var.set(email)
        self.phone_var.set(phone)
        self.passwrd_var.set(password)

#-----------------------------------------------------------function define -----------------------------------------------------------------    
    # def save_details(self):
    #     username = self.username_var.get()
    #     name = self.name_var.get()
    #     age = self.age_var.get()
    #     gender = self.gender_var.get()
    #     email = self.email_var.get()
    #     phone = self.phone_var.get()
    #     password = self.passwrd_var.get()

    #     if name == "":
    #         messagebox.showerror("Error", "Name cannot be empty.")
    #         return
    #     if age == "":
    #         messagebox.showerror("Error", "Age cannot be empty.")
    #         return
    #     if gender == "":
    #         messagebox.showerror("Error", "Gender cannot be empty.")
    #         return
    #     if email == "":
    #         messagebox.showerror("Error", "Email cannot be empty.")
    #         return
    #     if phone == "":
    #         messagebox.showerror("Error", "Phone cannot be empty.")
    #         return
    #     if password == "":
    #         messagebox.showerror("Error", "Password cannot be empty.")
    #         return

    #     temp_file = 'temp.csv'
    #     with open('database/admin_details.csv', 'r') as csv_file, open(temp_file, 'w', newline='') as temp_csv_file:
    #         reader = csv.DictReader(csv_file)
    #         fieldnames = reader.fieldnames
    #         writer = csv.DictWriter(temp_csv_file, fieldnames=fieldnames)

    #         writer.writeheader()
    #         for row in reader:
    #             if row['username'] == username:
    #                 row['name'] = name
    #                 row['age'] = age
    #                 row['gender'] = gender
    #                 row['email'] = email
    #                 row['phone'] = phone
    #                 row['password'] = password
    #             writer.writerow(row)

    #     shutil.move(temp_file, 'database/admin_details.csv')

    #     from admin_profile import Admin_Profile
    #     self.withdraw()
    #     save = Admin_Profile(username,password)
    #     save.mainloop()
        
    def save_details(self):
        self.file_manager.update_admin_profile(self)

    
    def back_button(self,username,password):
        from admin_profile import Admin_Profile
        self.withdraw()
        back = Admin_Profile(username,password)
        back.mainloop()

# if __name__ == "__main__":
#     app = Admin_Profile_update("Demo123","Demo123")
#     app.mainloop()