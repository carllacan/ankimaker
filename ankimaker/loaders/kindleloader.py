# -*- coding: utf-8 -*-
"""
Created on Thu Mar 30 16:22:49 2017

@author: carles
"""
import tkinter
from tkinter import ttk
from tkinter import filedialog
from loaders.loader import Loader

class KindleLoader(Loader):
    
    def __init__(self, parent):
        super().__init__(parent, 'Kindle')
        self.root = parent
        
    def init_frame(self):
    
        ttk.Label(self, text='Vocabulary file').grid(column=2, row=0, sticky='W')
        
        self.loaddb_button = ttk.Button(self, text='Load',
                                      command=self.load_from_kindle)
        self.loaddb_button.grid(column=1, row=0, sticky='E')
        
    def load_from_kindle(self):

        options = {'defaultextension':'db',
                   'parent':self,
                   'initialfile':'vocab.db',
                   'title':'Select your Kindle vocabulary'}
            
        dbfile = filedialog.askopenfilename(**options)

        lang = 'en'
        self.words = load_words(dbfile, lang)
        if self.words.keys():
            self.loadOED_button.state(['!disabled'])
            self.create_button.state(['!disabled'])
            