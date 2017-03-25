import sqlite3
import genanki
import wx


if __name__ == '__main__':

    lang = 'en'#raw_input('What language do you want the words in? (available: en)')
    fname = 'vocab.db' #raw_input...
    vocab = sqlite3.connect(fname)
    q = 'select WORDS.stem, LOOKUPS.usage, WORDS.timestamp from WORDS inner join LOOKUPS on WORDS.id=LOOKUPS.word_key where WORDS.lang=\'{}\''.format(lang)
    cursor = vocab.execute(q)

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
                'afmt': '{{FrontSide}}<hr id="answer">{{Answer}}<hr id="usage"{{Usage}}>'
            }]
    )
    
    for w in cursor:
        note = genanki.Note(
            model=model,
            fields=[w[0], 'descrp', w[1]]
            )
        deck.add_note(note)

    genanki.Package(deck).write_to_file('english.apkg')
    
    
