import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
from tkinter import *
from PIL import Image, ImageTk
from tkinter import font
from constants import *
import csv
import shutil

class Admin_add_doctors(tk.Toplevel):
    def __init__(self,username,password, master=None):
        super().__init__(master)

        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()

        position_top = int(screen_height / 3 - window_height / 3)
        position_right = int(screen_width / 2 - window_width / 2)

        # Set the position of the window to the center of the screen
        self.geometry(f"{window_width}x{window_height}+{position_right}+{position_top}")
        self.title("ADMIN-ADD DOCTORS (admin_add_doctors.py)")

        self.canvas = tk.Canvas(self, width=window_width, height=window_height)
        self.canvas.pack(fill=tk.BOTH, expand=True)

        image = Image.open('Images/Admin_add_doctors.png')
        image = image.resize((window_width, window_height), Image.BICUBIC)
        self.image = ImageTk.PhotoImage(image) # Convert the PIL image to a PhotoImage

        self.canvas.create_image(0, 0, image=self.image, anchor='nw')
        inter_font = font.Font(family="Inter")
        
#--------------------------------------- BUTTON/ Labels ------------------------------------------------------------

        self.photo = ImageTk.PhotoImage(Image.open("Images/admin_add_doctors_Add-details_button.png").resize((230, 60), Image.BICUBIC))
        self.photo1 = ImageTk.PhotoImage(Image.open("Images/back_button.png").resize((45, 30), Image.BICUBIC))

        self.backbutton = Button(self,image=self.photo1,borderwidth=0,highlightthickness=0,command=lambda: self.back_button(username, password))
        self.backbutton.place(width=45,height=30,x=22.5,y=21)

        self.add_details_button = Button(self,image=self.photo,borderwidth=0,highlightthickness=0,command=lambda: authenticate(self.name_entry.get(),age_entry.get(),gender_entry.get(),email_entry.get(),phone_entry.get(),specialization_entry.get(),passwrd_entry.get(),username_entry.get()))
        self.add_details_button.place(width=230,height=60,x=800,y=240)

        gap = 18

        self.name_var = tk.StringVar()
        self.name_entry = Entry(self,textvariable=self.name_var,font=(inter_font,25))
        self.name_entry.place(width=257,height=37.5,x=347,y=67)

        self.age_var = tk.StringVar()
        age_entry = Entry(self,textvariable=self.age_var,font=(inter_font,25))
        age_entry.place(width=257,height=37.5,x=347,y=67+37.5+gap)

        self.gender_var = tk.StringVar()
        gender_entry = Entry(self,textvariable=self.gender_var,font=(inter_font,25))
        gender_entry.place(width=257,height=37.5,x=347,y=67+((37.5+gap)*2))

        self.email_var = tk.StringVar()
        email_entry = Entry(self,textvariable=self.email_var,font=(inter_font,25))
        email_entry.place(width=257,height=37.5,x=347,y=67+((37.5+gap)*3))

        self.phone_var = tk.StringVar()
        phone_entry = Entry(self,textvariable=self.phone_var,font=(inter_font,25))
        phone_entry.place(width=257,height=37.5,x=347,y=67+((37.5+gap)*4))

        self.specialization_var = tk.StringVar()
        specialization_entry = Entry(self,textvariable=self.specialization_var,font=(inter_font,25))
        specialization_entry.place(width=257,height=37.5,x=850,y=67)

        self.passwrd_var = tk.StringVar()
        passwrd_entry = Entry(self,textvariable=self.passwrd_var,font=(inter_font,25))
        passwrd_entry.place(width=257,height=37.5,x=850,y=67+37.5+gap)

        self.username_var = tk.StringVar()
        username_entry = Entry(self,textvariable=self.username_var,font=(inter_font,25))
        username_entry.place(width=257,height=37.5,x=850,y=67+((37.5+gap)*2))


        self.treeview = ttk.Treeview(self,columns=("Username","Name","Age","Gender","Email","Phone No.","Specialization","Password"))

        self.treeview.heading("Username",text="Username")
        self.treeview.heading("Name",text="Name")
        self.treeview.heading("Age",text="Age")
        self.treeview.heading("Gender",text="Gender")
        self.treeview.heading("Email",text="Email")
        self.treeview.heading("Phone No.",text="Phone No.")
        self.treeview.heading("Specialization",text="Specialization")
        self.treeview.heading("Password",text="Password")

        self.treeview.column("#0", width=0, stretch=tk.NO)
        self.treeview.column("Username",anchor="center",width=100)
        self.treeview.column("Name",anchor="center",width=100)
        self.treeview.column("Age",anchor="center",width=100)
        self.treeview.column("Gender",anchor="center",width=100)
        self.treeview.column("Email",anchor="center",width=100)
        self.treeview.column("Phone No.",anchor="center",width=100)
        self.treeview.column("Specialization",anchor="center",width=100)
        self.treeview.column("Password",anchor="center",width=100)

        self.import_data()

        self.treeview.place(x=108,y=355,width=1002,height=310)

        def authenticate(name, age, gender, email, phone, specialization, password, username):
            if name != "" and age != "" and gender != "" and email != "" and phone != "" and specialization != "" and password != "" and username != "":
                age = int(age)

                temp_file = 'temp.csv'
                with open('database/doc_details.csv', 'r') as csv_file, open(temp_file, 'w', newline='') as temp_csv_file:
                    reader = csv.DictReader(csv_file)
                    fieldnames = reader.fieldnames
                    writer = csv.DictWriter(temp_csv_file, fieldnames=fieldnames)

                    writer.writeheader()
                    for row in reader:
                        if row['username'] == username:
                            messagebox.showwarning("Error", "Data already exists!")
                            return
                        writer.writerow(row) 
                    writer.writerow({'username': username, 'name': name, 'age': age, 'gender': gender, 'email': email, 'phone': phone, 'specialization': specialization, 'password': password})

                shutil.move(temp_file, 'database/doc_details.csv')
                messagebox.showinfo("Info", "Data added successfully!")
                self.update_treeview()

            else:
                messagebox.showerror("Error!", "All the Fields are compulsory.")

#----------------------------------------------------------------functions--------------------------------------------------------

    # def authenticate(self, name, age, gender, email, phone, specialization, password, username):
    #     if name != "" and age != "" and gender != "" and email != "" and phone != "" and specialization != "" and password != "" and username != "":
    #         temp_file = 'temp.csv'
    #         with open('database/doc_details.csv', 'r') as csv_file, open(temp_file, 'w', newline='') as temp_csv_file:
    #             reader = csv.DictReader(csv_file)
    #             fieldnames = reader.fieldnames
    #             writer = csv.DictWriter(temp_csv_file, fieldnames=fieldnames)

    #             writer.writeheader()
    #             for row in reader:
    #                 if row['username'] == username:
    #                     messagebox.showwarning("Error", "Data already exists!")
    #                     return
    #                 writer.writerow(row)
    #             writer.writerow({'username': username, 'name': name, 'age': age, 'gender': gender, 'email': email, 'phone': phone, 'specialization': specialization, 'password': password})

    #         shutil.move(temp_file, 'database/doc_details.csv')
    #         messagebox.showinfo("Info", "Data added successfully!")
    #         self.update_treeview()

    #     else:
    #         messagebox.showerror("Error!", "All the Fields are compulsory.")



    def import_data(self):
        with open('database/doc_details.csv', 'r') as csv_file:
            reader = csv.DictReader(csv_file)
            for row in reader:
                self.treeview.insert("", "end", values=(row['username'], row['name'], row['age'], row['gender'], row['email'], row['phone'], row['specialization'], row['password']))


    # def add_details(self, name, age, gender, email, phone, specialization, password, username):
    #     if name != "" and age != "" and gender != "" and email != "" and phone != "" and specialization != "" and password != "" and username != "":
    #         if len(phone) == 10 and phone.isnumeric() or phone == 'None':
    #             if len(age) < 4 and age.isnumeric() or age == 'None':
    #                 with open('doc_details.csv', 'a', newline='') as csv_file:
    #                     fieldnames = ['username', 'name', 'age', 'gender', 'email', 'phone', 'specialization', 'password']
    #                     writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
    #                     writer.writerow({'username': username, 'name': name, 'age': age, 'gender': gender, 'email': email, 'phone': phone, 'specialization': specialization, 'password': password})

    #                 self.name_var.set('')
    #                 self.age_var.set('')
    #                 self.gender_var.set('')
    #                 self.email_var.set('')
    #                 self.phone_var.set('')
    #                 self.specialization_var.set('')
    #                 self.passwrd_var.set('')
    #                 self.username_var.set('')
    #                 self.name_entry.focus_set()

    #                 self.update_treeview()

    #             else:
    #                 messagebox.showerror("Error!", "Invalid Age.")
    #         else:
    #             messagebox.showerror("Error!", "Invalid Phone number.")
    #     else:
    #         messagebox.showerror("Error!", "All the Fields are compulsory.")


    def update_treeview(self):
        self.treeview.delete(*self.treeview.get_children())
        self.import_data()


    def back_button(self,username, password):
        from admin_main import Admin_Main
        self.withdraw()
        back = Admin_Main(username, password)
        back.mainloop()


# if __name__ == "__main__":
#     app = Admin_add_doctors("Demo123","Demo123")
#     app.mainloop()