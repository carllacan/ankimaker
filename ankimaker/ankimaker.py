import genanki
import tkinter
from tkinter import ttk
from tkinter import filedialog
import loaders  

class MainFrame(ttk.Frame):
    def __init__(self, parent, *args, **kwargs):
        ttk.Frame.__init__(self, parent, *args, **kwargs)
        self.root = parent
        self.init_gui()
        self.words = {}
 
    def init_gui(self):
        """Builds GUI."""
        self.root.title('AnkiMaker')     
        self.grid(column=0, row=0, sticky='nsew')
        
        lists_width = 10
        
        
        # Questions loading frame              
              
        loader_list = [loaders.KindleLoader,
                       loaders.FileLoader,
                       loaders.OEDLoader,
                       loaders.WikLoader]
        
        self.loaders = []
        for l in loader_list:
            # initialize every loader's frame with the mainframe as parent
            self.loaders.append(l(self))
        
        # Question loading option list
        
        self.list = tkinter.Listbox(self, width = lists_width, 
                                    height = 8,
                                    selectmode = tkinter.SINGLE)
        self.list.grid(column=0, row=0, sticky = 'N')
        for op in self.loaders:
            self.list.insert(tkinter.END, op.name)   
        self.list.bind('<<ListboxSelect>>', self.select)
        

        self.list.selection_set(0)      

        # Deck creation frame
        
        self.dframe = DeckFrame(self)
        self.dframe.grid(column=0, row=1, columnspan = 4)
        self.dframe.disable()
        
        # Add padding to everything
        for child in self.winfo_children():
            child.grid_configure(padx=5, pady=5)
                                            
        self.select()
            
            
            
    def add_words(self, words):
        # Adds entries to the table if they are not there already
        self.dframe.add_words(words)    
        for w in words:
            if not w in self.words:
                self.words[w] = {}
                
#        self.activate_infoloaders()
        self.dframe.activate()
        
    def get_words(self):
        return self.words.keys()
        
    def add_info(self, col_name, words):
        # Adds entries to the table if they are not there already
        self.dframe.add_info(col_name, words)
        for w in words:
            if w in self.words:
                self.words[w][col_name] = words[w]
        
#    def activate_infoloaders(self):
#        for l in self.infoloaders:
#            l.activate()    
#            
#    def disable_infoloaders(self):
#        for l in self.infoloaders:
#            l.disable()
            
    def select(self, event = None):
        current_selection = self.list.curselection() # a tuple of selected
        if len(current_selection): # if there is a selected one
            index = current_selection[0]
            for l in self.loaders:
                l.grid_forget()
            self.loaders[index].grid(column=1, row=0, sticky = 'N')
            self.loaders[index].grid_configure(padx=5, pady=5)    


    
        
class DeckFrame(ttk.Frame):
        
    def __init__(self, parent, *args, **kwargs):
        ttk.Frame.__init__(self, parent, *args, **kwargs)
        self.parent = parent
        # this dictionary will store the index of every field
#        self.columns = {}
        self.columns = {'Question':'#0', 'Answer':'#1'}
        self.init_frame()
  
        
    def init_frame(self):
        columns = ['#' + str(c) for c in range(1, 10)]
        self.words_table = ttk.Treeview(self, columns = columns, 
                                        displaycolumns = ['#1'])
        self.words_table.grid(column= 0, row= 0, columnspan= 5)
        
        # this dictionary will store the index of every field
        
        self.words_table.heading('#0', text = 'Question',
                                 command = lambda: self.sort_table_by('#0'))
        self.words_table.heading('#1', text = 'Answer',
                                 command = lambda: self.sort_table_by('#1'))
        
        ttk.Label(self, text='Anki deck name:').grid(column=0, row=1)
        self.name_entry = ttk.Entry(self, width=20)
        self.name_entry.grid(column=1, row=1, columnspan = 1)
        
        ttk.Label(self, text='File').grid(column=2, row=1)
        self.file_entry = ttk.Entry(self, width=25)
        self.file_entry.grid(column=3, row=1, columnspan = 1)
      
        self.browse_button = ttk.Button(self, text='Browse',
                                      command=self.select_file)
        self.browse_button.grid(column=4, row=1, columnspan = 1)
        
      
        self.create_button = ttk.Button(self, text='Create',
                                      command=self.create_deck)
        self.create_button.grid(column=5, row=1, columnspan = 1)
        

     
        # Add padding to everything
        for child in self.winfo_children():
            child.grid_configure(padx=5, pady=5)
            
    def activate(self):
        self.browse_button.state(['!disabled'])
        self.create_button.state(['!disabled'])
            
    def disable(self):
        self.browse_button.state(['disabled'])
        self.create_button.state(['disabled'])
            
    def add_column(self, name):
        if not name in self.columns:
            cid = '#' + str(len(self.columns))
            self.columns[name] = cid
            new_columns = self.words_table.cget('displaycolumns') + (cid,)
            self.words_table.configure(displaycolumns = new_columns)
            
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
                self.words_table.set(w, self.columns[col_name], info[w])
    
    def select_file(self):
        options = {'defaultextension':'apkg',
                   'parent':self,
                   'title':'Select the Anki deck location'}
        self.filename = filedialog.asksaveasfilename(**options)
        if self.filename != '': 
            self.file_entry.delete(0, tkinter.END)
            self.file_entry.insert(0, self.filename)
            

        
    def create_deck(self):

        deck = genanki.Deck(2059400110, self.name_entry.get())
        
        fields = []
        for f in self.columns.keys(): # for each field
            fields.append({'name':f})
        model = genanki.Model(
            1607392319,
            'Word',
            fields=fields,
            templates=[
                {
                    'name': 'Card 1',
                    'qfmt': '{{Question}}',
                    'afmt': '<b>{{FrontSide}}</b>: {{Answer}}<hr id="usage">{{Usage}}'
                }]
        )
        
        for w in self.parent.words:
            fields = []
            for f in self.columns.keys(): # for each field
                if f == 'Question':
                    fields.append(w)
                else:
                    fields.append(self.parent.words[w][f])
            note = genanki.Note(
                model=model,
                fields=fields
                )
            deck.add_note(note)
    
        genanki.Package(deck).write_to_file(self.file_entry.get())
        

        
    def sort_table_by(self, column):
        print('Sorting by' + column)
    
    
if __name__ == '__main__':
    root = tkinter.Tk()
    MainFrame(root)
    root.mainloop()
