# AnkiMaker
AnkiMaker lets you automatically create Anki Decks out of your Kindle vocabulary lists and the OED.

# How to use it

* The Vocabulary Builder's list of your Kindle is under [Your Kindle filesystem]/system/vocabulary/vocab.db. 
* Get credentials for the OED's API. Go [here](https://developer.oxforddictionaries.com) and create a *Free* account. This will grant you 3000 word lookups a month, which is probably enough (and if it isn't you can just make another account). Then click on *Credentials* and open *None*'s app. This will show you your Application ID and your Application Keys

# Install

## Linux 

Linux users can download the Python file. To execute it you'll need to have genanki and requests installed. You can do:

    pip install genanki
    pip install requests
    mkdir ankimaker && cd ankimaker
    wget https://raw.githubusercontent.com/carllacan/ankimaker/master/ankimaker.py
    python ankimaker

A packaged version is not available yet.

## Windows

No installation required. Just download [the Windows executable](https://github.com/carllacan/ankimaker/raw/master/ankimaker.exe) and open it.

## Thanks to

* The creator of [Genanki](https://github.com/kerrickstaley/genanki)
* The creator of Anki
