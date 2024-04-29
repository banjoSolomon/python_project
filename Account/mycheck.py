import re

try:
    with open('example.txt', 'w') as example:
        example.write("01 solomon 500\n")
        example.write("02 sam 500\n")
        example.write("03 timi 500\n")
        example.write("04 john 500\n")
except FileNotFoundError:
    print('File not found')


def match_latters(word):
    if re.fullmatch(r'\d+ [A-Z][a-z]* [A-Z][a-z]*', word):
        return True
    else:
        return False
