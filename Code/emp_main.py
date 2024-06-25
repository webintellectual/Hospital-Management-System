import tkinter as tk
from tkinter import messagebox
from tkinter import *
from PIL import Image, ImageTk
from constants import *


class Emp_Main(tk.Toplevel):
    def __init__(self,username,password, master=None):
        super().__init__(master)

        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()

        position_top = int(screen_height / 3 - window_height / 3)
        position_right = int(screen_width / 2 - window_width / 2)

        # Set the position of the window to the center of the screen
        self.geometry(f"{window_width}x{window_height}+{position_right}+{position_top}")
        self.title("DOCTOR-DASHBOARD (emp_main.py)")

        self.canvas = tk.Canvas(self, width=window_width, height=window_height)
        self.canvas.pack(fill=tk.BOTH, expand=True)

        image = Image.open('Images/doctor_main.png')
        image = image.resize((window_width, window_height), Image.BICUBIC)
        self.image = ImageTk.PhotoImage(image) # Convert the PIL image to a PhotoImage


        self.canvas.create_image(0, 0, image=self.image, anchor='nw')


#-------------------------------------------------------------Buttons-------------------------------------------------------------------------------------------------------

        btns_width = 293
        btns_height = 124

        self.photo = ImageTk.PhotoImage(Image.open("Images/doctor_main_profile_button.png").resize((btns_width, btns_height), Image.BICUBIC))
        self.photo1 = ImageTk.PhotoImage(Image.open("Images/doctor_main_pat-hist_button.png").resize((btns_width, btns_height), Image.BICUBIC))
        self.photo2 = ImageTk.PhotoImage(Image.open("Images/doctor_main_logout_button.png").resize((btns_width, btns_height), Image.BICUBIC))

        self.doc_profile_button = Button(self,image=self.photo,borderwidth=0,highlightthickness=0,command=lambda: self.profile(username, password))
        self.doc_profile_button.place(width=btns_width,height=btns_height,x=454,y=161)

        self.pat_hist_button = Button(self,image=self.photo1,borderwidth=0,highlightthickness=0,command=lambda: self.pat_history(username, password))
        self.pat_hist_button.place(width=btns_width,height=btns_height,x=454,y=160+btns_height+62)

        self.logout_button = Button(self,image=self.photo2,borderwidth=0,highlightthickness=0,command=self.logout)
        self.logout_button.place(width=btns_width,height=btns_height,x=454,y=160+2*(btns_height+62)-1)


#-------------------------------------------------------Funtions----------------------------------------------------------------------------------------------------------


    def logout(self):
        if messagebox.askyesno("Alert","Are You sure you want to Logout?"):
           from emp import Employee
           self.withdraw()
           logout = Employee()
           logout.mainloop()


    def profile(self,username,password):
        from doctor_profile import doctor_Profile
        self.withdraw()
        profile = doctor_Profile(username,password)
        profile.mainloop()


    def pat_history(self,username,password):
        from doctor_pat_hist import Emp_pat_hist
        self.withdraw()
        pat_history = Emp_pat_hist(username,password)
        pat_history.mainloop()

# if __name__ == "__main__":
#     app = Emp_Main("Demo123","Demo123")
#     app.mainloop()