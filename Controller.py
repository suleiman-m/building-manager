from datetime import datetime

from View import *
from ModelObjects import *

import tkinter as tk
from tkinter.ttk import *
from tkinter import filedialog

'''Creates the model, view, and controller for the application and runs it.

====NOTES====
All files are located in one folder. The naming convention accounts for each 
corresponding building number. 

Creating a new file or opening an existing file should require an 
"Are you sure you wish to proceed?" check, because doing so will overwrite all 
the currently stored data in Model.
'''
class Controller:
    
    def __init__(self):
        self.root = tk.Tk()
        # Initial launch no building file is loaded (frames locked).
        self.values_loaded = False
        # File not yet saved on first launch.
        self.savestatus = 0
        # Temporary initial placeholder for attribute. Updated in csave_file().
        self.savetime = datetime.now().strftime("%H:%M:%S")
        
        self.root.title("building-manager v1.0")
        self.root.configure(width="640", height="480")
        self.view = View(self.root, self)
        self.root.mainloop()
    
    def set_up(self, mode):
        # If-statement avoids attribute not yet being initialized error.
        if (mode == "new file"):
            self.building_details = self.view.new_building_details
        elif (mode == "open file"):
            self.chosen_building = self.view.chosen_building  
            
        self.model = ModelObjects.Model(self, mode)
        self.values_loaded = True
        
        return
    
    def csave_file(self, mode):
        if (mode == "save"):
            # Write all current values from ModelObjects.py to appropriate 
            # floors.csv and rooms.csv files.               
            pass
        elif (mode == "first save"):
            # Write all current values from ModelObjects.py to fresh CSVs for
            # floors and rooms. Filename format:
            #       floors_building#.csv
            #       rooms_building#.csv            
            pass
        
        # Update buildings.csv building# entry with new info (costs, etc.)
        
        self.savetime = datetime.now().strftime("%H:%M:%S")
        self.savestatus = 1
        return
                 
if __name__ == "__main__":
    app = Controller()
