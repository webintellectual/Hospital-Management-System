import tkinter as tk
from tkinter import messagebox
from tkinter import *
from PIL import Image, ImageTk
from constants import *


class HMS(tk.Tk):
    def __init__(self):
        super().__init__()

        main_btns_width = 301
        main_btns_height = 66
        main_btns_x = 678.4
        main_btns_y = 304

        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()

        position_top = int(screen_height / 3 - window_height / 3)
        position_right = int(screen_width / 2 - window_width / 2)

        # Set the position of the window to the center of the screen
        self.geometry(f"{window_width}x{window_height}+{position_right}+{position_top}")
        self.title("HEALTH CENTER (app_main.py)")

        self.canvas = tk.Canvas(self, width=window_width, height=window_height)
        self.canvas.pack(fill=tk.BOTH, expand=True)

        image = Image.open('Images/Front_page_1.png')
        image = image.resize((window_width, window_height), Image.BICUBIC)
        self.image = ImageTk.PhotoImage(image) # Convert the PIL image to a PhotoImage

        self.canvas.create_image(0, 0, image=self.image, anchor='nw')
        self.protocol("WM_DELETE_WINDOW", self.Exit)

#----------------------------------------Buttons------------------------------------------------------------------------------------
        self.photo = ImageTk.PhotoImage(Image.open("Images/Home.png").resize((header_buttons_width, header_buttons_height), Image.BICUBIC))
        self.photo1 = ImageTk.PhotoImage(Image.open("Images/About.png").resize((header_buttons_width, header_buttons_height), Image.BICUBIC))
        self.photo2 = ImageTk.PhotoImage(Image.open("Images/Facility.png").resize((header_buttons_width, header_buttons_height), Image.BICUBIC))
        self.photo3 = ImageTk.PhotoImage(Image.open("Images/Contact_us.png").resize((header_buttons_width, header_buttons_height), Image.BICUBIC))
        self.photo4 = ImageTk.PhotoImage(Image.open("Images/Feedback.png").resize((header_buttons_width, header_buttons_height), Image.BICUBIC))
        self.photo5 = ImageTk.PhotoImage(Image.open("Images/Admin.png").resize((main_btns_width, main_btns_height), Image.BICUBIC))
        self.photo6 = ImageTk.PhotoImage(Image.open("Images/Doctor.png").resize((main_btns_width, main_btns_height), Image.BICUBIC))
        self.photo7 = ImageTk.PhotoImage(Image.open("Images/Patient.png").resize((main_btns_width, main_btns_height), Image.BICUBIC))

        self.homebutton = Button(self,borderwidth=0,highlightthickness=0,image=self.photo,command=self.open_home)
        self.homebutton.place(width=header_buttons_width,height=header_buttons_height,x=left_offset,y=header_buttons_y)

        self.aboutbutton = Button(self,borderwidth=0,highlightthickness=0,image=self.photo1,command=self.about)
        self.aboutbutton.place(width=header_buttons_width,height=header_buttons_height,x=left_offset+header_buttons_width,y=header_buttons_y)

        self.facilitybutton = Button(self,borderwidth=0,highlightthickness=0,image=self.photo2,command=self.facility)
        self.facilitybutton.place(width=header_buttons_width,height=header_buttons_height,x=left_offset+(2*header_buttons_width),y=header_buttons_y)
        
        self.contact_usbutton = Button(self,borderwidth=0,highlightthickness=0,image=self.photo3,command=self.contact_us)
        self.contact_usbutton.place(width=header_buttons_width,height=header_buttons_height,x=left_offset+(3*header_buttons_width),y=header_buttons_y)

        self.feedbackbutton = Button(self,borderwidth=0,highlightthickness=0,image=self.photo4,command=self.feedback)
        self.feedbackbutton.place(width=header_buttons_width,height=header_buttons_height,x=left_offset+(4*header_buttons_width),y=header_buttons_y)
        
        self.adminbutton = Button(self,borderwidth=0,highlightthickness=0,image=self.photo5,command=self.open_admin)
        self.adminbutton.place(width=main_btns_width,height=main_btns_height,x=main_btns_x,y=main_btns_y)

        self.empbutton = Button(self,borderwidth=0,highlightthickness=0,image=self.photo6,command=self.open_emp)
        self.empbutton.place(width=main_btns_width,height=main_btns_height,x=main_btns_x,y=main_btns_y+main_btns_height+50)

        self.patientbutton = Button(self,borderwidth=0,highlightthickness=0,image=self.photo7,command=self.open_patient)
        self.patientbutton.place(width=main_btns_width,height=main_btns_height,x=main_btns_x,y=main_btns_y+(2*main_btns_height)+100)

#-----------------------------------------Functions for Every Buttons---------------------------------------------------------------------------------------

    def Exit(self):
        if messagebox.askyesno("Exit","Are You sure you want to exit?"):
            self.destroy()

    def open_admin(self):
        from admin import Admin
        self.withdraw()
        admin = Admin(self)
        admin.mainloop()

    def open_home(self):
        self.destroy()
        home = HMS()
        home.mainloop()
        
    def open_emp(self):
        from emp import Employee
        self.withdraw()
        emp = Employee()
        emp.mainloop()

    def open_patient(self):
        from patient import Patient
        self.withdraw()
        patient = Patient()
        patient.mainloop()


    def about(self):
        from about import About
        self.withdraw()
        about = About()
        about.mainloop()

    
    def facility(self):
        from facility import facility
        self.withdraw()
        fac = facility()
        fac.mainloop()


    def contact_us(self):
        from contact_us import contact_us
        self.withdraw()
        contact = contact_us()
        contact.mainloop()
        

    def feedback(self):
        from feedback import feedback
        self.withdraw()
        feed = feedback()
        feed.mainloop()


#---------------------------------------------------------Main App Calling part------------------------------------------------------------------------------------------

if __name__ == "__main__":
    app = HMS()
    app.mainloop()



