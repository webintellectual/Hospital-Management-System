import tkinter as tk
from tkinter import messagebox
from tkinter import *
from PIL import Image, ImageTk
from constants import *
import csv
from file_manager import FileManager

class Emp_Signup(tk.Toplevel):
    def __init__(self, master=None):
        super().__init__(master)

        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()

        position_top = int(screen_height / 3 - window_height / 3)
        position_right = int(screen_width / 2 - window_width / 2)

        # Set the position of the window to the center of the screen
        self.geometry(f"{window_width}x{window_height}+{position_right}+{position_top}")
        self.title("SIGN UP - EMPLOYEE (emp_signup.py)")

        self.canvas = tk.Canvas(self, width=window_width, height=window_height)
        self.canvas.pack(fill=tk.BOTH, expand=True)

        image = Image.open('Images/SIGN_UP_page.png')
        image = image.resize((window_width, window_height), Image.BICUBIC)
        self.image = ImageTk.PhotoImage(image) # Convert the PIL image to a PhotoImage

        self.canvas.create_image(0, 0, image=self.image, anchor='nw')

        file_manager = FileManager()

#-------------------------------Entry Box-----------------------------------------------------------------

        name_var = tk.StringVar()
        name_entry = Entry(self,textvariable=name_var,font=("Roboto",25))
        name_entry.place(width=380,height=41,x=403,y=206)

        username_var = tk.StringVar()
        username_entry = Entry(self,textvariable=username_var,font=("Roboto",25))
        username_entry.place(width=380,height=41,x=403,y=206+41+38)

        passwrd_var = tk.StringVar()
        passwrd_entry = Entry(self,show="*",textvariable=passwrd_var,font=("Roboto",25))
        passwrd_entry.place(width=380,height=41,x=403,y=206+((41+39)*2))

        mob_var = tk.StringVar()
        mob_entry = Entry(self,textvariable=mob_var,font=("Roboto",25))
        mob_entry.place(width=380,height=41,x=403,y=206+((41+39)*3))

#----------------------------------------------------Buttons-----------------------------

        self.photo = ImageTk.PhotoImage(Image.open("Images/create_button.png").resize((255,44), Image.BICUBIC))
        self.photo1 = ImageTk.PhotoImage(Image.open("Images/back_button.png").resize((45,30), Image.BICUBIC))


        self.createbutton = Button(self,image=self.photo,borderwidth=0,highlightthickness=0,command=lambda: file_manager.sign_up(self,name_entry.get(),username_entry.get(),passwrd_entry.get(),mob_entry.get(), 'doctor'))
        self.createbutton.place(width=255,height=44,x=465,y=546)

        self.backbutton = Button(self,image=self.photo1,borderwidth=0,highlightthickness=0,command=self.back_button)
        self.backbutton.place(width=45,height=30,x=22.5,y=21)

        # def insertion(name, username, password, mobile):
        #     if name != "" and username != "" and password != "" and mobile != "":
        #         if len(mobile) == 10 and mobile.isnumeric():
        #             with open('database/employee.csv', 'r') as csv_file:
        #                 reader = csv.DictReader(csv_file)
        #                 for row in reader:
        #                     if row['username'] == username:
        #                         messagebox.showerror("Error!", "Username already exist, please try to login or use other Username.")
        #                         return

        #             with open('database/employee.csv', 'a', newline='') as csv_file:
        #                 fieldnames = ['emp_name', 'username', 'password', 'mobile_no']
        #                 writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        #                 writer.writerow({'emp_name': name, 'username': username, 'password': password, 'mobile_no': mobile})

        #             with open('database/doc_details.csv', 'a', newline='') as csv_file:
        #                 fieldnames = ['username', 'name', 'age' , 'gender' ,'email', 'phone' , 'specialization', 'password'] 
        #                 writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        #                 writer.writerow({'name': name, 'username': username, 'password': password, 'phone': mobile, 'age': 'N/A', 'gender': 'N/A', 'email': 'N/A', 'specialization': 'N/A'})

        #             messagebox.showinfo("Info", "Account Successfully created.")
        #             self.create_button()
        #         else:
        #             messagebox.showerror("Error!", "Invalid mobile number.")
        #     else:
        #         messagebox.showerror("Error!", "All the Fields are compulsory.")

    def back_button(self):
        from emp import Employee
        self.withdraw()
        back = Employee()
        back.mainloop()

    def create_button(self):
        from emp import Employee
        self.withdraw()
        back = Employee()
        back.mainloop()

# if __name__ == "__main__":
#     app = Emp_Signup()
#     app.mainloop()
