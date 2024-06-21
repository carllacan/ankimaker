# ATTENTION

Oxford API has changed their API and this program no longer works. You are welcome to make a fork of it and adapt it, but I believe the Terms and Conditions changed as well and it might not be possible/legal to make something like AnkiMaker any more (or at least not using Oxford API). I did some work on including a Wiktionary parser 7 years ago, but I didn't get very far. However Wiktionary does have an API that I seem to have missed when I started making that parser, and which could probably be used in place of the Oxford API. Better yet, it could be used for languages other than English.

In any case I have found that makin my Anki cards by hand results in better retention, so you might be better served by not using any automation tools for this.

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
