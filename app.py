import numpy as np
import json
from flask import Flask, request, jsonify

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

trickslist = [' ','1','2','3','4','5','6','7','8','9','.',',']

def trickCheck(targstr):
    n = len(targstr)
    newstring = list(targstr)
    for i in range(n):
        if newstring[i] in trickslist:
            newstring[i] = '-'
    retstring = "".join(newstring)

    return retstring

def replacefword(string,fword):
    n = len(string)
    m = len(fword)
    word = ""
    c = 0
    for i in range(n-m):
        j = 0
        while (j < m):
            if string[i+j+c] == '-':
                j -= 1
                word += '-'
                c += 1
            elif string[i+j+c]==fword[j]:
                word += fword[j]
            else:
                word = ""
                c = 0
                break
            j += 1
        if len(word) == m+c:
            break
        
    word = word.strip("-")
    string = string.replace(word,"*"*len(word),1)
    
    return string

    
# code start
# load swearlist

swear_txt = ['fword_list.txt']

swear_list = []
for slist in swear_txt:
    f = open(slist, 'rt', encoding='UTF8')
    while(True):
        word = f.readline()
        if not word:
            break
        word = word.strip()
        swear_list.append(word)
    f.close()
swear_list.sort(key=len, reverse=True)


app = Flask(__name__)

@app.route('/test', methods=['POST'])
def test():
    lists = request.args['file_name']
    lists = lists.split(',')
    data = []
    for list in lists:
        data.append(list)
    
    

    return jsonify({
        'result': data
    })

if __name__ == '__main__':
    app.run()