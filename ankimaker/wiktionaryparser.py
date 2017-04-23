from html.parser import HTMLParser

parts_of_speech = ("Noun",
                   "Verb",
                   "Pronoun",
                   "Adjective",
                   "Adverb")

class WiktionaryParser(HTMLParser):
    
    def __init__(self, lang):
        self.lang = lang # lang of the word we are looking up
        self.in_lang = False # flag: are we in the appropriate language?
        self.getting_defs = False # flag: are we collecting definitions?
        self.pos = "" # part of speech we are in
        self.trans = {} # each key is the pos, each entry the translations
        HTMLParser.__init__(self)
    
    def handle_starttag(self, tag, attrs):
        if tag == "span" and ("id", self.lang) in attrs:
            self.in_lang = True
        if tag == "ol" and self.in_lang:
            self.getting_defs = True        
        if tag == "h2" and self.in_lang:
            self.in_lang = False
            
    def handle_endtag(self, tag):
        if tag == "ol" and self.getting_defs:
            self.getting_defs = False

    def handle_data(self, data):
        if not self.getting_defs and data in parts_of_speech:
            self.pos = data
        if self.getting_defs and data != "\n" and len(data) < 20:
            self.trans[self.pos] = data
            print ("koierleiñeñirbñeirñeorngeñorgneñorgneñorjgneorgneorijngeorigjeorgijerogij")
            print(data)
            
#url = 'https://en.wiktionary.org/w/index.php?title=cosa&printable=yes'
#r = requests.get(url, headers={})
#p = WiktionaryParser("Catalan")
#p.feed(r.text)
