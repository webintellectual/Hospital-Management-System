import tkinter as tk
from tkinter import messagebox
from tkinter import *
from PIL import Image, ImageTk
from constants import *



class Admin_Main(tk.Toplevel):
    def __init__(self,username,password, master=None):
        super().__init__(master)

        btns_width = 269
        btns_height = 123
        left_offset = 94
        h_gap = 77
        top_offset = 198
        v_gap = 50

        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()

        position_top = int(screen_height / 3 - window_height / 3)
        position_right = int(screen_width / 2 - window_width / 2)

        # Set the position of the window to the center of the screen
        self.geometry(f"{window_width}x{window_height}+{position_right}+{position_top}")
        self.title("ADMIN-DASHBOARD (admin_main.py)")

        self.canvas = tk.Canvas(self, width=window_width, height=window_height)
        self.canvas.pack(fill=tk.BOTH, expand=True)

        image = Image.open('Images/Admin_Main.png')
        image = image.resize((window_width, window_height), Image.BICUBIC)
        self.image = ImageTk.PhotoImage(image) # Convert the PIL image to a PhotoImage

        self.canvas.create_image(0, 0, image=self.image, anchor='nw')

#----------------------------------------------------Buttons-----------------------------

        self.photo = ImageTk.PhotoImage(Image.open("Images/Admin_profile_button.png").resize((btns_width, btns_height), Image.BICUBIC))
        self.photo1 = ImageTk.PhotoImage(Image.open("Images/Admin_doctors_button.png").resize((btns_width, btns_height), Image.BICUBIC))
        self.photo2 = ImageTk.PhotoImage(Image.open("Images/Admin_add_doctors_button.png").resize((btns_width, btns_height), Image.BICUBIC))
        self.photo3 = ImageTk.PhotoImage(Image.open("Images/Admin_edit_doctors_button.png").resize((btns_width, btns_height), Image.BICUBIC))
        self.photo4 = ImageTk.PhotoImage(Image.open("Images/Admin_equipments_button.png").resize((btns_width, btns_height), Image.BICUBIC))
        self.photo5 = ImageTk.PhotoImage(Image.open("Images/Admin_feedback_button.png").resize((btns_width, btns_height), Image.BICUBIC))
        self.photo6 = ImageTk.PhotoImage(Image.open("Images/Admin_logout_button.png").resize((btns_width, btns_height), Image.BICUBIC))


        self.adm_profile_button = Button(self,image=self.photo,borderwidth=0,highlightthickness=0,command=lambda: self.profile(username, password))
        self.adm_profile_button.place(width=btns_width,height=btns_height,x=left_offset,y=top_offset)

        self.adm_doctors_button = Button(self,image=self.photo1,borderwidth=0,highlightthickness=0,command=lambda: self.doctors(username, password))
        self.adm_doctors_button.place(width=btns_width,height=btns_height,x=left_offset+btns_width+h_gap,y=top_offset)

        self.adm_add_doctor_button = Button(self,image=self.photo2,borderwidth=0,highlightthickness=0,command=lambda: self.add_doctors(username, password))
        self.adm_add_doctor_button.place(width=btns_width,height=btns_height,x=left_offset+(2*btns_width)+(2*h_gap),y=top_offset)

        self.adm_edit_doctor_button = Button(self,image=self.photo3,borderwidth=0,highlightthickness=0,command=lambda: self.edit_doctors(username, password))
        self.adm_edit_doctor_button.place(width=btns_width,height=btns_height,x=left_offset,y=top_offset+btns_height+v_gap)

        self.adm_feedback_button = Button(self,image=self.photo5,borderwidth=0,highlightthickness=0,command=lambda: self.feedback(username, password))
        self.adm_feedback_button.place(width=btns_width,height=btns_height,x=left_offset+btns_width+h_gap,y=top_offset+btns_height+v_gap)

        self.adm_logout_button = Button(self,image=self.photo6,borderwidth=0,highlightthickness=0,command=self.logout)
        self.adm_logout_button.place(width=btns_width,height=btns_height,x=left_offset+(2*btns_width)+2*h_gap,y=top_offset+(btns_height)+v_gap)


# -------------------------------------------------------------- Functions ------------------------------------------------------------------

    def logout(self):
        if messagebox.askyesno("Alert","Are You sure you want to Logout?"):
           from admin import Admin
           self.withdraw()
           logout = Admin()
           logout.mainloop()

    def profile(self,username,password):
        from admin_profile import Admin_Profile
        self.withdraw()
        profile = Admin_Profile(username,password)
        profile.mainloop()

    def doctors(self,username,password):
        from admin_doctors import Admin_doctors
        self.withdraw()
        doctors = Admin_doctors(username,password)
        doctors.mainloop()

    def add_doctors(self,username,password):
        from admin_add_doctors import Admin_add_doctors
        self.withdraw()
        add_doctors = Admin_add_doctors(username,password)
        add_doctors.mainloop()

    def edit_doctors(self,username,password):
        from admin_edit_doctors import Admin_edit_doctors
        self.withdraw()
        edit_doctors = Admin_edit_doctors(username,password)
        edit_doctors.mainloop()

    def feedback(self,username,password):
        from admin_feedback import Admin_feedback
        self.withdraw()
        feedback = Admin_feedback(username,password)
        feedback.mainloop()

# if __name__ == "__main__":
#     app = Admin_Main("Demo123","Demo123")
#     app.mainloop()