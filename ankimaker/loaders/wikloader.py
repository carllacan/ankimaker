import requests
import tkinter
from tkinter import ttk
from loaders.loader import Loader
from wiktionaryparser import WiktionaryParser

class WikLoader(Loader):
    
    def __init__(self, parent):
        super().__init__(parent, 'Wiktionary', 'Load info from Wiktionary')
        
    def init_frame(self):

        # TODO: add the language selector
        self.load_button = ttk.Button(self, text='Load',
                                      command=self.load)
        self.load_button.grid(column=0, row=2, columnspan = 2, rowspan = 2)
#        self.load_button.state(['disabled'])
        

            
    def load(self):
        words = self.parent.get_words()
        info = {}
        url = "https://en.wiktionary.org/w/index.php?title={}&printable=yes"
        lang = "English" # get from the selector in the future
        parser = WiktionaryParser(lang)
        for w in words:
            r = requests.get(url.format(w), headers={}) 
            parser.feed(r.text)
            info[w] = str(parser.trans)
            parser.reset()
        self.parent.add_info('Answer', info)