import os.path
import tkinter
from tkinter import ttk
from tkinter import filedialog
from loaders.loader import Loader
from checkbutton import CheckButton

class FileLoader(Loader):
    
    def __init__(self, parent):
        super().__init__(parent, 'File', 'Load words from any kind of textfile')
        
    def init_frame(self):
        self.textfile = ''
    
        self.file_entry = ttk.Entry(self, width=25)
        self.file_entry.grid(column=0, row=1, columnspan=2, sticky='W')
        
        self.selecdb_button = ttk.Button(self, text='Browse',
                                      command=self.select_file)
        self.selecdb_button.grid(column=2, row=1, sticky='E')
        
        self.load_button = ttk.Button(self, text='Load words',
                                      command=self.load_words)
        self.load_button.grid(column = 2, row = 2, sticky='W')    
    
    def select_file(self):
        options = {'defaultextension':'txt',
                   'parent':self,
                   'title':'Select your text file'}
            
        self.textfile = filedialog.askopenfilename(**options)
        if self.textfile != '':
            self.file_entry.delete(0, tkinter.END)
            self.file_entry.insert(0, self.textfile)

    def load_words(self):
        if not os.path.isfile(self.textfile) :
            return None
        file = open(self.textfile, "r")
        lines = file.readlines()

        words = {}
        
        for line in lines:
        	words[line] = ''

        self.parent.add_words(words)
 