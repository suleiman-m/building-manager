from datetime import datetime
import sys
import string

from View import *
from ModelObjects import *

import tkinter as tk
from tkinter.ttk import *
from tkinter import filedialog

'''Creates the model, view, and controller for the application and runs it.

====NOTES====
CCT211 Group Project

ALL DATA FILES are located in one folder. The naming convention accounts for 
each corresponding building number:
    b3_floors.csv
    b3_rooms.csv
ALL REGISTERED BUILDINGS are located in buildings.csv with their IDs.

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
        # Placeholder. Updated in csave_file().
        self.savetime = datetime.now().strftime("%H:%M:%S")
        self.chosen_building=""
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
            
        self.model = Model(self, mode)
        
        # Must change self.chosen_building to avoid attribute error later 
        # for new-file option.
        # Make (Office Space Lease) variable for Site Construction
        self.view.projectInfo.config(text="Building No. ID: " + self.chosen_building \
                                     + "(Office Space Lease)", foreground="black")
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
