import sys 

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

origin_txt = sys.argv[1]

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

# load text
origin_file = open(origin_txt, 'rt', encoding='UTF8')

text = []
while(True):
    paragraph = origin_file.readline()
    if not paragraph:
        break
    paragraph = paragraph.strip()
    lines = paragraph.split('.')
    lines = [v for v in lines if v]
    if len(lines):
        for i in range(len(lines)):
            lines[i] = lines[i].strip()
        text.append(lines)
print(text)

origin_file.close()

refine_text = []

for paragraph in text:
    refine_paragraph = []
    for line in paragraph:
        # words = line.split()
        # for i in range(len(words)):
        #     word = words[i]
        #     for fword in swear_set:
        #         idx = word.find(fword)
        #         if idx >= 0:
        #             fword_len = len(fword)
        #             new_word = '나쁜말' + word[idx + fword_len:]
        #             words[i] = new_word
        filterline = trickCheck(line)
        # filterline2 = trickCheck(StringReplacer(line))
        
        fline = filterline.replace("-","")
        for fword in swear_list:
            while fword in fline:
                filterline = replacefword(filterline, fword)
                fline = fline.replace(fword,"*"*len(fword),1)
        filterline = filterline.replace("-"," ")
        refine_paragraph.append(filterline)
    refine_text.append(refine_paragraph)

new_txt = sys.argv[2]

new_file = open(new_txt, 'wt', encoding='UTF-8')

for paragraph in refine_text:
    for line in paragraph:
        print(line)
        new_file.write(line + '. ')
    new_file.write('\n')

new_file.close()