import tkinter as tk
from tkinter import ttk
from tkinter import *
from PIL import Image, ImageTk
# from tkinter import font
from constants import *
import csv
from file_manager import FileManager

class Admin_feedback(tk.Toplevel):
    def __init__(self,username,password, master=None):
        super().__init__(master)

        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()

        position_top = int(screen_height / 3 - window_height / 3)
        position_right = int(screen_width / 2 - window_width / 2)

        # Set the position of the window to the center of the screen
        self.geometry(f"{window_width}x{window_height}+{position_right}+{position_top}")
        self.title("ADMIN-FEEDBACK (admin_feedback.py)")

        self.canvas = tk.Canvas(self, width=window_width, height=window_height)
        self.canvas.pack(fill=tk.BOTH, expand=True)

        image = Image.open('Images/Admin_feedback.png')
        image = image.resize((window_width, window_height), Image.BICUBIC)
        self.image = ImageTk.PhotoImage(image) # Convert the PIL image to a PhotoImage

        self.canvas.create_image(0, 0, image=self.image, anchor='nw')

        # inter_font = font.Font(family="Inter")

        self.file_manager = FileManager()
        
#--------------------------------------- BUTTON/ Labels ------------------------------------------------------------

        self.photo1 = ImageTk.PhotoImage(Image.open("Images/back_button.png").resize((45, 30), Image.BICUBIC))

        self.backbutton = Button(self,image=self.photo1,borderwidth=0,highlightthickness=0,command=lambda: self.back_button(username, password))
        self.backbutton.place(width=45,height=30,x=22.5,y=21)


#---------------------------------CSV / TREE VIEW and Data labels --------------------------------------------------
        self.treeview = ttk.Treeview(self,columns=("Name","Email","Feedback"))

        self.treeview.heading("Name",text="Name")
        self.treeview.heading("Email",text="Email")
        self.treeview.heading("Feedback",text="Feedback")

        self.treeview.column("#0", width=0, stretch=tk.NO)
        self.treeview.column("Name",anchor="center",width=150)
        self.treeview.column("Email",anchor="center",width=150)
        self.treeview.column("Feedback",anchor="center",width=150)

        # self.import_data()
        self.file_manager.fetch_feedbacks(self)

        self.treeview.place(x=102,y=160,width=1000,height=480)
            

#---------------------------------------------------FUNCTIONS-----------------------------------------------------------------------
    # def import_data(self):
    #     with open('database/feedback.csv', 'r') as csv_file:
    #         reader = csv.DictReader(csv_file)
    #         for row in reader:
    #             self.treeview.insert("", "end", values=(row['name'], row['email'], row['feedback']))


    def back_button(self,username, password):
        from admin_main import Admin_Main
        self.withdraw()
        back = Admin_Main(username, password)
        back.mainloop()

# if __name__ == "__main__":
#     app = Admin_feedback(username="Demo123", password="Demo123")
#     app.mainloop()