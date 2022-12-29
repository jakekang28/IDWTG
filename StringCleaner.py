# StringCleaner.py
from copy import copy

def StringReplacer(targstr):
    
    targstr = targstr.replace("|<", "k")
    targstr = targstr.replace("|>", "p")
    targstr = targstr.replace("()", "o")
    targstr = targstr.replace("[]", "o")
    targstr = targstr.replace("{}", "o")
    
    n = len(targstr)
    newstring = list(targstr)
    
    for i in range(n):
        if newstring[i] == '@':
            newstring[i] = 'a'
        elif newstring[i] == '$':
            newstring[i] = 's'
        elif newstring[i] == '0':
            newstring[i] = 'o'
        elif newstring[i] == '7':
            newstring[i] = 't'
        elif newstring[i] == '3':
            newstring[i] = 'e'
        elif newstring[i] == '5':
            newstring[i] = 's'
        elif newstring[i] == '<':
            newstring[i] = 'c'
    
    targstr = "".join(newstring)
    return targstr

trickslist = ['1','2','3','4','5','6','7','8','9','.',',']

def trickCheck(targstr):
    n = len(targstr)
    newstring = list(targstr)
    for i in range(n):
        if newstring[i] in trickslist:
            newstring[i] = ' '
    retstring = "".join(newstring)

    return retstring

x = "씨1발 뭐 fuc|< 5ex 젠.장"
print(trickCheck(StringReplacer(x)).replace(" ",""))