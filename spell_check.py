from autocorrect import Speller

spell = Speller(lang='en')

def spell_check(text):
    '''
    Spell checks the text
    '''
    return spell(text)

def spell_check_json(json_data: dict):
    '''
    Spell checks the JSON data
    '''
    for key, value in json_data.items():
        json_data[key] = spell_check(value)

    return json_data

