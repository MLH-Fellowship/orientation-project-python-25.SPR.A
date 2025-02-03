from autocorrect import Speller

spell = Speller(lang='en')

def spell_check(text):
    '''
    Spell checks the text
    '''
    return spell(text)

