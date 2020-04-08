from tkinter import *
from tkinter.ttk import *
import tkinter as tk
import tkinter.font as font
from tkinter import messagebox
import tkinter.ttk as ttk

from ModelObjects import *
from Controller import *
from PIL import ImageTk, Image
import os

background="#F1FBF7"

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
        
        fileMenu.add_command(label="New File", underline=1, command=lambda: self.new_file())
        fileMenu.add_command(label="Open File", underline=2, command=lambda: self.open_file("menu button", 0))
        fileMenu.add_command(label="Save", underline=3, command=lambda: self.save_file("save"))
        fileMenu.add_command(label="Save As", underline=4, command=lambda: self.save_file("saveas"))
        fileMenu.add_command(label="Exit", underline=5, command=self.exit_program)
        
        helpMenu.add_command(label="View Instructions", underline=1, command=self.view_help)
        
        self.root.config(menu=self.menubar, width="640", height="480")
        
        # Styling and Tkinter macOS bug adjustments
        self.font = "Roboto"
  
        self.root.option_add('*tearOff', FALSE)
        self.root.configure(width="640", height="480", background=background)
        style = Style()
        style.theme_use('classic') 
        style.configure("TButton", highlightcolor="#216657", \
                        background="#39A78E", foreground="white", \
                        relief="flat", font=(self.font, 15), width=25)        
        
        # Container window.
        self.main_frame = tk.Frame(self.root, width="640", height="480")
        self.main_frame.pack(side="top", fill="both", expand=True)
        self.main_frame.grid_rowconfigure(0, weight=1)
        self.main_frame.grid_columnconfigure(0, weight=1)
        
        self.projectInfo = tk.Label(self.root, text="Building No. ID:  0 (No File Loaded)", background=background, \
                                    font=(self.font, 12), anchor=W)
        self.projectInfo.pack(side="bottom", anchor="w", pady=(0,20))
        
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
        
        # Initializing helper frames here.
        frame4 = OpenFileScreen(parent=self.main_frame, controller=self)
        frame4.grid(row=0, column=0, sticky="nsew")
        self.frames["Open File"] = frame4
        
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
        
        self.config(background=background)
        self.controller = controller

        self.title= Label(self, text="Building Planner", width="55", \
                         foreground="white", background="#39A78E", \
                         font=(controller.font, 20), anchor=CENTER)
       
        self.MB_btn = Button(self, text="Manage Building", 
           style="TButton", command=lambda: controller.choose_frame("MB"))
        self.MF_btn = Button(self, text="Manage Floors", 
           style="TButton", command=lambda: controller.choose_frame("MF"))
        self.VCB_btn = Button(self, text="Visual Planner", 
           style="TButton", command=lambda: controller.choose_frame("VCB"))

        self.title.grid(row=0, column=0, columnspan=3, sticky="we")

        self.MB_btn.grid(row=1, column=0, sticky="we")
        self.MF_btn.grid(row=1, column=1, sticky="we")
        self.VCB_btn.grid(row=1, column=2, sticky="we")
        
        # Set up logo
        image = Image.open("building-icon.png")
        image = image.resize((200, 150), Image.ANTIALIAS)
        self.photo = ImageTk.PhotoImage(image)
        self.logo = Label(self, text="Logo", image=self.photo, background=background)
        self.logo.grid(row=2, column=0, sticky="NSEW", pady=(75,75), padx=(25,0))
     
        self.welcome = Label(self, text="\nWelcome to Building Manager v1.0!\n" +
        "\nHere, you can register a building or office to modify and manage workspaces." +
        "There is support for floor-plans, HVAC, furnishing and story/room costs.\n", 
            background=background #"#39A78E"
            , font=(controller.font,14, "bold"), 
            anchor=CENTER, wraplength=400, padding=0)
        self.welcome.grid(row=2, column=1, sticky="ew", columnspan=2)  

        self.getStarted = Label(self, text="Get Started: ", background=background, \
                                foreground="#39A78E", font=(controller.font, 20))
        self.getStarted.grid(row=3, column=0, sticky="we")
        
        self.gsMessage = Label(self, text="Create a new file or load a pre-existing one using the File menu in the top left of your screen.", \
            foreground="black", font=(controller.font, 12), background=background)
        self.gsMessage.grid(row=4, column=0, columnspan=3, sticky="we")
        
        return     

class ManageBuildingScreen(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, width="640", height="480", background=background)
        self.controller = controller 
        
        self.title= Label(self, text="Building Manager", \
                         foreground="white", background="#39A78E", width="55",\
                         font=(controller.font, 20), anchor=CENTER)        
        
        self.title.grid(row=0, column=0, columnspan=3, sticky="we")
        # self.title.place(relx=0.5, rely=0.0250, anchor=CENTER)
        
        self.HP_btn = Button(self, text="Home Page", 
           style="TButton", command=lambda: controller.choose_frame("HP"))        
        self.MF_btn = Button(self, text="Manage Floors", 
           style="TButton", command=lambda: controller.choose_frame("MF"))
        self.VCB_btn = Button(self, text="View Blueprint", 
           style="TButton", command=lambda: controller.choose_frame("VCB"))  
        
        self.HP_btn.grid(row=1, column=0, sticky="we")
        self.MF_btn.grid(row=1, column=1, sticky="we")
        self.VCB_btn.grid(row=1, column=2, sticky="we") 
        
        self.address = Label(self, text="Address: ", background=background, 
                         font=(controller.font, 15), anchor=CENTER, foreground="#39A78E")
        self.address.grid(row=2, column=0, sticky="we", pady=(25,0))  
        self.addressField = tk.Entry(self, background="white", font=(controller.font, 13), foreground="black")
        self.addressField.insert(0, "1055-A Forestwood Drive")
        self.addressField.config(state=DISABLED, disabledbackground=background)
        self.addressField.grid(row=2, column=1, sticky="we",  pady=(25,0))
        
        self.region = Label(self, text="Region: ", background=background, 
                         font=(controller.font, 15), anchor=CENTER, foreground="#39A78E")
        self.region.grid(row=3, column=0, sticky="we")  
        self.regionField = tk.Entry(self, background="white", font=(controller.font, 13), foreground="black")
        self.regionField.insert(0, "Missisauga, ON, Canada")
        self.regionField.config(state=DISABLED, disabledbackground=background)
        self.regionField.grid(row=3, column=1, sticky="we")
        
        self.postalCode = Label(self, text="Postal Code: ", background=background, 
                         font=(controller.font, 15), anchor=CENTER, foreground="#39A78E")
        self.postalCode.grid(row=4, column=0, sticky="we")  
        self.postalCode = tk.Entry(self, background="white", font=(controller.font, 13), foreground="black")
        self.postalCode.insert(0, "L5C 1T6")
        self.postalCode.config(state=DISABLED, disabledbackground=background)
        self.postalCode.grid(row=4, column=1, sticky="we")  
        
        self.totalStories = Label(self, text="Building Details: ", background=background, 
                         font=(controller.font, 15), anchor=CENTER, foreground="#39A78E")
        self.totalStories.grid(row=5, column=0, sticky="we")  
        self.totalStories = tk.Entry(self, background="white", font=(controller.font, 13), foreground="black")
        self.totalStories.insert(0, "Stories: 8 | Modifiable Floors: 7")
        self.totalStories.config(state=DISABLED, disabledbackground=background)
        self.totalStories.grid(row=5, column=1, sticky="we")
        
        self.totalCost = Label(self, text="Total Construction Cost: ", background=background, 
                         font=(controller.font, 15), anchor=CENTER, foreground="#39A78E")
        self.totalCost.grid(row=6, column=0, sticky="we")  
        self.totalCost = tk.Entry(self, background="white", font=(controller.font, 13), foreground="black")
        self.totalCost.insert(0, "$15, 647.97 CAD")
        self.totalCost.config(state=DISABLED, disabledbackground=background, disabledforeground="red")
        self.totalCost.grid(row=6, column=1, sticky="we")         
        
        self.addFloor = Button(self, text="Add Floor", command=lambda: controller.controller.model.currBuild.mod_story("add"))
        self.addFloor.grid(row=7, column=1, sticky="we", pady=(25,0))
        
        self.removeFloor = Button(self, text="Remove Floor", command=lambda: controller.controller.model.currBuild.mod_story("del"))
        self.removeFloor.grid(row=7, column=2, sticky="we", pady=(25,0))
    
        return    

class ManageFloorScreen(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, width="640", height="480", background=background)
        self.controller = controller
        
        self.title= Label(self, text="Floor Manager", width="55",
                         foreground="white", background="#39A78E", \
                         font=(controller.font, 20), anchor=CENTER)        
        
        self.title.grid(row=0, column=0, columnspan=3, sticky="we")
        #self.title.place(relx=0.5, rely=0.0250, anchor=CENTER, height=30)
        
        self.HP_btn = Button(self, text="Home Page", 
           style="TButton", command=lambda: controller.choose_frame("HP"))        
        self.MB_btn = Button(self, text="Manage Building", 
           style="TButton", command=lambda: controller.choose_frame("MB"))
        self.VCB_btn = Button(self, text="View Blueprint", 
           style="TButton", command=lambda: controller.choose_frame("VCB")) 
    
        
        self.HP_btn.grid(row=1, column=0, sticky="we")
        self.MB_btn.grid(row=1, column=1, sticky="we")
        self.VCB_btn.grid(row=1, column=2, sticky="we") 
            
        self.roomNum = Label(self, text="Room Number: ", background=background, 
                         font=(controller.font, 15), anchor=CENTER, foreground="#39A78E")  
        self.roomNumField = tk.Entry(self, background="white", font=(controller.font, 13), foreground="black")
        self.roomNum.grid(row=2, column=0, sticky="we", pady=(25,0))
        self.roomNumField.grid(row=2, column=1,  sticky="we", pady=(25,0))
        
        
        self.roomType = Label(self, text="Room Type: ", background=background, 
                         font=(controller.font, 15), anchor=CENTER, foreground="#39A78E")  
        self.roomTypeField = tk.Entry(self, background="white", font=(controller.font, 13), foreground="black")
        self.roomType.grid(row=3, column=0, sticky="we")  
        self.roomTypeField.grid(row=3, column=1, sticky="we")
        
        self.size = Label(self, text="Square Footage: ", background=background, \
                         font=(controller.font, 15), anchor=CENTER, foreground="#39A78E")
        self.size.grid(row=4, column=0, sticky="we")  
        self.sizeField = tk.Entry(self, background="white", font=(controller.font, 13), foreground="black")
        self.sizeField.grid(row=4, column=1, sticky="we")
        
        self.location = Label(self, text="Location: ", background=background, \
                         font=(controller.font, 15), anchor=CENTER, foreground="#39A78E")
        self.location.grid(row=5, column=0, sticky="we")  
        self.location = tk.Entry(self, background="white", font=(controller.font, 13), foreground="black")
        self.location.grid(row=5, column=1, sticky="we")  
        
        self.furnished = Label(self, text="Furnished: ", background=background, \
                         font=(controller.font, 15), anchor=CENTER, foreground="#39A78E")
        self.furnished.grid(row=6, column=0, sticky="we")  
        self.furnishedYes = tk.Radiobutton(self,  text = "Yes", background=background, value=True,
                    font=(controller.font, 15), anchor=CENTER, foreground="#39A78E")
        self.furnishedYes.grid(row=6, column=1, sticky="w")
        self.furnishedNo = tk.Radiobutton(self,  text = "No", background=background, value=False,
                    font=(controller.font, 15), anchor=CENTER, foreground="#39A78E")
        self.furnishedNo.grid(row=6, column=1, sticky="e")        
             

        self.addRoom = Button(self, text="Add Room", command=lambda: controller.controller.model.currBuild.mod_room("add"))
        self.addRoom.grid(row=7, column=1, sticky="we", pady=(20,10))
        
        self.removeRoom = Button(self, text="Remove Room", command=lambda: controller.controller.model.currBuild.mod_room("del"))
        self.removeRoom.grid(row=7, column=2, sticky="w", pady=(20,10))
        
        
        # self.tree = ttk.Treeview(self,
        #                          columns=('Room number','Room Type','Square Footage','Location'),show=["headings"])
     
        # self.tree.heading('#1', text='Room Number')
        # self.tree.heading('#2', text='Room Type')
        # self.tree.heading('#3', text='Square Footage')
        # self.tree.heading('#4', text='Location')
        
        # self.tree.column('#1', width="")
        # self.tree.column('#2', width="50")
        # self.tree.column('#0', width="50")
        # self.tree.column('#3', width="50")
        # self.tree.column('#4', width="50")
        # self.tree.grid(row=9, columnspan=3, sticky='nsew')
        # self.treeview = self.tree   
     
        #self.HP_btn.place(x=0, y=27)
        #self.MB_btn.place(x=230, y=27)
        #self.VCB_btn.place(x=470, y=27)         
    
        return      

class ViewBlueprintScreen(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, width="640", height="480", background=background)
        self.controller = controller
        self.dragInfo ={}
        self._drag_data = {"x": 0, "y": 0, "item": None}
        self.title= Label(self, text="Visual Floor Planner", width="55",\
                         foreground="white", background="#39A78E", \
                         font=(controller.font, 20), anchor=CENTER)        
        
        self.title.grid(row=0, column=0, columnspan=3, sticky="we")
        
        self.HP_btn = Button(self, text="Home Page", 
           style="TButton", command=lambda: controller.choose_frame("HP"))        
        self.MB_btn = Button(self, text="Manage Building", 
           style="TButton", command=lambda: controller.choose_frame("MB"))
        self.MF_btn = Button(self, text="Manage Floors", 
           style="TButton", command=lambda: controller.choose_frame("MF")) 
        
        self.HP_btn.grid(row=1, column=0, sticky="we")
        self.MB_btn.grid(row=1, column=1, sticky="we")
        self.MF_btn.grid(row=1, column=2, sticky="we")         
        
        self.item_label = Label(self, text="Floor-Plan Objects", \
                         foreground="black", background=background, \
                         font=(controller.font, 20), anchor="w")  
        self.item_label.grid(row=2, column=0)
        self.floorplan_label = Label(self, text="Floor-Plan Canvas", \
                         foreground="black", background=background, \
                         font=(controller.font, 20))  
        self.floorplan_label.grid(row=2, column=1, columnspan=2)
        
        #Canvas for the floor plan stuff, scrollbar for the floor plan items
        self.floorplan = tk.Canvas(self, width=360, height=500, background="#a7d8b8")
        self.item_canvas = tk.Canvas(self, width=100, height=500, background="#a7d8b8")
        self.item_canvas.grid(row=3, column=0, sticky="nsew") 
        self.floorplan.grid(row=3, column=1, columnspan=3, sticky="nsew" )

        scroll_y = tk.Scrollbar(self, orient="vertical", command=self.item_canvas.yview)
        scroll_y.grid(row=3, column=0, sticky="nse")
        self.item_canvas.configure(scrollregion=self.item_canvas.bbox("all"))
        self.item_canvas.configure(yscrollcommand=scroll_y.set)

        directory = 'images'
        self.draggers = []
        self.images = {} # Key: filename of image, Value: (Image, ImageTk.PhotoImage)
        y = 0
        for filename in os.listdir(directory):       

            self.image = Image.open("images/" + filename) 
            self.photo = ImageTk.PhotoImage(self.image)
            self.images[filename] = (self.image, self.photo)
            
            self.item_canvas.create_image(100, y, image=self.photo, tags=filename+"orig")
            self.item_canvas.tag_bind(filename +"orig", '<ButtonPress-1>', lambda event, arg=filename: self.make(event, arg))

            
            y+=(self.photo.height() + 50)
        self.item_canvas.configure(scrollregion=self.item_canvas.bbox("all"))

        self.hints = Label(self, text=
            "This screen is used to design potential layouts.\n"+
            "Click an object to add it to the floor plan. " +
            "Drag the object with the LEFT mouse button. "+
            "\nMouse over an object and RIGHT-CLICK to delete it." , \
                         foreground="black", background=background, \
                         font=(controller.font, 11, 'bold'), anchor="e")  
        self.hints.grid(row=4, column=0, columnspan=3)

        return 
    def make(self, event, filename):
        self.floorplan.create_image(300,100,image=self.images[filename][1], tags=filename, anchor="n")
        self.floorplan.tag_bind(filename, '<ButtonPress-1>', lambda event, arg=filename: self.drag_start(event, arg))
        self.floorplan.tag_bind(filename, '<B1-Motion>', lambda event: self.drag(event))
        self.floorplan.tag_bind(filename, '<ButtonRelease-1>', lambda event: self.drag_stop(event))
        self.floorplan.tag_bind(filename, '<ButtonPress-2>', lambda event, arg=filename: self.delete_canvas_item(event, arg))
        self.floorplan.tag_bind(filename, '<ButtonPress-3>', lambda event, arg=filename: self.delete_canvas_item(event, arg))
 
    def delete_canvas_item(self, event, filename):
       self.floorplan.delete(event.widget.find_withtag('current')[0])
    def drag_start(self, event, filename):
        """Begining drag of an object"""
        # # record the item and its location
        self._drag_data["item"] = self.floorplan.find_closest(event.x, event.y)[0]
        self._drag_data["x"] = event.x
        self._drag_data["y"] = event.y

    def drag_stop(self, event):
        """End drag of an object"""
        # reset the drag information
        self._drag_data["item"] = None
        self._drag_data["x"] = 0
        self._drag_data["y"] = 0
        

    def drag(self, event):
        """Handle dragging of an object"""
        # compute how much the mouse has moved
       
        delta_x = event.x - self._drag_data["x"]
        delta_y = event.y - self._drag_data["y"]
        # move the object the appropriate amount
        self.floorplan.move(self._drag_data["item"], delta_x, delta_y)
        # record the new position
        self._drag_data["x"] = event.x
        self._drag_data["y"] = event.y


class OpenFileScreen(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, width="640", height="480")
        self.controller = controller
        
        self.title= Label(self, text="Open File", width="55",\
                         foreground="white", background="#39A78E", \
                         font=(controller.font, 20), anchor=CENTER)        
        self.title.grid(row=0, column=0, columnspan=3, sticky="we")
        
        self.HP_btn = Button(self, text="Back to Home Page", 
           style="TButton", command=lambda: controller.choose_frame("HP"))        
        self.HP_btn.grid(row=1, column=0, columnspan=3, sticky="we")
        
        valBuildNum = (self.register(self.is_Num), "%S")
        self.enterNum = Label(self, text="Enter Building ID No. Here: ", anchor=W)
        self.enterNum.grid(row=3, column=0, sticky="we")
        
        self.numForm = tk.Entry(self, background="white", font=(controller.font, 13), foreground="black")
        self.numForm.config(validate="key", validatecommand=valBuildNum)
        self.numForm.grid(row=3, column=1, sticky="we")
        
        self.accept_btn = Button(self, text="Accept", style="TButton", command=self.submit)
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


