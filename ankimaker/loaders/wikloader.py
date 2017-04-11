import requests
import tkinter
from tkinter import ttk
from loaders.loader import Loader

class WikLoader(Loader):
    
    def __init__(self, parent):
        super().__init__(parent, 'Wiktionary', 'Load info from Wiktionary')
        
    def init_frame(self):

                
        self.load_button = ttk.Button(self, text='Load',
                                      command=self.load)
        self.load_button.grid(column=0, row=2, columnspan = 2, rowspan = 2)
        self.load_button.state(['disabled'])
        

            
    def load(self):
        pass