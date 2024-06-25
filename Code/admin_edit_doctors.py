import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
from tkinter import *
from PIL import Image, ImageTk
from tkinter import font
from constants import *
import csv
import shutil

class Admin_edit_doctors(tk.Toplevel):
    def __init__(self,username,password, master=None):
        super().__init__(master)

        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()

        position_top = int(screen_height / 3 - window_height / 3)
        position_right = int(screen_width / 2 - window_width / 2)

        # Set the position of the window to the center of the screen
        self.geometry(f"{window_width}x{window_height}+{position_right}+{position_top}")
        self.title("ADMIN-ADD DOCTORS (admin_edit_doctors.py)")

        self.canvas = tk.Canvas(self, width=window_width, height=window_height)
        self.canvas.pack(fill=tk.BOTH, expand=True)

        image = Image.open('Images/Admin_edit_doctors.png')
        image = image.resize((window_width, window_height), Image.BICUBIC)
        self.image = ImageTk.PhotoImage(image) # Convert the PIL image to a PhotoImage

        self.canvas.create_image(0, 0, image=self.image, anchor='nw')
        inter_font = font.Font(family="Inter")
        
#--------------------------------------- BUTTON/ Labels ------------------------------------------------------------

        self.photo = ImageTk.PhotoImage(Image.open("Images/admin_edit_doctor_update_button.png").resize((215, 50), Image.BICUBIC))
        self.photo1 = ImageTk.PhotoImage(Image.open("Images/admin_edit_doctor_delete_button.png").resize((222, 49), Image.BICUBIC))
        self.photo2 = ImageTk.PhotoImage(Image.open("Images/back_button.png").resize((45, 30), Image.BICUBIC))


        self.backbutton = Button(self,image=self.photo2,borderwidth=0,highlightthickness=0,command=lambda: self.back_button(username, password))
        self.backbutton.place(width=45,height=30,x=22.5,y=21)

        self.update_details_button = Button(self,image=self.photo,borderwidth=0,highlightthickness=0,command=self.update_details)
        self.update_details_button.place(width=215,height=50,x=642,y=275)

        self.delete_details_button = Button(self,image=self.photo1,borderwidth=0,highlightthickness=0,command=self.delete_details)
        self.delete_details_button.place(width=222,height=49,x=642+215+30,y=276)

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
        username_entry = Entry(self,textvariable=self.username_var,font=(inter_font,25),state="readonly")
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


        self.treeview.bind("<Double-1>", self.populate_entry_boxes)

        self.import_data()

        self.treeview.place(x=108,y=355,width=1002,height=310)



    def populate_entry_boxes(self, event):
        selected_item = self.treeview.focus()
        if selected_item:
            values = self.treeview.item(selected_item)["values"]
            self.username_var.set(values[0])
            self.name_var.set(values[1])
            self.age_var.set(values[2])
            self.gender_var.set(values[3])
            self.email_var.set(values[4])
            self.phone_var.set(values[5])
            self.specialization_var.set(values[6])
            self.passwrd_var.set(values[7])
    
    def import_data(self):
        with open('database/doc_details.csv', 'r') as csv_file:
            reader = csv.DictReader(csv_file)
            for row in reader:
                self.treeview.insert("", "end", values=(row['username'], row['name'], row['age'], row['gender'], row['email'], row['phone'], row['specialization'], row['password']))


    def update_details(self):
        selected_item = self.treeview.focus()
        if selected_item:
            values = self.treeview.item(selected_item)["values"]
            username = values[0]
            name = self.name_var.get()
            age = self.age_var.get()
            gender = self.gender_var.get()
            email = self.email_var.get()
            phone = self.phone_var.get()
            specialization = self.specialization_var.get()
            password = self.passwrd_var.get()

            temp_file = 'temp.csv'
            with open('database/doc_details.csv', 'r') as csv_file, open(temp_file, 'w', newline='') as temp_csv_file:
                reader = csv.DictReader(csv_file)
                fieldnames = reader.fieldnames
                writer = csv.DictWriter(temp_csv_file, fieldnames=fieldnames)

                writer.writeheader()
                for row in reader:
                    if row['username'] == username:
                        row['name'] = name
                        row['age'] = age
                        row['gender'] = gender
                        row['email'] = email
                        row['phone'] = phone
                        row['specialization'] = specialization
                        row['password'] = password
                    writer.writerow(row)

            shutil.move(temp_file, 'database/doc_details.csv')

            # Clear the entry boxes
            self.clear_entry_boxes()

            # Refresh the treeview with updated data
            self.treeview.delete(*self.treeview.get_children())
            self.import_data()

            messagebox.showinfo("Success", "Details updated successfully!")
        else:
            messagebox.showerror("Error", "No item selected!")

    def delete_details(self):
        selected_item = self.treeview.focus()
        if selected_item:
            values = self.treeview.item(selected_item)["values"]
            username = values[0]

            temp_file = 'temp.csv'
            with open('database/doc_details.csv', 'r') as csv_file, open(temp_file, 'w', newline='') as temp_csv_file:
                reader = csv.DictReader(csv_file)
                fieldnames = reader.fieldnames
                writer = csv.DictWriter(temp_csv_file, fieldnames=fieldnames)

                writer.writeheader()
                for row in reader:
                    if row['username'] != username:
                        writer.writerow(row)

            shutil.move(temp_file, 'database/doc_details.csv')

            self.clear_entry_boxes()

            # Refresh the treeview with updated data
            self.treeview.delete(*self.treeview.get_children())
            self.import_data()

            messagebox.showinfo("Success", "Details deleted successfully!")
        else:
            messagebox.showerror("Error", "No item selected!")

    def clear_entry_boxes(self):
        self.username_var.set("")
        self.name_var.set("")
        self.age_var.set("")
        self.gender_var.set("")
        self.email_var.set("")
        self.phone_var.set("")
        self.specialization_var.set("")
        self.passwrd_var.set("")


    def back_button(self,username, password):
        from admin_main import Admin_Main
        self.withdraw()
        back = Admin_Main(username, password)
        back.mainloop()

# if __name__ == "__main__":
#     app = Admin_edit_doctors("Demo123","Demo123")
#     app.mainloop()