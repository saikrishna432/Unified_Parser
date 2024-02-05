from indic_unified_parser.uparser import wordparse
from joblib import Parallel, delayed
from tqdm import tqdm               

path_malayalam_input="/home/speech/Desktop/new_parser_vik/Unified_Parser_vikram_git/malayalam/malayalam_old_data_unique_words.txt"
with open(path_malayalam_input, 'r') as f:
    words = f.readlines()

words = [wd.strip() for wd in words]
anslist = Parallel(n_jobs=4)(delayed(wordparse)(wd, 0, 0, 0) for wd in tqdm(words))

path_malayalam_oputput='/home/speech/Desktop/new_parser_vik/Unified_Parser_vikram_git/malayalam/malayalam_OUP.txt'
with open(path_malayalam_oputput, 'w') as f:
    for i in range(len(words)):
        f.write(f'{words[i]} = {anslist[i]}\n')