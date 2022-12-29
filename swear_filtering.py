import numpy as np
import sys 

wrong_word = '나쁜말'

swear_txt = ['fword_list.txt']

origin_txt = sys.argv[1]

swear_list = []
for list in swear_txt:
    f = open(list, 'rt', encoding='UTF8')
    while(True):
        word = f.readline()
        if not word:
            break
        word = word.strip()
        swear_list.append(word)
    f.close()
swear_list.sort(key=len, reverse=True)

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

        for fword in swear_list:
            if fword in line:
                replace_word = "" + wrong_word * (len(fword) // 3)
                if len(fword) % 3 == 1:
                    replace_word = '말' + replace_word
                elif len(fword) % 3 == 2:
                    replace_word = '쁜말' + replace_word
                replace_word = '"' + replace_word + '"'
                line = line.replace(fword, replace_word)
        
        #refine_line = ' '.join(words)
        refine_paragraph.append(line)
    refine_text.append(refine_paragraph)

new_txt = 'refined_' + origin_txt

new_file = open(new_txt, 'wt', encoding='UTF-8')

for paragraph in refine_text:
    for line in paragraph:
        print(line)
        new_file.write(line + '. ')
    new_file.write('\n')

new_file.close()
            

