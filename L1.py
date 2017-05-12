'''
For http://www.pythonchallenge.com/pc/def/map.html
'''
from string import maketrans

def translate(text):
    input = 'abcdefghijklmnopqrstuvwxyz'
    output = ''
    for char in input:
        output += chr(ord(char) + 2) 
    keyfortranslate = maketrans(input, output)
    print text.translate(keyfortranslate)
text = "map"
translate(text)