# -*- coding: utf-8 -*-
"""
Created on Tue Apr 11 16:14:15 2017

@author: carles

A wrapper for tkinter's CheckButton widget that adds a getter for the
button's value.
"""

from tkinter import IntVar
from tkinter.ttk import Checkbutton

class CheckButton(Checkbutton):
    
    def __init__(self, parent, **params):
        self.value = IntVar()
        # if for some reason the button is created with a different onvalue
        if 'onvalue' in params: 
            # take note of it
            self.onvalue = params['onvalue']
        else:
            # otherwise onvalue is just 1
            self.onvalue = 1
        super().__init__(parent, variable = self.value, **params)
        
    def __bool__(self):
        return self.value == self.onvalue