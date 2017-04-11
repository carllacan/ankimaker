import requests
import tkinter
from tkinter import ttk
from loaders.loader import Loader

class WikLoader(Loader):
    
    def __init__(self, parent):
        super().__init__(parent, 'Wiktionary')
        self.root = parent
        
    def init_frame(self):

                
        self.loadOED_button = ttk.Button(self, text='Load',
                                      command=self.load_OED)
        self.loadOED_button.grid(column=0, row=2, columnspan = 2, rowspan = 2)
        self.loadOED_button.state(['disabled'])

            
    def load_OED(self):
        pass