import json

from difflib import get_close_matches
data=json.load(open('data.json'))

def translate(word):
    word=word.lower()
    if word in data:
        return data[word]
    elif word.title() in data:
        return data[word.title()]
    elif word.upper() in data:
        return data[word.upper()]
    elif len(get_close_matches(word, data.keys())) > 0:
        yeah=input("Please you mean %s instead? Please enter Y if yes, or N if no: " % get_close_matches(word, data.keys()[0]))
        if yeah == "Y":
            return data[get_close_matches(word, data.keys())[0]]
        elif yeah == "N":
            return "Please word does't exit. Please double check it"
        else:
            return "We did't understand your entry."
        
    else:
        return "The word doe't exit. Please double check it"
    
    
word=input("Please a word:")
outpput=translate(word)

if type(output) == list:
    for item in output:
        print(item)
        
else:
    print(output)
    