
# path1="/home/speech/Desktop/new_parser_vik/Unified_Parser_vikram_git/bengali/bengali_words_phones_NUP.txt"
# path1_tamil='/home/speech/Desktop/new_parser_vik/Unified_Parser_vikram_git/tamil/tamil_words_phones_NUP_phone.txt'
# path1_assamis='/home/speech/Desktop/new_parser_vik/Unified_Parser_vikram_git/assamese/assamese_words_phones_NUP.txt'
# path1_gujrathi='/home/speech/Desktop/new_parser_vik/Unified_Parser_vikram_git/gujrathi/gujarati_NUP_phone.txt'
# path1_marathi="/home/speech/Desktop/new_parser_vik/Unified_Parser_vikram_git/marathi/marathi_NUP_phone.txt"
# path1_odiya='/home/speech/Desktop/new_parser_vik/Unified_Parser_vikram_git/odiya/odia_NUP_phone.txt'
# path1_rajasthani="/home/speech/Desktop/new_parser_vik/Unified_Parser_vikram_git/rajasthani/rajasthani_NUP_phone.txt"
path1_malayalam="/home/speech/Desktop/new_parser_vik/Unified_Parser_vikram_git/malayalam/malayalam_NUP_phone.txt"
with open(path1_malayalam, 'r') as f_new:
    words_new = f_new.readlines()

# path2_bengali="/home/speech/Desktop/new_parser_vik/Unified_Parser_vikram_git/bengali/bengali.dict.OUP"
# path2_tamil='/home/speech/Desktop/new_parser_vik/Unified_Parser_vikram_git/tamil/tamil.dict.OUP'
# path2_assamies='/home/speech/Desktop/new_parser_vik/Unified_Parser_vikram_git/assamese/assame.dict.OUP'
# path2_gujrathi='/home/speech/Desktop/new_parser_vik/Unified_Parser_vikram_git/gujrathi/gujarati.dict'
# path2_marathi='/home/speech/Desktop/new_parser_vik/Unified_Parser_vikram_git/marathi/marathi.dict'
# path2_odiya="/home/speech/Desktop/new_parser_vik/Unified_Parser_vikram_git/odiya/odia.dict"
# path2_rajasthani='/home/speech/Desktop/new_parser_vik/Unified_Parser_vikram_git/rajasthani/rajasthani.dict'
path2_malayalam="/home/speech/Desktop/new_parser_vik/Unified_Parser_vikram_git/malayalam/malayalam_OUP.txt"

with open(path2_malayalam, 'r') as f_old:
    words_old = f_old.readlines()

words_new = [wd.strip("\n") for wd in words_new]
words_old = [wd.strip("\n") for wd in words_old]
# print(words_old)
count=0
not_match=0
for wd in words_new:
    if wd in words_old:
        words_new.remove(wd)
        words_old.remove(wd)
        count=count+1
        print(count)
    else:
        not_match=not_match+1
        print("Not_match_found=%d" %not_match)

print(len(words_new), len(words_old))

for wd in words_old:
    if wd in words_new:
        words_new.remove(wd)
        words_old.remove(wd)
        count=count+1
        print(count)
    else:
        not_match=not_match+1
        print("Not_match_found=%d" %not_match)

print(len(words_new), len(words_old))


for wd in words_new:
    if wd in words_old:
        words_new.remove(wd)
        words_old.remove(wd)
        count=count+1
        print(count)
    else:
        not_match=not_match+1
        print("Not_match_found=%d" %not_match)

print(len(words_new), len(words_old))

for wd in words_old:
    if wd in words_new:
        words_new.remove(wd)
        words_old.remove(wd)
        count=count+1
        print(count)
    else:
        not_match=not_match+1
        print("Not_match_found=%d" %not_match)

print(len(words_new), len(words_old))

for wd in words_new:
    if wd in words_old:
        words_new.remove(wd)
        words_old.remove(wd)
        count=count+1
        print(count)
    else:
        not_match=not_match+1
        print("Not_match_found=%d" %not_match)

print(len(words_new), len(words_old))

for wd in words_old:
    if wd in words_new:
        words_new.remove(wd)
        words_old.remove(wd)
        count=count+1
        print(count)
    else:
        not_match=not_match+1
        print("Not_match_found=%d" %not_match)

print(len(words_new), len(words_old))


for wd in words_new:
    if wd in words_old:
        words_new.remove(wd)
        words_old.remove(wd)
        count=count+1
        print(count)
    else:
        not_match=not_match+1
        print("Not_match_found=%d" %not_match)

print(len(words_new), len(words_old))

for wd in words_old:
    if wd in words_new:
        words_new.remove(wd)
        words_old.remove(wd)
        count=count+1
        print(count)
    else:
        not_match=not_match+1
        print("Not_match_found=%d" %not_match)

for wd in words_new:
    if wd in words_old:
        words_new.remove(wd)
        words_old.remove(wd)
        count=count+1
        print(count)
    else:
        not_match=not_match+1
        print("Not_match_found=%d" %not_match)

print(len(words_new), len(words_old))

for wd in words_old:
    if wd in words_new:
        words_new.remove(wd)
        words_old.remove(wd)
        count=count+1
        print(count)
    else:
        not_match=not_match+1
        print("Not_match_found=%d" %not_match)

print(len(words_new), len(words_old))


for wd in words_new:
    if wd in words_old:
        words_new.remove(wd)
        words_old.remove(wd)
        count=count+1
        print(count)
    else:
        not_match=not_match+1
        print("Not_match_found=%d" %not_match)

print(len(words_new), len(words_old))

for wd in words_old:
    if wd in words_new:
        words_new.remove(wd)
        words_old.remove(wd)
        count=count+1
        print(count)
    else:
        not_match=not_match+1
        print("Not_match_found=%d" %not_match)

print(len(words_new), len(words_old))

for wd in words_new:
    if wd in words_old:
        words_new.remove(wd)
        words_old.remove(wd)
        count=count+1
        print(count)
    else:
        not_match=not_match+1
        print("Not_match_found=%d" %not_match)

print(len(words_new), len(words_old))

for wd in words_old:
    if wd in words_new:
        words_new.remove(wd)
        words_old.remove(wd)
        count=count+1
        print(count)
    else:
        not_match=not_match+1
        print("Not_match_found=%d" %not_match)

print(len(words_new), len(words_old))


for wd in words_new:
    if wd in words_old:
        words_new.remove(wd)
        words_old.remove(wd)
        count=count+1
        print(count)
    else:
        not_match=not_match+1
        print("Not_match_found=%d" %not_match)

print(len(words_new), len(words_old))

for wd in words_old:
    if wd in words_new:
        words_new.remove(wd)
        words_old.remove(wd)
        count=count+1
        print(count)
    else:
        not_match=not_match+1
        print("Not_match_found=%d" %not_match)

print(len(words_new), len(words_old))
print(count, not_match)
#path3="/home/speech/Desktop/new_parser_vik/Unified_Parser_vikram_git/bengali/bengali_comp_results.txt"
#path3_tamil="/home/speech/Desktop/new_parser_vik/Unified_Parser_vikram_git/tamil/tamil_comp_results.txt"
# path3_assamies="/home/speech/Desktop/new_parser_vik/Unified_Parser_vikram_git/assamese/assamies_comp_results.txt"
# path3_gujrathi='/home/speech/Desktop/new_parser_vik/Unified_Parser_vikram_git/gujrathi/gujarati_comp_results.txt'
# path3_marathi='/home/speech/Desktop/new_parser_vik/Unified_Parser_vikram_git/marathi/marathi_comp_results.txt'
# path3_odiya='/home/speech/Desktop/new_parser_vik/Unified_Parser_vikram_git/odiya/odia_comp_results.txt'
# path3_rajasthani='/home/speech/Desktop/new_parser_vik/Unified_Parser_vikram_git/rajasthani/rajasthani_comp_results.txt'
path3_malayalam='/home/speech/Desktop/new_parser_vik/Unified_Parser_vikram_git/malayalam/malayalam_comp_results.txt'

with open(path3_malayalam, 'w') as f:
    for i in range(len(words_old)):
        f.write(words_old[i])
        f.write('\n')
    
    f.write("From here sentences from new parser")
    
    for i in range(len(words_new)):
        f.write(words_new[i])
        f.write('\n')
            