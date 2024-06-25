import tkinter as tk
from tkinter import messagebox
from tkinter import *
from PIL import Image, ImageTk
from constants import *

class pat_Main(tk.Toplevel):
    def __init__(self,username,password, master=None):
        super().__init__(master)

        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()

        position_top = int(screen_height / 3 - window_height / 3)
        position_right = int(screen_width / 2 - window_width / 2)

        # Set the position of the window to the center of the screen
        self.geometry(f"{window_width}x{window_height}+{position_right}+{position_top}")
        self.title("PATIENT-DASHBOARD (patient_main.py)")

        self.canvas = tk.Canvas(self, width=window_width, height=window_height)
        self.canvas.pack(fill=tk.BOTH, expand=True)

        image = Image.open('Images/patient_main_page.png')
        image = image.resize((window_width, window_height), Image.BICUBIC)
        self.image = ImageTk.PhotoImage(image) # Convert the PIL image to a PhotoImage

        self.canvas.create_image(0, 0, image=self.image, anchor='nw')
        
#-------------------------------------------------------------Buttons-------------------------------------------------------------------------------------------------------

        btns_width = 293
        btns_height = 124

        self.photo = ImageTk.PhotoImage(Image.open("Images/patient_main_profile_button.png").resize((btns_width, btns_height), Image.BICUBIC))
        self.photo1 = ImageTk.PhotoImage(Image.open("Images/patient_main_activity_button.png").resize((btns_width, btns_height), Image.BICUBIC))
        self.photo2 = ImageTk.PhotoImage(Image.open("Images/patient_main_logout_button.png").resize((btns_width, btns_height), Image.BICUBIC))


        self.pat_profile_button = Button(self,image=self.photo,borderwidth=0,highlightthickness=0,command=lambda: self.profile(username, password))
        self.pat_profile_button.place(width=btns_width,height=btns_height,x=454,y=161)

        self.activity_button = Button(self,image=self.photo1,borderwidth=0,highlightthickness=0,command=lambda: self.activity(username, password))
        self.activity_button.place(width=btns_width,height=btns_height,x=454,y=160+btns_height+62)

        self.logout_button = Button(self,image=self.photo2,borderwidth=0,highlightthickness=0,command=self.logout)
        self.logout_button.place(width=btns_width,height=btns_height,x=454,y=160+2*(btns_height+62)-1)



#-------------------------------------------------------Funtions----------------------------------------------------------------------------------------------------------

    def logout(self):
        if messagebox.askyesno("Alert","Are You sure you want to Logout?"):
           from patient import Patient
           self.withdraw()
           logout = Patient()
           logout.mainloop()


    def profile(self,username,password):
        from patient_profile import patient_Profile
        self.withdraw()
        profile = patient_Profile(username,password)
        profile.mainloop()


    def activity(self,username,password):
        from patient_activity import patient_activity
        self.withdraw()
        activity = patient_activity(username,password)
        activity.mainloop()

# if __name__ == "__main__":
#     app = pat_Main("Demo123","Demo123")
#     app.mainloop()
