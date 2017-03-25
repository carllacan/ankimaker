# kindletoanki
Short script that creates and Anki deck from a Kindle's Vocabulary list, taking the definitions from the Oxford English Dictionary.

# How to use it

You need to get credentials for the OED's API. Create an account at https://developer.oxforddictionaries.com/.
The Vocabulary Builder's list of your Kindle is under [Your Kindle filesystem]/system/vocabulary/vocab.db. You only get to make 3000 queries per month, but it should be enough.

# Dependencies

The genanki, ktinker and request Python libraries are needed.