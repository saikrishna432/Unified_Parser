words = set()
with open('/home/speech/Desktop/new_parser_vik/Unified_Parser_vikram_git/malayalam/txt.done.data', 'r') as f:
    cnts = f.readlines()
    for l in cnts:
        l = l.strip('\n').split(' ')
        for wd in l[:]:
            wd = wd.strip('.,|? ')
            if wd != '':
                words.add(wd)

words = list(words)
words = sorted(words)
with open('malayalam_olddata_words.txt', 'w') as f:
    for w in words:
        f.write(f'{w}\n')
