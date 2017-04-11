import tkinter
from tkinter import ttk
from loaders.loader import Loader

class FileLoader(Loader):
    
    def __init__(self, parent):
        super().__init__(parent, 'Load from a file')
        self.root = parent
        
    def init_frame(self):
        pass