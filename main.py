from random import randint
import requests

words = []
r = requests.get('https://rentry.co/pythonWordsModule/raw')
words = r.text.split()

def getWords(isJson: bool):
    if isJson:
        word = {"Word": f"{words[randint(0, len(words))]}"}
        return word
    elif not isJson:
        word = f"{words[randint(0, len(words))]}"
        return word
