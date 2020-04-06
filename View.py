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
        
        fileMenu.add_command(label="New File", underline=1, command=lambda: self.new_file("menu button"))
        fileMenu.add_command(label="Open File", underline=2, command=lambda: self.open_file("menu button", 0))
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
        
        self.projectInfo = tk.Label(self.root, text="Building No. ID:  0 (No File Loaded)", \
                                    font=(self.font, 12), anchor=W)
        self.projectInfo.pack(side="bottom", anchor="w")
        
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
        
        frame4 = OpenFileScreen(parent=self.main_frame, controller=self)
        frame4.grid(row=0, column=0, sticky="nsew")
        self.frames["Open File"] = frame4
        
        # Initializing helper frames here.
        #pass
        
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
    
    def open_file(self, caller, num):
        self.chosen_building = num
        if (caller == "menu button"):
            self.go_Screen("Open File")
            return
        
        elif (caller == "submit button"):
            self.controller.set_up("open file")
            self.choose_frame("HP")            
        
        # CHANGES REQUIRED:
        # Open pop-up window with selectable drop-down menu asking for Building
        # Number. Each option should have number and address present on the 
        # same line. Update self.chosen_building after selection.

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

        self.title= Label(self, text="Building Planner", width="55", \
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
        
        # Blank Row 1 
        # (filler space)
        self.br1 = Label(self, text=" ", background="white", \
                         font=(controller.font, 100))
        self.br1.grid(row=2, column=1)
        
        self.welcome = Label(self, text="Welcome to Building Manager v1.0!", 
                             background="light gray", foreground="black",\
                             font=(controller.font, 12), anchor=CENTER)
        
        self.welcome2 = Label(self, text="Here, you can register a building or office", \
                              background="light gray", foreground="black",\
                              font=(controller.font, 12), anchor=W)
        
        self.welcome3 = Label(self, text="lease to modify and manage workspaces, ", \
                             background="light gray", foreground="black",\
                             font=(controller.font, 12), anchor=W)  
        
        self.welcome4 = Label(self, text="floor-plans, blueprints, HVAC, furnishing, ", \
                              background="light gray", foreground="black",\
                              font=(controller.font, 12), anchor=W)
        
        self.welcome5 = Label(self, text="and story/room costs.", \
                              background="light gray", foreground="black",\
                              font=(controller.font, 12), anchor=W)                              

        self.welcome.grid(row=4, column=1, sticky="we")   
        self.welcome2.grid(row=5, column=1, sticky="we")
        self.welcome3.grid(row=6, column=1, sticky="we")
        self.welcome4.grid(row=7, column=1, sticky="we")
        self.welcome5.grid(row=8, column=1, sticky="we")
        
        # Blank Row 2
        self.br2 = Label(self, text=" ", background="white", \
                         font=(controller.font, 100))
        self.br2.grid(row=9, column=0)    
        
        self.getStarted = Label(self, text="Get Started: ", background="white", \
                                foreground="blue", font=(controller.font, 20))
        self.getStarted.grid(row=10, column=0, sticky="we")
        
        self.gsMessage = Label(self, text="Create a new file or load a pre-existing one using the File menu in the top left of your screen.", \
                               foreground="black", font=(controller.font, 12), \
                               background="white")
        self.gsMessage.grid(row=11, column=0, columnspan=3, sticky="we")
        
        return     

class ManageBuildingScreen(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, width="640", height="480")
        self.controller = controller 
        
        self.title= Label(self, text="Building Manager", \
                         foreground="white", background="#39A78E", width="55",\
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
        
        #Blank Row 1
        self.br1 = Label(self, text=" ", background="white", \
                         font=(controller.font, 100))
        self.br1.grid(row=9, column=0)          
        
        self.address = Label(self, text="Address: ", background="white", \
                         font=(controller.font, 15), anchor=E, foreground="blue")
        self.address.grid(row=2, column=0, sticky="we")  
        self.addressField = Entry(self, foreground="black")
        self.addressField.insert(0, "1055-A Forestwood Drive")
        self.addressField.config(state=DISABLED)
        self.addressField.grid(row=2, column=1, sticky="we")
        
        self.region = Label(self, text="Region: ", background="white", \
                         font=(controller.font, 15), anchor=E, foreground="blue")
        self.region.grid(row=3, column=0, sticky="we")  
        self.regionField = Entry(self, foreground="black")
        self.regionField.insert(0, "Missisauga, ON, Canada")
        self.regionField.config(state=DISABLED)
        self.regionField.grid(row=3, column=1, sticky="we")
        
        self.postalCode = Label(self, text="Postal Code: ", background="white", \
                         font=(controller.font, 15), anchor=E, foreground="blue")
        self.postalCode.grid(row=4, column=0, sticky="we")  
        self.postalCode = Entry(self, foreground="black")
        self.postalCode.insert(0, "L5C 1T6")
        self.postalCode.config(state=DISABLED)
        self.postalCode.grid(row=4, column=1, sticky="we")  
        
        self.totalStories = Label(self, text="Building Details: ", background="white", \
                         font=(controller.font, 15), anchor=E, foreground="blue")
        self.totalStories.grid(row=5, column=0, sticky="we")  
        self.totalStories = Entry(self, foreground="black")
        self.totalStories.insert(0, "Stories: 8 | Modifiable Floors: 7")
        self.totalStories.config(state=DISABLED)
        self.totalStories.grid(row=5, column=1, sticky="we")
        
        self.totalCost = Label(self, text="Total Construction Cost: ", background="white", \
                         font=(controller.font, 15), anchor=E, foreground="red")
        self.totalCost.grid(row=6, column=0, sticky="we")  
        self.totalCost = Entry(self, foreground="red")
        self.totalCost.insert(0, "$15, 647.97 CAD")
        self.totalCost.config(state=DISABLED)
        self.totalCost.grid(row=6, column=1, sticky="we")         
        
        self.addFloor = Button(self, text="Add Floor", command=lambda: self.controller.model.b1.mod_story("add"))
        self.addFloor.grid(row=7, column=2, sticky="we")
        
        self.removeFloor = Button(self, text="Remove Floor", command=lambda: self.controller.model.b1.mod_story("del"))
        self.removeFloor.grid(row=8, column=2, sticky="we")
    
        return    

class ManageFloorScreen(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, width="640", height="480")
        self.controller = controller
        
        self.title= Label(self, text="Floor Manager", width="56",
                         foreground="white", background="#39A78E", \
                         font=(controller.font, 20), anchor=CENTER)        
        
        #self.title.grid(row=0, column=0, columnspan=3, sticky="we")
        self.title.place(relx=0.5, rely=0.0250, anchor=CENTER, height=30)
        
        self.HP_btn = Button(self, text="Home Page", 
           style="TButton", command=lambda: controller.choose_frame("HP"))        
        self.MB_btn = Button(self, text="Manage Building", 
           style="TButton", command=lambda: controller.choose_frame("MB"), \
           width="21")
        self.VCB_btn = Button(self, text="View Current Blueprint", 
           style="TButton", command=lambda: controller.choose_frame("VCB"), \
           width="23")  
        
        #self.HP_btn.grid(row=1, column=0, sticky="we")
        #self.MB_btn.grid(row=1, column=1, sticky="we")
        #self.VCB_btn.grid(row=1, column=2, sticky="we") 
        
        self.HP_btn.place(x=0, y=27)
        self.MB_btn.place(x=230, y=27)
        self.VCB_btn.place(x=470, y=27)         
    
        return    

class ViewBlueprintScreen(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, width="640", height="480")
        self.controller = controller
        
        self.title= Label(self, text="Floor-Plan Blueprint Viewer", width="55",\
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

class OpenFileScreen(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, width="640", height="480")
        self.controller = controller
        
        self.title= Label(self, text="Open File", width="55",\
                         foreground="white", background="#39A78E", \
                         font=(controller.font, 20), anchor="center")        
        self.title.grid(row=0, column=0, columnspan=3)
        
        self.HP_btn = Button(self, text="Back to Home Page", 
           style="TButton", command=lambda: controller.choose_frame("HP"))        
        self.HP_btn.grid(row=1, column=0, columnspan=3, sticky="we")
        
        #Blank Row 1
        self.br1 = Label(self, text=" ", background="white", \
                         font=(controller.font, 100))
        self.br1.grid(row=2, column=0)         
        
        valBuildNum = (self.register(self.is_Num), "%S")
        self.enterNum = Label(self, text="Enter Building ID No. Here: ", anchor=W, \
                              validate="key", validatecommand=valBuildNum)
        self.enterNum.grid(row=3, column=0, sticky="we")
        
        self.numForm = Entry(self, anchor=W, )
        self.numForm.grid(row=3, column=1, sticky="we")
        
        self.accept_btn = Button(self, text="Accept", style="TButton", \
                                 command=self.submit, anchor=CENTER)
        self.accept_btn.grid(row=4, column=1, sticky="we")
    
        return
    
    def is_Num(self, d, V):
        if (d.isdigit()):
            return True
        
        return False 
    
    def submit(self):
        if (len(self.numForm.get()) > 0):
            controller.open_file("submit button", self.numForm.get())
        
        return