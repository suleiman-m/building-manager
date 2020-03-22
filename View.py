from tkinter import *
from tkinter.ttk import *
import tkinter as tk
import tkinter.font as font

from tkinter import messagebox

# from model import *
# from controller import *


''' The visual interface for the application'''
class View():

    def __init__(self, root, controller):
        
        # The controller passes an instance of itself as well as the top level root
        self.controller = controller
        self.root = root
      
         # Styling and Tkinter macOS bug adjustments
        self.font = "Roboto"
        self.background="#F1FBF7"
        self.root.option_add('*tearOff', FALSE)
        self.root.configure(background=self.background)
        style = Style()
        style.theme_use('classic') 
        style.configure("TButton",
            highlightcolor="#216657", background="#39A78E", 
            foreground="white", relief="flat", font=(self.font, 15), width=20)


        self.home_page = tk.Frame(self.root, background=self.background)
     

        self.title= Label(self.home_page, text="Building Planner", foreground="white",
        background="#39A78E", font=(self.font, 20))

        self.new_btn = Button(self.home_page, text="New Building", 
            style="TButton", command=self.temporary_command)
        self.import_btn = Button(self.home_page, text="Import", 
            style="TButton", command=self.temporary_command)
        self.exit_btn = Button(self.home_page, text="Exit", 
            style="TButton", command=self.temporary_command)

        self.home_page.grid()
        self.title.grid()

        self.new_btn.grid(pady=10)
        self.import_btn.grid(pady=10)
        self.exit_btn.grid(pady=10)

    def temporary_command(self):
        pass