from uparser import wordparse
from joblib import Parallel, delayed
from tqdm import tqdm

# path1_telugu='/home/speech/Desktop/new_parser_vik/Unified_Parser_vikram_git/telugu/rough'
# with open(path1_telugu, 'r') as f:
#     words = f.readlines()

# words = [wd.strip() for wd in words]
# anslist = Parallel(n_jobs=3)(delayed(wordparse)(wd, 0, 0, 0) for wd in tqdm(words))

# with open('telugu/telugu_results_rough2.txt', 'w') as f:
#     for i in range(len(words)):
#         f.write(f'{words[i]} = {anslist[i]}\n')



## Bengali
# path_bengali_input="/home/speech/Desktop/new_parser_vik/Unified_Parser_vikram_git/bengali/bengali.words"
# with open(path_bengali_input, 'r') as f:
#     words = f.readlines()

# words = [wd.strip() for wd in words]
# anslist = Parallel(n_jobs=4)(delayed(wordparse)(wd, 0, 1, 1) for wd in tqdm(words))

# path_bengali_oputput='/home/speech/Desktop/new_parser_vik/Unified_Parser_vikram_git/bengali/bengali_words_phones_NUP_syllable.txt'
# with open(path_bengali_oputput, 'w') as f:
#     for i in range(len(words)):
#         f.write(f'{words[i]} = {anslist[i]}\n')


##Hindi

# path_hindi_input="/home/speech/Desktop/new_parser_vik/Unified_Parser_vikram_git/hindi/hi.words"
# with open(path_hindi_input, 'r') as f:
#     words = f.readlines()

# words = [wd.strip() for wd in words]
# anslist = Parallel(n_jobs=4)(delayed(wordparse)(wd, 0, 1, 1) for wd in tqdm(words))

# path_hindi_oputput='//home/speech/Desktop/new_parser_vik/Unified_Parser_vikram_git/hindi/hi.words_syllable.txt'
# with open(path_hindi_oputput, 'w') as f:
#     for i in range(len(words)):
#         f.write(f'{words[i]} = {anslist[i]}\n')



## Tamil

# path_tamil_input="/home/speech/Desktop/new_parser_vik/Unified_Parser_vikram_git/tamil/tamil.words"
# with open(path_tamil_input, 'r') as f:
#     words = f.readlines()

# words = [wd.strip() for wd in words]
# anslist = Parallel(n_jobs=1)(delayed(wordparse)(wd, 0, 0, 1) for wd in tqdm(words))

# path_tamil_oputput='/home/speech/Desktop/new_parser_vik/Unified_Parser_vikram_git/tamil/tamil_words_phones_NUP_phone.txt'
# with open(path_tamil_oputput, 'w') as f:
#     for i in range(len(words)):
#         f.write(f'{words[i]} = {anslist[i]}\n')

## assami

# path_tamil_input="/home/speech/Desktop/new_parser_vik/Unified_Parser_vikram_git/assamese/assamese.words"
# with open(path_tamil_input, 'r') as f:
#     words = f.readlines()

# words = [wd.strip() for wd in words]
# anslist = Parallel(n_jobs=3)(delayed(wordparse)(wd, 0, 0, 0) for wd in tqdm(words))

# path_assamese_oputput='/home/speech/Desktop/new_parser_vik/Unified_Parser_vikram_git/assamese/assamese_words_phones_NUP.txt'
# with open(path_assamese_oputput, 'w') as f:
#     for i in range(len(words)):
#         f.write(f'{words[i]} = {anslist[i]}\n')


##Rajasthani

# path_rajasthani_input="/home/speech/Desktop/new_parser_vik/Unified_Parser_vikram_git/rajasthani/rajasthani.words"
# with open(path_rajasthani_input, 'r') as f:
#     words = f.readlines()

# words = [wd.strip() for wd in words]
# anslist = Parallel(n_jobs=4)(delayed(wordparse)(wd, 0, 0, 0) for wd in tqdm(words))

# path_rajasthani_oputput='/home/speech/Desktop/new_parser_vik/Unified_Parser_vikram_git/rajasthani/rajasthani_NUP_phone.txt'
# with open(path_rajasthani_oputput, 'w') as f:
#     for i in range(len(words)):
#         f.write(f'{words[i]} = {anslist[i]}\n')

##marathi
# path_marathi_input="/home/speech/Desktop/new_parser_vik/Unified_Parser_vikram_git/marathi/marathi.words"
# with open(path_marathi_input, 'r') as f:
#     words = f.readlines()

# words = [wd.strip() for wd in words]
# anslist = Parallel(n_jobs=4)(delayed(wordparse)(wd, 0, 0, 0) for wd in tqdm(words))

# path_marathi_oputput='/home/speech/Desktop/new_parser_vik/Unified_Parser_vikram_git/marathi/marathi_NUP_phone.txt'
# with open(path_marathi_oputput, 'w') as f:
#     for i in range(len(words)):
#         f.write(f'{words[i]} = {anslist[i]}\n')


##odiya
# path_odiya_input="/home/speech/Desktop/new_parser_vik/Unified_Parser_vikram_git/odiya/odia.words"
# with open(path_odiya_input, 'r') as f:
#     words = f.readlines()

# words = [wd.strip() for wd in words]
# anslist = Parallel(n_jobs=4)(delayed(wordparse)(wd, 0, 0, 0) for wd in tqdm(words))

# path_odiya_oputput='/home/speech/Desktop/new_parser_vik/Unified_Parser_vikram_git/odiya/odia_NUP_phone.txt'
# with open(path_odiya_oputput, 'w') as f:
#     for i in range(len(words)):
#         f.write(f'{words[i]} = {anslist[i]}\n')


##Gujrathi
# path_gujrathi_input="/home/speech/Desktop/new_parser_vik/Unified_Parser_vikram_git/gujrathi/gujarati.words"
# with open(path_gujrathi_input, 'r') as f:
#     words = f.readlines()

# words = [wd.strip() for wd in words]
# anslist = Parallel(n_jobs=4)(delayed(wordparse)(wd, 0, 0, 0) for wd in tqdm(words))

# path_gujrathi_oputput='/home/speech/Desktop/new_parser_vik/Unified_Parser_vikram_git/gujrathi/gujarati_NUP_phone.txt'
# with open(path_gujrathi_oputput, 'w') as f:
#     for i in range(len(words)):
#         f.write(f'{words[i]} = {anslist[i]}\n')

# #malayalam
# path_malayalam_input="/home/speech/Desktop/new_parser_vik/Unified_Parser_vikram_git/malayalam/malayalam_old_data_unique_words.txt"
# with open(path_malayalam_input, 'r') as f:
#     words = f.readlines()

# words = [wd.strip() for wd in words]
# anslist = Parallel(n_jobs=4)(delayed(wordparse)(wd, 0, 0, 0) for wd in tqdm(words))

# path_malayalam_oputput='/home/speech/Desktop/new_parser_vik/Unified_Parser_vikram_git/malayalam/malayalam_NUP_phone.txt'
# with open(path_malayalam_oputput, 'w') as f:
#     for i in range(len(words)):
#         f.write(f'{words[i]} = {anslist[i]}\n')


#hindhi_sudhenshu_file
path_hi_input="/home/speech/Desktop/new_parser_vik/Unified_Parser_vikram_git/for comparision_hindhi_sudhanshu/unique_words.words"
with open(path_hi_input, 'r') as f:
    words = f.readlines()

words = [wd.strip() for wd in words]
anslist = Parallel(n_jobs=4)(delayed(wordparse)(wd, 0, 0, 0) for wd in tqdm(words))

path_hi_oputput='/home/speech/Desktop/new_parser_vik/Unified_Parser_vikram_git/for comparision_hindhi_sudhanshu/hi_old_python_parser.txt'
with open(path_hi_oputput, 'w') as f:
    for i in range(len(words)):
        f.write(f'{words[i]} = {anslist[i]}\n')