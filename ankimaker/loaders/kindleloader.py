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
    
        self.label = ttk.Label(self, text='Select your Kindle vocabulary file:')
        self.label.grid(column=0, row=0, columnspan=2)
        self.fileentry = ttk.Entry(self, width=25)
        self.fileentry.grid(column=0, row=1, columnspan=2, sticky='W')
        
        self.loaddb_button = ttk.Button(self, text='Load',
                                      command=self.load_from_kindle)
        self.loaddb_button.grid(column=2, row=1, sticky='E')
        
        self.usage_check = ttk.Checkbutton(self)
        self.usage_check.grid(column = 0, row = 2, sticky='E')
        self.usage_label = ttk.Label(self, text='Load also usage sentences')
        self.usage_label.grid(column = 1, row = 2, sticky='W')
        
    def load_from_kindle(self):

        options = {'defaultextension':'db',
                   'parent':self,
                   'initialfile':'vocab.db',
                   'title':'Select your Kindle vocabulary'}
            
        dbfile = filedialog.askopenfilename(**options)

        lang = 'en'
        self.words = self.load_words(dbfile, lang)
        if self.words.keys():
            self.loadOED_button.state(['!disabled'])
            self.create_button.state(['!disabled'])
            
    def load_words(self, dbfile, lang):
        vocab = sqlite3.connect(dbfile)
        q = '''select WORDS.stem, LOOKUPS.usage, WORDS.timestamp from WORDS
            inner join LOOKUPS on WORDS.id=LOOKUPS.word_key 
            where WORDS.lang=\'{}\''''.format(lang)
        cursor = vocab.execute(q)
        
        words = {}    
        for w in cursor:
            stem = w[0]
            usage = w[1]
            timestamp = w[2]
            if stem not in words.keys():
                words[stem] = {'usage':usage}
        return words
            