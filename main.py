import sqlite3
import genanki
import requests
import json

if __name__ == '__main__':

    lang = 'en'#raw_input('What language do you want the words in? (available: en)')
    fname = 'vocab.db' #raw_input...
    
    vocab = sqlite3.connect(fname)
    q = 'select WORDS.stem, LOOKUPS.usage, WORDS.timestamp from WORDS inner join LOOKUPS on WORDS.id=LOOKUPS.word_key where WORDS.lang=\'{}\''.format(lang)
    cursor = vocab.execute(q)

    app_id = '91cff402'
    app_key = 'edde3eeb5d8fe2ab96493642f535f580'
    headers = {'app_id': app_id, 'app_key': app_key}
    url = 'https://od-api.oxforddictionaries.com:443/api/v1/entries/'
    
    deck = genanki.Deck(2059400110, "Kindle Words")
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
    
    added_words = []
    for w in cursor:
        
        # Get OED definition
        
        r = requests.get(url  + lang + '/' + word_id.lower(), headers=headers) 
        entries = r.json()['results'][0]['lexicalEntries'][0]['entries']
        definition = entries[0]['senses'][0]['definitions'][0]
        
        stem = w[0]
        usage = w[1]
        
        if stem not in added_words:
            added_words.append(stem)
            note = genanki.Note(
                model=model,
                fields=[stem, definition, usage]
                )
            deck.add_note(note)

    genanki.Package(deck).write_to_file('english.apkg')
    
    
