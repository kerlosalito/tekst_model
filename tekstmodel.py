#
# textmodel.py
#
# Opdracht: Tekstidentificatie
#
# Naam:
#

import string


class TextModel:
    """A class supporting complex models of text."""

    def __init__(self):
        """Create an empty TextModel."""
        #
        # Maak dictionary's voor elke eigenschap
        #
        self.words = {}             # Om woorden te tellen
        self.word_lengths = {}      # Om woordlengtes te tellen
        self.stems = {}             # Om stammen te tellen
        self.sentence_lengths = {}  # Om zinslengtes te tellen
        #
        # Maak een eigen dictionary
        #
        self.my_feature = {}        # Om ... te tellen

    def __repr__(self):
        """Display the contents of a TextModel."""
        s = 'Woorden:\n' + str(self.words) + '\n\n'
        s += 'Woordlengtes:\n' + str(self.word_lengths) + '\n\n'
        s += 'Stammen:\n' + str(self.stems) + '\n\n'
        s += 'Zinslengtes:\n' + str(self.sentence_lengths) + '\n\n'
        s += 'MIJN EIGENSCHAP:\n' + str(self.my_feature)
        return s

    # Voeg hier andere methodes toe.
    # Je hebt in het bijzonder methodes nodig die het model vullen.
    def read_text_from_file(self, filename):
        """Open the given file from parameter filename, read the file and add the content of the file to self.text"""
        with open(filename) as data:
            self.text = data.read()

    def clean_string(self, s):
        s = s.lower()

        for p in string.punctuation:
            s = s.replace(p, '')
        
        return s



# Hier kan je dingen testen...
tm = TextModel()
# Zet hier aanroepen neer die het model vullen met informatie
print('TextModel:', tm)

test_text = """Dit is een korte zin. Dit is geen korte zin, omdat
deze zin meer dan 10 woorden en een getal bevat! Dit is
geen vraag, of wel?"""

tm.read_text_from_file('test.txt')
assert tm.text == test_text 

clean_text = """dit is een korte zin dit is geen korte zin omdat
deze zin meer dan 10 woorden en een getal bevat dit is
geen vraag of wel"""
clean_s = tm.clean_string(tm.text)
assert clean_s == clean_text