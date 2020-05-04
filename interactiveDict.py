#Interactive English Dictionary
import json
import difflib
from difflib import get_close_matches
#read from json file
data = json.load(open('data.json'))

def translate(word):
    word = word.lower()
    if word in data:
        return data[word]

    #for word that starts with capital letter
    elif word.title() in data:
        return data[word.title()]

    #for acronyms
    elif word.upper() in data:
        return data[word.upper()]

    #if similar word
    elif len(get_close_matches(word, data.keys())) > 0:
        yn = input('Did you mean %s instead? Enter Y if yes or N if no.' %get_close_matches(word, data.keys())[0])
        if yn == 'Y':
            return data[get_close_matches(word, data.keys())[0]]
        elif yn == 'N':
            return 'The word does not exist. Please double check it.'
        else:
            return 'We did not understand your entry.'

    #if bad word
    else:
        return ('The word does not exist. Please double check it.')

word = input('Enter word: ')

out = translate(word)
if type(out) == list:
    for item in out:
        print(item)
else:
    print(out)
