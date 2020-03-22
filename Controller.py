
from View import *
import tkinter as tk
from tkinter.ttk import *

from tkinter import filedialog


'''Creates the model, view, and controller for the application and runs it.
'''
class Controller:
    
    def __init__(self):

        self.root = tk.Tk()
        self.view = View(self.root, self)
  
        self.root.mainloop()


    

                 
if __name__ == "__main__":
    app = Controller()
