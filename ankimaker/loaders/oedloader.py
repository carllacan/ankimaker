# -*- coding: utf-8 -*-
"""
Created on Thu Mar 30 16:35:02 2017

@author: carles
"""

import tkinter
from tkinter import ttk
from tkinter import filedialog
from loaders.loader import Loader

class OEDLoader(Loader):
    
        
    def init_frame(self):
        ttk.Label(self, text='App id').grid(column=0, row=0)
        self.appid_entry = ttk.Entry(self, width=30)
        self.appid_entry.grid(column=1, row = 0)
        
        ttk.Label(self, text='App key').grid(column=0, row=1)
        self.keyid_entry = ttk.Entry(self, width=30)
        self.keyid_entry.grid(column=1, row = 1)
                
        self.loadOED_button = ttk.Button(self, text='Load definitions from OED',
                                      command=self.load_OED)
        self.loadOED_button.grid(column=0, row=2, columnspan = 2, rowspan = 2)
        self.loadOED_button.state(['disabled'])