# -*- coding: utf-8 -*-
"""
Created on Thu Mar 30 15:14:08 2017

@author: carles
"""
import tkinter
from tkinter import ttk
from tkinter import filedialog

class Loader(ttk.LabelFrame):
    
    def __init__(self, parent, text):
        super().__init__(text = text)
        self.root = parent
        self.init_frame()
        
    def init_frame(self):
        pass
        
    def hide(self):
        pass