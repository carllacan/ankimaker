# -*- coding: utf-8 -*-
"""
Created on Thu Mar 30 16:22:49 2017

@author: carles
"""
import os.path
import sqlite3
import tkinter
from tkinter import ttk
from tkinter import filedialog
from loaders.loader import Loader
from checkbutton import CheckButton

class KindleLoader(Loader):
    
    def __init__(self, parent):
        super().__init__(parent, 'Kindle', 'Load words from a Kindle\'s Vocabulary Builder List')
        
    def init_frame(self):
        self.dbfile = ''
    
        self.file_entry = ttk.Entry(self, width=25)
        self.file_entry.grid(column=0, row=1, columnspan=2, sticky='W')
        
        self.selecdb_button = ttk.Button(self, text='Browse',
                                      command=self.select_file)
        self.selecdb_button.grid(column=2, row=1, sticky='E')
        
        self.usage_check = CheckButton(self)
        self.usage_check.grid(column = 0, row = 2, sticky='E')
        self.usage_label = ttk.Label(self, text='Load also usage sentences')
        self.usage_label.grid(column = 1, row = 2, sticky='W')
        
        self.load_button = ttk.Button(self, text='Load words',
                                      command=self.load_words)
        self.load_button.grid(column = 2, row = 2, sticky='W')
        
    def select_file(self):
        options = {'defaultextension':'db',
                   'parent':self,
                   'initialfile':'vocab.db',
                   'title':'Select your Kindle vocabulary'}
            
        self.dbfile = filedialog.askopenfilename(**options)
        if self.dbfile != '':
            self.file_entry.delete(0, tkinter.END)
            self.file_entry.insert(0, self.dbfile)

    def load_words(self):
        lang = 'en' # TODO: add a language selection list
        if not os.path.isfile(self.dbfile) :
            return None
        vocab = sqlite3.connect(self.dbfile)
        q = '''select WORDS.stem, LOOKUPS.usage, WORDS.timestamp from WORDS
            inner join LOOKUPS on WORDS.id=LOOKUPS.word_key 
            where WORDS.lang=\'{}\''''.format(lang)
        cursor = vocab.execute(q)
        
        info = {} 
        info.keys()
        for w in cursor:
            stem = w[0]
            usage = w[1]
#            timestamp = w[2]
            if stem not in info.keys():
                info[stem] = usage
                
        self.parent.add_words(info.keys()) # add new words
        if self.usage_check:
            self.parent.add_info('Usage', info) # add usage of words
        
        
            
        
            