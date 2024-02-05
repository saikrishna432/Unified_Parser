import sortedcontainers as sc
from helpers import RemoveUnwanted
from uparser import safe_word_parse
from tqdm import tqdm
from itertools import product



def get_mapping(lang_id = LANG_ID):
    symboltable = [[None for _ in range(2)] for _ in range(128)]
    with open('./common.map', 'r') as fl:
        lines = fl.readlines()
        for i in range(len(lines)):
            l = lines[i].strip().split('\t')
            symboltable[i][0] = l[1]
            symboltable[i][1] = l[1 + lang_id]
    return symboltable

def split_word(word, symbolTable):
    split_list = []
    for sym in word:
        idx = ord(sym)%128
        if idx in range(0,4) or idx in range(58,80) or idx in range(85, 88):
            split_list[-1] += sym
        else:
            split_list.append(sym)
    return split_list

# function to generate all sublists of a given list
def generate_sublists(lst):
    ln = len(lst)
    sublists = []
    for i in range(ln):
        for j in range(i+3, ln+1):
            sublist = lst[i:j]
            sublists.append((sublist, i, i + len(sublist) - 1))
    return sublists

# generate all prefixes of a given list
def generate_prefixes(lst):
    ln = len(lst)
    sublists = []
    for l in range(2, ln):
        sublists.append(lst[:l])
    
    sublists.reverse()
    return sublists

# we do weighted activity selection with weight = length of match in order to maximize
# the total portion of the word that is covered.
# reference - https://www.cs.princeton.edu/~wayne/cs423/lectures/dynamic-programming-4up.pdf
def weighted_activity_selection(activities, debug=False):

    N = len(activities)
    activities.sort(key = lambda x : (x[2], -x[1]))

    # finding the maximum indexed preceding activity that is compatible with the current activity
    preceding_compatible_activity = [None for i in range(N+1)]

    for i in range(1, N+1):
        comp_act = 0
        cur_act = activities[i-1]
        for j in range(1, i):
            cand = activities[j-1]
            if cand[2] < cur_act[1]:
                comp_act = j
        preceding_compatible_activity[i] = comp_act

    weights = [0 for i in range(N+1)]
    for i in range(1, N+1):
        cur_act = activities[i-1]
        weights[i] = cur_act[2] - cur_act[1] + 1

    opt = [0 for i in range(N+1)]
    ans = [[] for i in range(N+1)]

    for idx in range(1, N+1):
        opt[idx] = opt[idx-1]
        ans[idx] = ans[idx-1].copy()
        if weights[idx] + opt[preceding_compatible_activity[idx]] >= opt[idx]:
            opt[idx] = weights[idx] + opt[preceding_compatible_activity[idx]]
            ans[idx] = ans[preceding_compatible_activity[idx]] + [activities[idx-1]]
    if (debug):
        print('chosen words :', ans[N])
    return ans[N]

# remove unwanted symbols from word before passing it
def matching_based_parse(word, prefix_encodings, seed_word_encodings, symboltable, debug=False):
    if debug:
        print(f'debugging {word}')
    if word == '':
        return []
    
    spword = split_word(word, symboltable)
    prefixes = []
    # prefixes = generate_prefixes(spword)
    
    # print("list of prefixes")
    # print(prefix_encodings)
    match_prefix, pref_ans = [], []
    for pref in prefixes:
        if prefix_encodings.count(pref) != 0:
            # print(match_prefix)
            match_prefix = pref
            _, pref_ans = safe_word_parse(''.join(match_prefix), 1, 1, 1)
            pref_ans = [pref_ans]
            break
    remword = spword[len(match_prefix):]
    if debug:
        print(f'found prefix {"".join(match_prefix)}')
        print(f'remaining - {remword}')
        print(f'spword - {spword}')
    remword = spword[len(match_prefix):]

    sublists = generate_sublists(remword)
    print(sublists)
    matching_sublists = []
    for sublist, begpos, endpos in sublists:
        if seed_word_encodings.count(sublist) != 0:
            matching_sublists.append((sublist, begpos, endpos))
    
    if len(matching_sublists) == 0:
        _, ans = safe_word_parse(''.join(remword), 1, 1, 1)
        ans = [ans]
        return pref_ans + ans

    max_matching_sublists = weighted_activity_selection(matching_sublists, debug)
    if debug:
        for l, _, _ in max_matching_sublists:
            wd = ''.join(l)
            print(l, wd)
    
    idx = 0
    cur_act = 0
    parsings = pref_ans
    while idx < len(remword):

        if cur_act == len(max_matching_sublists):
            word = ''
            while (idx < len(remword)):
                word += remword[idx]
                idx += 1
            if word != '':
                _, parsing = safe_word_parse(word, 1, 1, 1)
                parsings += [parsing]
            break

        word = ''
        while (idx < max_matching_sublists[cur_act][1]):
            word += remword[idx]
            idx += 1
        if word != '':
            _, parsing = safe_word_parse(word, 1, 1, 1)
            parsings += [parsing]
        
        word = ''
        while (idx <= max_matching_sublists[cur_act][2]):
            word += remword[idx]
            idx +=1
        if word != '':
            _, parsing = safe_word_parse(word, 1, 1, 1)
            parsings += [parsing]
        
        cur_act += 1
    if debug:
        print(f'parsings - {parsings}')
    return parsings


def testing(symttable):
    # testing some functionality 
    sp = split_word('तितिम्मा', symbolTable=symttable)
    print(sp)
    sp = split_word('तितिलिका', symbolTable=symttable)
    print(sp)
    sp = split_word('कहाल', symbolTable=symttable)
    print(sp)


def generate_item(word):
    try:
        wd = RemoveUnwanted(word)
        wd_debug = True
        parsing = matching_based_parse(wd, prefix_words, seed_words, symttable, wd_debug)
        parsing = ''.join(parsing)
        if wd_debug:
            print(wd, parsing, sep='\t')
    except KeyError:
        parsing = 'FAILED'
        print(f'ignored {wd}')
    return [wd, f"(set! wordstruct '( {parsing}))"]



if __name__ == '__main__':

    # # we fix hindi as of now and may change it later
    LANG_ID = 5
    # MAX_LENGTH = 5
    # MIN_LENGTH = 3
    DEBUG = False

    # checking from here
    symttable = get_mapping()
    # now, we open the file containing all the hindi words
    words = []
    path_words_bengali='/home/speech/Desktop/new_parser_vik/Unified_Parser_vikram_git/bengali/bengali.words.txt'
    with open(path_words_bengali, 'r') as fl:
        cnts = fl.readlines()
        for ln in cnts:
            ln = ln.strip()
            ln = RemoveUnwanted(ln)
            words.append(ln)

    # words.sort(key=lambda x : (len(encode_split_word(split_word(x,symttable), sym2id)), x))
    path_seeds_bengali='/home/speech/Desktop/new_parser_vik/Unified_Parser_vikram_git/seed_dict/bengali_seed_dict.txt'
    seed_words = sc.SortedList()
    with open(path_seeds_bengali, 'r') as fl:
        cnts = fl.readlines()
        for ln in cnts:
            ln = ln.strip()
            wd, parsing = ln.split('\t')
            try:
                wd = RemoveUnwanted(wd)
                spword = split_word(wd, symttable)
            except:
                continue
            if len(spword) >= 2:
                seed_words.add(spword)

    # load a separate prefix file... maybe use the set of seed words itself??
    prefix_words = sc.SortedList()
    with open('prefixes_hindi.txt', 'r') as fl:
        cnts = fl.readlines()
        for ln in cnts:
            wd = ln.strip()
            try:
                wd = RemoveUnwanted(wd)
                spword = split_word(wd, symttable)
            except:
                continue
            if len(spword) >= 2:
                prefix_words.add(spword)


    words = ['लोकसभा','उसका','ताजमहल','है','अवश्यम्भावी','निराशा','सबक़','कुंड']
    items = []
    for wd in tqdm(words):
        items.append(generate_item(wd))

    with open('out36.txt', 'w') as f:
        for wd, parsing in items:
            f.write(wd + '\t' + parsing + '\n')
