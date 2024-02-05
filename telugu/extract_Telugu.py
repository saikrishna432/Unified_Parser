words = set()
path='/home/speech/Desktop/new_parser_vik/telugu/telugutext-total1.txt'
with open(path, 'r') as f:
    cnts = f.readlines()
    for l in cnts:
        l = l.strip('\n').split(' ')
        for wd in l[1:]:
            wd = wd.strip('.,|? ')
            if wd != '':
                words.add(wd)

words = list(words)
words = sorted(words)
path2='/home/speech/Desktop/new_parser_vik/telugu/telugu.txt'
with open(path2, 'w') as f:
    for w in words:
        f.write(f'{w}\n')