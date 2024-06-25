import tkinter as tk
from tkinter import messagebox
from tkinter import *
from PIL import Image, ImageTk
# from tkinter import font
from app_main import HMS
from constants import *

class facility(tk.Toplevel):
    def __init__(self,master=None):
        super().__init__(master)

        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()

        position_top = int(screen_height / 3 - window_height / 3)
        position_right = int(screen_width / 2 - window_width / 2)

        # Set the position of the window to the center of the screen
        self.geometry(f"{window_width}x{window_height}+{position_right}+{position_top}")
        self.title("FITNESS CENTER (facility.py)")

        self.canvas = tk.Canvas(self, width=window_width, height=window_height)
        self.canvas.pack(fill=tk.BOTH, expand=True)

        image = Image.open('Images/facilities.png')
        image = image.resize((window_width, window_height), Image.BICUBIC)
        self.image = ImageTk.PhotoImage(image) # Convert the PIL image to a PhotoImage

        self.canvas.create_image(-5, 0, image=self.image, anchor='nw')

        self.protocol("WM_DELETE_WINDOW", self.Exit)
        
        # inter_font = font.Font(family="Inter")

#----------------------------------------Buttons------------------------------------------------------------------------------------
        self.photo = ImageTk.PhotoImage(Image.open("Images/Home.png").resize((header_buttons_width, header_buttons_height), Image.BICUBIC))
        self.photo1 = ImageTk.PhotoImage(Image.open("Images/About.png").resize((header_buttons_width, header_buttons_height), Image.BICUBIC))
        self.photo2 = ImageTk.PhotoImage(Image.open("Images/Facility.png").resize((header_buttons_width, header_buttons_height), Image.BICUBIC))
        self.photo3 = ImageTk.PhotoImage(Image.open("Images/Contact_us.png").resize((header_buttons_width, header_buttons_height), Image.BICUBIC))
        self.photo4 = ImageTk.PhotoImage(Image.open("Images/Feedback.png").resize((header_buttons_width, header_buttons_height), Image.BICUBIC))

        self.homebutton = Button(self,borderwidth=0,highlightthickness=0,image=self.photo,command=self.open_home)
        self.homebutton.place(width=header_buttons_width,height=header_buttons_height,x=left_offset-2,y=header_buttons_y)

        self.aboutbutton = Button(self,borderwidth=0,highlightthickness=0,image=self.photo1,command=self.about)
        self.aboutbutton.place(width=header_buttons_width,height=header_buttons_height,x=left_offset-2+header_buttons_width,y=header_buttons_y)

        self.facilitybutton = Button(self,borderwidth=0,highlightthickness=0,image=self.photo2,command=self.facility)
        self.facilitybutton.place(width=header_buttons_width,height=header_buttons_height,x=left_offset-2+(2*header_buttons_width),y=header_buttons_y)
        
        self.contact_usbutton = Button(self,borderwidth=0,highlightthickness=0,image=self.photo3,command=self.contact_us)
        self.contact_usbutton.place(width=header_buttons_width,height=header_buttons_height,x=left_offset-2+(3*header_buttons_width),y=header_buttons_y)

        self.feedbackbutton = Button(self,borderwidth=0,highlightthickness=0,image=self.photo4,command=self.feedback)
        self.feedbackbutton.place(width=header_buttons_width-3,height=header_buttons_height,x=left_offset-2+(4*header_buttons_width),y=header_buttons_y)


    def Exit(self):
        if messagebox.askyesno("Exit","Are You sure you want to exit?"):
            self.destroy()


    def open_home(self):
        self.destroy()
        self.master.destroy()
        back = HMS()
        back.mainloop()


    def about(self):
        from about import About
        self.withdraw()
        about = About()
        about.mainloop()

    
    def facility(self):
        self.destroy()
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

# if __name__ == "__main__":
#     app = facility()
#     app.mainloop()
