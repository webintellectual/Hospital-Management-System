import tkinter as tk
from tkinter import messagebox
from tkinter import *
from PIL import Image, ImageTk
from tkinter import font
from constants import *
import csv
from file_manager import FileManager

class Emp_Profile_update(tk.Toplevel):
    def __init__(self,username,password, master=None):
        super().__init__(master)

        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()

        position_top = int(screen_height / 3 - window_height / 3)
        position_right = int(screen_width / 2 - window_width / 2)

        # Set the position of the window to the center of the screen
        self.geometry(f"{window_width}x{window_height}+{position_right}+{position_top}")
        self.title("DOCTOR-PROFILE (UPDATE) (doctor_profile_update.py)")

        self.canvas = tk.Canvas(self, width=window_width, height=window_height)
        self.canvas.pack(fill=tk.BOTH, expand=True)

        image = Image.open('Images/doctor_main_profile_edit.png')
        image = image.resize((window_width, window_height), Image.BICUBIC)
        self.image = ImageTk.PhotoImage(image) # Convert the PIL image to a PhotoImage

        self.canvas.create_image(0, 0, image=self.image, anchor='nw')

        inter_font = font.Font(family="Inter")

        self.file_manager = FileManager()

#-------------------------------------------------------------- Entry box / button ---------------------------------------------------------------

        gap = 18.8

        self.username_var = tk.StringVar()
        username_entry = Entry(self,textvariable=self.username_var,font=(inter_font,25),state="readonly")
        username_entry.place(width=409,height=36,x=553,y=114)

        self.name_var = tk.StringVar()
        name_entry = Entry(self,textvariable=self.name_var,font=(inter_font,21))
        name_entry.place(width=409,height=36,x=553,y=114+36+gap)

        self.age_var = tk.StringVar()
        age_entry = Entry(self,textvariable=self.age_var,font=(inter_font,21))
        age_entry.place(width=409,height=36,x=553,y=114+((36+gap)*2))

        self.gender_var = tk.StringVar()
        gender_entry = Entry(self,textvariable=self.gender_var,font=(inter_font,21))
        gender_entry.place(width=409,height=36,x=553,y=114+((36+gap)*3))

        self.email_var = tk.StringVar()
        email_entry = Entry(self,textvariable=self.email_var,font=(inter_font,21))
        email_entry.place(width=409,height=36,x=553,y=114+((36+gap)*4))

        self.phone_var = tk.StringVar()
        phone_entry = Entry(self,textvariable=self.phone_var,font=(inter_font,21))
        phone_entry.place(width=409,height=36,x=553,y=114+((36+gap)*5))

        self.specialization_var = tk.StringVar()
        specialization_entry = Entry(self,textvariable=self.specialization_var,font=(inter_font,21))
        specialization_entry.place(width=409,height=36,x=553,y=114+((36+gap)*6))

        self.passwrd_var = tk.StringVar()
        passwrd_entry = Entry(self,textvariable=self.passwrd_var,font=(inter_font,21))
        passwrd_entry.place(width=409,height=36,x=553,y=114+((36+gap)*7))


        self.photo = ImageTk.PhotoImage(Image.open("Images/adm_pro_Save_details_button.png").resize((200,52), Image.BICUBIC))
        self.photo1 = ImageTk.PhotoImage(Image.open("Images/back_button.png").resize((45, 30), Image.BICUBIC))

        self.save_detail_button = Button(self,image=self.photo,borderwidth=0,highlightthickness=0,command=self.save_details)
        self.save_detail_button.place(width=200,height=52,x=492,y=608)

        self.backbutton = Button(self,image=self.photo1,borderwidth=0,highlightthickness=0,command=lambda: self.back_button(username, password))
        self.backbutton.place(width=45,height=30,x=22.5,y=21)

#------------------------------------------------------mysql connection----------------------------------------------------------

        with open('database/doc_details.csv', 'r') as csv_file:
            reader = csv.DictReader(csv_file)
            for row in reader:
                if row['username'] == username:
                    username = row['username']
                    name = row['name']
                    age = row['age']
                    gender = row['gender']
                    email = row['email']
                    phone = row['phone']
                    specialization = row['specialization']
                    password = row['password']
                    break

        self.username_var.set(username)
        self.name_var.set(name)
        self.age_var.set(age)
        self.gender_var.set(gender)
        self.email_var.set(email)
        self.phone_var.set(phone)
        self.specialization_var.set(specialization)
        self.passwrd_var.set(password)

#-----------------------------------------------------------function define -----------------------------------------------------------------

    # def save_details(self):
    #     username = self.username_var.get()
    #     name = self.name_var.get()
    #     age = self.age_var.get()
    #     gender = self.gender_var.get()
    #     email = self.email_var.get()
    #     phone = self.phone_var.get()
    #     specialization = self.specialization_var.get()
    #     password = self.passwrd_var.get()

    #     if name == "":
    #         name = None
    #     if age == "":
    #         age = None
    #     if gender == "":
    #         gender = None
    #     if email == "":
    #         email = None
    #     if phone == "":
    #         phone = None
    #     if specialization == "":
    #         specialization = None
    #     if password == "":
    #         password = None

    #     data = []
    #     with open('database/doc_details.csv', 'r') as csv_file:
    #         reader = csv.DictReader(csv_file)
    #         for row in reader:
    #             if row['username'] == username:
    #                 row['name'] = name
    #                 row['age'] = age
    #                 row['gender'] = gender
    #                 row['email'] = email
    #                 row['phone'] = phone
    #                 row['specialization'] = specialization
    #                 row['password'] = password
    #             data.append(row)

    #     with open('database/doc_details.csv', 'w') as csv_file:
    #         fieldnames = ['username', 'name', 'age', 'gender', 'email', 'phone', 'specialization', 'password']
    #         writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
    #         writer.writeheader()
    #         writer.writerows(data)

    #     messagebox.showinfo("Update", "Profile details updated successfully!")

    #     from doctor_profile import doctor_Profile
    #     self.withdraw()
    #     save = doctor_Profile(username,password)
    #     save.mainloop()
    
    def save_details(self):
        self.file_manager.update_profile(self, 'doctor')
    
    def back_button(self,username,password):
        from doctor_profile import doctor_Profile
        self.withdraw()
        back = doctor_Profile(username,password)
        back.mainloop()

# if __name__ == "__main__":
#     app = Emp_Profile_update("Demo123","Demo123")
#     app.mainloop()