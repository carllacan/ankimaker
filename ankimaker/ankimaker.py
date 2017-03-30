import sqlite3
import genanki
import requests
import tkinter
from tkinter import ttk
from tkinter import filedialog
import loaders  

class MainFrame(ttk.Frame):
    def __init__(self, parent, *args, **kwargs):
        ttk.Frame.__init__(self, parent, *args, **kwargs)
        self.root = parent
        self.init_gui()
 
    def init_gui(self):
        """Builds GUI."""
        self.root.title('Kindle to Anki')
     
        self.grid(column=0, row=0, sticky='nsew')
        
        # Question loading option list
        question_load_ops = ['A Kindle', 'A list', 'A subtitle']

        
        self.questionload_list = tkinter.Listbox(self, width = 15, 
                                                 height = 8)
        self.questionload_list.grid(column=0, row=0, sticky = 'N')
        for o in question_load_ops:
            self.questionload_list.insert(tkinter.END, o)
              
        # Questions loading frame
        
        self.qload = loaders.KindleLoader(self)
        self.qload.grid(column=1, row=0, sticky = 'N')

        
        # Answers loading option list
        answers_load_ops = ['The OED', 'Wiktionary']
        
        self.answersload_list = tkinter.Listbox(self, width = 15, 
                                                 height = 8)
        self.answersload_list.grid(column=2, row=0, sticky = 'N')
        for o in answers_load_ops:
            self.answersload_list.insert(tkinter.END, o)
            
        # Answers loading frame

        self.aload = loaders.OEDLoader(self)
        self.aload.grid(column=3, row=0, sticky = 'N')
        
        self.dframe = DeckFrame(self)
        self.dframe.grid(column=0, row=1, columnspan = 4)
     
        # Add padding to everything
        for child in self.winfo_children():
            child.grid_configure(padx=5, pady=5)
        
class DeckFrame(ttk.Frame):
        
    def __init__(self, parent, *args, **kwargs):
        ttk.Frame.__init__(self, parent, *args, **kwargs)
        self.root = parent
        self.init_frame()
        for child in self.winfo_children():
            child.grid_configure(padx=5, pady=5)
  
        
    def init_frame(self):
        
        ttk.Label(self, text='Anki deck name:').grid(column=0, row=0)
        
        self.deckname_entry = ttk.Entry(self, width=30)
        self.deckname_entry.grid(column=1, row=0, columnspan = 1)
      
        self.create_button = ttk.Button(self, text='Create',
                                      command=self.create_deck)
        self.create_button.grid(column=2, row=0, columnspan = 1)
        self.create_button.state(['disabled'])

     
        # Add padding to everything
        for child in self.winfo_children():
            child.grid_configure(padx=5, pady=5)
    

    def create_deck(self):
        lang = 'en'
        deckname = self.deckname_entry.get()
        options = {'defaultextension':'apkg',
                   'parent':self,
                   'title':'Select the Anki deck location'}
        deckfile = filedialog.asksaveasfilename(**options)
        deck = genanki.Deck(2059400110, deckname)
        model = genanki.Model(
            1607392319,
            'Word',
            fields=[
                {'name': 'Question'},
                {'name': 'Answer'},
                {'name': 'Usage'}
                ],
            templates=[
                {
                    'name': 'Card 1',
                    'qfmt': '{{Question}}',
                    'afmt': '<b>{{FrontSide}}</b>: {{Answer}}<hr id="usage">{{Usage}}'
                }]
        )
        
        for w in words:
                note = genanki.Note(
                    model=model,
                    fields=[w, words[w]['definition'], words[w]['usage']]
                    )
                deck.add_note(note)
    
        genanki.Package(deck).write_to_file(deckfile)
    
    
if __name__ == '__main__':
    root = tkinter.Tk()
    MainFrame(root)
    root.mainloop()
