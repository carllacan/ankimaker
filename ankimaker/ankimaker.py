import genanki
import requests
import tkinter
from tkinter import ttk
from tkinter import filedialog
import loaders  
import tktable

class MainFrame(ttk.Frame):
    def __init__(self, parent, *args, **kwargs):
        ttk.Frame.__init__(self, parent, *args, **kwargs)
        self.root = parent
        self.init_gui()
        # Add padding to everything
        for child in self.winfo_children():
            child.grid_configure(padx=5, pady=5)
 
    def init_gui(self):
        """Builds GUI."""
        self.root.title('Kindle to Anki')     
        self.grid(column=0, row=0, sticky='nsew')
        
        lists_width = 10
        
        # Question loading option list
        question_load_ops = ['A Kindle', 'A list', 'A subtitle']

        
        self.questionload_list = tkinter.Listbox(self, width = lists_width, 
                                                 height = 8)
        self.questionload_list.grid(column=0, row=0, sticky = 'N')
        for o in question_load_ops:
            self.questionload_list.insert(tkinter.END, o)
              
        # Questions loading frame
        
        self.qload = loaders.KindleLoader(self)
        self.qload.grid(column=1, row=0, sticky = 'N')

        
        # Answers loading option list
        answers_load_ops = ['The OED', 'Wiktionary']
        
        self.answersload_list = tkinter.Listbox(self, width = lists_width, 
                                                 height = 8)
        self.answersload_list.grid(column=2, row=0, sticky = 'N')
        for o in answers_load_ops:
            self.answersload_list.insert(tkinter.END, o)
            
        # Answers loading frame

        self.aload = loaders.OEDLoader(self)
        self.aload.grid(column=3, row=0, sticky = 'N')
        
        self.dframe = DeckFrame(self)
        self.dframe.grid(column=0, row=1, columnspan = 4)
        
    def add_words(self, words):
        # Adds entries to the table if they are not there already
        self.dframe.add_words(words)    
        
    def add_info(self, info, words):
        # Adds entries to the table if they are not there already
        self.dframe.add_info(info, words)
     
        
class DeckFrame(ttk.Frame):
        
    def __init__(self, parent, *args, **kwargs):
        ttk.Frame.__init__(self, parent, *args, **kwargs)
        self.root = parent
        # this dictionary will store the index of every field
#        self.columns = {}
        self.columns = {'Questions':'#0', 'Answers':'#1'}
        self.init_frame()
  
        
    def init_frame(self):
        
        self.words_table = ttk.Treeview(self, columns = ['#1'])
        self.words_table.grid(column= 0, row= 0, columnspan= 3)
        
        # this dictionary will store the index of every field
        
        self.words_table.heading('#0', text = 'Questions',
                                 command = lambda: self.sort_table_by('#0'))
        self.words_table.heading('#1', text = 'Answers',
                                 command = lambda: self.sort_table_by('#1'))
        ttk.Label(self, text='Anki deck name:').grid(column=0, row=1)
        
        
#        ysb = ttk.Scrollbar(orient=tkinter.VERTICALs
        
        self.deckname_entry = ttk.Entry(self, width=30)
        self.deckname_entry.grid(column=1, row=1, columnspan = 1)
      
        self.create_button = ttk.Button(self, text='Create',
                                      command=self.create_deck)
        self.create_button.grid(column=2, row=1, columnspan = 1)
        self.create_button.state(['disabled'])
        

     
        # Add padding to everything
        for child in self.winfo_children():
            child.grid_configure(padx=5, pady=5)
            
    def add_column(self, name):
        if not name in self.columns:
            cid = '#' + str(len(self.columns))
            self.columns[name] = cid
            new_columns = self.words_table.cget('columns') + (cid,)
            print(self.words_table.cget('columns'))
            print(new_columns)
            self.words_table.configure(columns = new_columns)
            
            sort_command = lambda: self.sort_table_by(cid)
            self.words_table.heading(cid, text = name,
                                     command = sort_command)

    def add_words(self, words):
        # Adds entries to the table if they are not there already
        # words: a list of words to be added
        for w in words:
            if not self.words_table.exists(w):
                self.words_table.insert('', 'end', w, text=w)
    
    def add_info(self, col_name, info):
        # Adds entries to the table if they are not there already.
        # Columns will be created if they don't exist yet
        # col_name: a string with the name of the relevant field
        # words_info: a dictionary of dictionaries with the words
        # as keys and the information as values
    
        # Maybe join this methoed with add_words, so that if the
        # words passed to this one don't exists new entries are added
        self.add_column(col_name)
        for w in info:
            if self.words_table.exists(w):
#                values = self.words_table.item(w)
##                values[col_name] = info[w]
#                print(values['values']['values'])
#                self.words_table.item(w, values = values)
                self.words_table.set(w, col_name, info[w])
    

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
        

        
    def sort_table_by(self, column):
        print('Sorting by' + column)
    
    
if __name__ == '__main__':
    root = tkinter.Tk()
    MainFrame(root)
    root.mainloop()
