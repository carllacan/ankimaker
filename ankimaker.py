import sqlite3
import genanki
import requests
from tkinter import ttk
from tkinter import filedialog
lang_names = {'en': 'English'}

class MainFrame(ttk.Frame):
    def __init__(self, parent, *args, **kwargs):
        ttk.Frame.__init__(self, parent, *args, **kwargs)
        self.root = parent
        self.init_gui()
 
    def init_gui(self):
        """Builds GUI."""
        self.root.title('Kindle to Anki')
     
        self.grid(column=0, row=0, sticky='nsew')
        
        # Load vocabulary file
        
        ttk.Label(self, text='Vocabulary file').grid(column=0, row=0)
        
        self.loaddb_button = ttk.Button(self, text='Load',
                                      command=self.load_from_kindle)
        self.loaddb_button.grid(column=1, row=0)
        
        
        # Load from OED         
        
        ttk.Label(self, text='App id').grid(column=0, row=2)
        self.appid_entry = ttk.Entry(self, width=30)
        self.appid_entry.grid(column=1, row = 2)
        
        ttk.Label(self, text='App key').grid(column=0, row=3)
        self.keyid_entry = ttk.Entry(self, width=30)
        self.keyid_entry.grid(column=1, row = 3)
                
        self.loadOED_button = ttk.Button(self, text='Load definitions from OED',
                                      command=self.load_OED)
        self.loadOED_button.grid(column=2, row=2, columnspan = 2, rowspan = 2)
        self.loadOED_button.state(['disabled'])
        
        # Create vocabulary file
        
        ttk.Label(self, text='Anki deck name:').grid(column=0, row=4)
        
        self.deckname_entry = ttk.Entry(self, width=30)
        self.deckname_entry.grid(column=1, row = 4)
      
        self.create_button = ttk.Button(self, text='Create',
                                      command=self.create_deck)
        self.create_button.grid(column=2, row=4)
        self.create_button.state(['disabled'])

     
        for child in self.winfo_children():
            child.grid_configure(padx=5, pady=5)
    
    def load_from_kindle(self):
#        return filedialog.askopenfilename(defaultextension='.db', 
#                                      filetypes=['db'],
#                                      initialfile='vocab.db',
#                                      mustexist=True, 
#                                      parent=self, 
#                                      )
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
            
    
    def load_OED(self):
        lang = 'en'
        app_id = self.appid_entry.get()
        app_key = self.keyid_entry.get()
        load_ODE(self.words, lang, app_id, app_key)

    def create_deck(self):
        lang = 'en'
        deckname = self.deckname_entry.get()
        options = {'defaultextension':'apkg',
                   'parent':self,
                   'title':'Select the Anki deck location'}
        deckfile = filedialog.asksaveasfilename(**options)
        create_deck(self.words, lang, deckname, deckfile)
    
    
def load_words(dbfile, lang):
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
    
def load_ODE(words, lang, app_id, app_key):
    headers = {'app_id': app_id, 'app_key': app_key}
    url = 'https://od-api.oxforddictionaries.com:443/api/v1/entries/'
    for w in words:            
        stem = w.lower()
        r = requests.get(url  + lang + '/' + stem, headers=headers) 
        entries = r.json()['results'][0]['lexicalEntries'][0]['entries']
        words[w]['definition'] = entries[0]['senses'][0]['definitions'][0]
    return words
 
def create_deck(words, lang, deckname, deckfile):
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
