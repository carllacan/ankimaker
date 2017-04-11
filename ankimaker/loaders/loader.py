
from tkinter import ttk

class Loader(ttk.LabelFrame):
    
    def __init__(self, parent, name, text):
        super().__init__(parent, text = text, height = 125, width = 500)
        self.name = name
        self.parent = parent
        self.init_frame()
        self.height = 200
        self.height = 500
        self.grid_propagate(0)
        for child in self.winfo_children():
            child.grid_configure(padx=5, pady=5)
        
    def init_frame(self):
        pass
        
    
    def activate(self):
        for child in self.winfo_children():
            child.state(['!disabled'])
            
    def disable(self):
        for child in self.winfo_children():
            child.state(['disabled'])