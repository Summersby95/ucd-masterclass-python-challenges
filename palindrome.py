import re

s = "race car"

def PalindromeCheck(string):
    string = re.sub(r'[^A-Za-z0-9]+','',string)
    reverse = string[::-1]
    if reverse.lower() == string.lower():
        return True
    else:
        return False

print(PalindromeCheck(s))