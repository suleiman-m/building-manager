from tkinter import *
from tkinter.ttk import *
import tkinter as tk
import tkinter.font as font
from tkinter import messagebox

from ModelObjects import *
from Controller import *

''' The visual interface for the application.'''
class View():

    def __init__(self, root, controller):
        
        # The controller passes an instance of itself as well as the top level root
        self.controller = controller
        self.root = root
        
        # Menu bars
        self.menubar = Menu(self.root)
        fileMenu = Menu(self.menubar, tearoff=False)
        helpMenu = Menu(self.menubar, tearoff=False)
        self.menubar.add_cascade(label="File", underline=0, menu=fileMenu)
        self.menubar.add_cascade(label="Help", underline=0, menu=helpMenu)
        
        fileMenu.add_command(label="New File", underline=1, command=lambda: self.new_file)
        fileMenu.add_command(label="Open File", underline=2, command=lambda: self.open_file)
        fileMenu.add_command(label="Save", underline=3, command=lambda: self.save_file("save"))
        fileMenu.add_command(label="Save As", underline=4, command=lambda: self.save_file("saveas"))
        fileMenu.add_command(label="Exit", underline=5, command=self.exit_program)
        
        helpMenu.add_command(label="View Instructions", underline=1, command=self.view_help)
        
        self.root.config(menu=self.menubar, width="640", height="480")
        
        # Styling and Tkinter macOS bug adjustments
        self.font = "Roboto"
        self.background="#F1FBF7"
        self.root.option_add('*tearOff', FALSE)
        self.root.configure(width="640", height="480", background=self.background)
        style = Style()
        style.theme_use('classic') 
        style.configure("TButton", highlightcolor="#216657", \
                        background="#39A78E", foreground="white", \
                        relief="flat", font=(self.font, 15), width=20)        
        
        # Container window.
        self.main_frame = tk.Frame(self.root, width="640", height="480")
        self.main_frame.pack(side="top", fill="both", expand=True)
        self.main_frame.grid_rowconfigure(0, weight=1)
        self.main_frame.grid_columnconfigure(0, weight=1)
        
        # Initializing the four main frames here.
        self.frames = {}
        frame0 = HomePage(parent=self.main_frame, controller=self)
        frame0.grid(row=0, column=0, sticky="nsew")
        self.frames["Home Page"] = frame0
        frame1 = ManageBuildingScreen(parent=self.main_frame, controller=self)
        frame1.grid(row=0, column=0, sticky="nsew")
        self.frames["Building Manager"] = frame1
        frame2 = ManageFloorScreen(parent=self.main_frame, controller=self)
        frame2.grid(row=0, column=0, sticky="nsew")
        self.frames["Floor Manager"] = frame2
        frame3 = ViewBlueprintScreen(parent=self.main_frame, controller=self)
        frame3.grid(row=0, column=0, sticky="nsew")
        self.frames["Floor-Plan Blueprint Viewer"] = frame3
        
        self.goScreen("Home Page")
        
        return
    
    def goScreen(self, screenName):
        frame = self.frames[screenName]
        frame.tkraise()
        
        return    

    def choose_frame(self, button_name):
        #if (self.controller.values_loaded == False):
            # Give pop-up error message saying: 
            #
            # "ERROR: A building must first be loaded. To load a building plan, 
            # either create a new one or select a pre-existing one, using
            # the File menu located at the top left of your screen in the menu
            # bar for this program."
            #
            # Provide button to close the error message.
            #return
        
        # Communicate directly to ModelObjects.py within each of these frames
        # when modifying floors, rooms, or furniture.
        if (button_name == "MB"):
            self.goScreen("Building Manager")
        elif (button_name == "MF"):
            self.goScreen("Floor Manager")
        elif (button_name == "VCB"):
            self.goScreen("Floor-Plan Blueprint Viewer")
        elif (button_name == "HP"):
            self.goScreen("Home Page")
        
        return 
    
    def view_help(self):
        # Open pop-up window for help instructions. Include close button.
        
        return
    
    def save_file(self, option, mode):
        if (mode == "save"):
            # If file has not been saved yet (0), do a save as.
            if (self.controller.savestatus == 0):
                self.save_file("saveas")
            # If file has been saved (1)
            elif (self.controller.savestatus == 1):
                self.controller.csave_file("save")              
        elif (mode == "saveas"):
            self.controller.csave_file("first save")
            
        return 
    
    def new_file(self):
        self.new_building_details = []
        # Open pop-up form asking user to fill out and submit initial details.
        # Store info in self.new_building_details array.
        self.controller.set_up("new file")
        
        return
    
    def open_file(self):
        self.chosen_building = 0
        # Open pop-up window with selectable drop-down menu asking for Building
        # Number. Each option should have number and address present on the 
        # same line. Update self.chosen_building
        self.controller.set_up("open file")
        
        return
    
    def exit_program(self):
        # Implement pop-up "Are you sure you want to quit?" check.
        # Notify user if any changes were made after most recent save time.
        #         Use self.controller.savetime to get this value.
        # Button Options: "Yes", "No", "Cancel".
        # Destroy all temporary files if any were made.
        
        return
    
class HomePage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, width="640", height="480")
        self.controller = controller

        self.title= Label(self, text="Building Planner", width="54", \
                         foreground="white", background="#39A78E", \
                         font=(controller.font, 20), anchor=CENTER)
       
        self.MB_btn = Button(self, text="Manage Building", 
           style="TButton", command=lambda: controller.choose_frame("MB"))
        self.MF_btn = Button(self, text="Manage Floors", 
           style="TButton", command=lambda: controller.choose_frame("MF"))
        self.VCB_btn = Button(self, text="View Current Blueprint", 
           style="TButton", command=lambda: controller.choose_frame("VCB"))

        self.title.grid(row=0, column=0, columnspan=3)

        self.MB_btn.grid(row=1, column=0, sticky="we")
        self.MF_btn.grid(row=1, column=1, sticky="we")
        self.VCB_btn.grid(row=1, column=2, sticky="we")        
    
        return     

class ManageBuildingScreen(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, width="640", height="480")
        self.controller = controller 
        
        self.title= Label(self, text="Building Manager", \
                         foreground="white", background="#39A78E", width="54",\
                         font=(controller.font, 20), anchor=CENTER)        
        
        self.title.grid(row=0, column=0, columnspan=3, sticky="we")
        #self.title.place(relx=0.5, rely=0.0250, anchor=CENTER)
        
        self.HP_btn = Button(self, text="Home Page", 
           style="TButton", command=lambda: controller.choose_frame("HP"))        
        self.MF_btn = Button(self, text="Manage Floors", 
           style="TButton", command=lambda: controller.choose_frame("MF"))
        self.VCB_btn = Button(self, text="View Current Blueprint", 
           style="TButton", command=lambda: controller.choose_frame("VCB"))  
        
        self.HP_btn.grid(row=1, column=0, sticky="we")
        self.MF_btn.grid(row=1, column=1, sticky="we")
        self.VCB_btn.grid(row=1, column=2, sticky="we")                
    
        return    

class ManageFloorScreen(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, width="640", height="480")
        self.controller = controller
        
        self.title= Label(self, text="Floor Manager", width="54",
                         foreground="white", background="#39A78E", \
                         font=(controller.font, 20), anchor=CENTER)        
        
        self.title.grid(row=0, column=0, columnspan=3, sticky="we")
        # self.title.place(relx=0.5, rely=0.0250, anchor=CENTER, height=30)
        
        self.HP_btn = Button(self, text="Home Page", 
           style="TButton", command=lambda: controller.choose_frame("HP"))        
        self.MB_btn = Button(self, text="Manage Building", 
           style="TButton", command=lambda: controller.choose_frame("MB"))
        self.VCB_btn = Button(self, text="View Current Blueprint", 
           style="TButton", command=lambda: controller.choose_frame("VCB"))  
        
        self.HP_btn.grid(row=1, column=0, sticky="we")
        self.MB_btn.grid(row=1, column=1, sticky="we")
        self.VCB_btn.grid(row=1, column=2, sticky="we")        
    
        return    

class ViewBlueprintScreen(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, width="640", height="480")
        self.controller = controller
        
        self.title= Label(self, text="Floor-Plan Blueprint Viewer", width="54",\
                         foreground="white", background="#39A78E", \
                         font=(controller.font, 20), anchor="center")        
        
        self.title.grid(row=0, column=0, columnspan=3)
        
        self.HP_btn = Button(self, text="Home Page", 
           style="TButton", command=lambda: controller.choose_frame("HP"))        
        self.MB_btn = Button(self, text="Manage Building", 
           style="TButton", command=lambda: controller.choose_frame("MB"))
        self.MF_btn = Button(self, text="Manage Floors", 
           style="TButton", command=lambda: controller.choose_frame("MF")) 
        
        self.HP_btn.grid(row=1, column=0, sticky="we")
        self.MB_btn.grid(row=1, column=1, sticky="we")
        self.MF_btn.grid(row=1, column=2, sticky="we")         
    
        return