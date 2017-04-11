import requests
from tkinter import ttk
from loaders.loader import Loader

class OEDLoader(Loader):
    
    def __init__(self, parent):
        super().__init__(parent, 'OED', 'Load definitions from the OED')
        
    def init_frame(self):
        ttk.Label(self, text='App id').grid(column=0, row=0)
        self.appid_entry = ttk.Entry(self, width=30)
        self.appid_entry.grid(column=1, row = 0)
        
        ttk.Label(self, text='App key').grid(column=0, row=1)
        self.keyid_entry = ttk.Entry(self, width=30)
        self.keyid_entry.grid(column=1, row = 1)
                
        self.load_button = ttk.Button(self, text='Load definitions from OED',
                                      command=self.load_info)
        self.load_button.grid(column=0, row=2, columnspan = 2, rowspan = 2)
#        self.load_button.state(['disabled'])

        try: # for lazines I store my OED credentials in a file
            secrets = open('secrets')
            self.appid_entry.insert(0, secrets.readline()[:-1])
            self.keyid_entry.insert(0, secrets.readline()[:-1])
            secrets.close()
        except:
            pass
            
    def load_info(self):
        lang = 'en'
        app_id = self.appid_entry.get()
        app_key = self.keyid_entry.get()
        headers = {'app_id': app_id, 'app_key': app_key}
        url = 'https://od-api.oxforddictionaries.com:443/api/v1/entries/'
        words = self.parent.get_words()
        info = {}
        for w in words:            
            stem = w.lower()
            r = requests.get(url  + lang + '/' + stem, headers=headers) 
            entries = r.json()['results'][0]['lexicalEntries'][0]['entries']
            info[w] = entries[0]['senses'][0]['definitions'][0]
        self.parent.add_info('Answer', info)
 