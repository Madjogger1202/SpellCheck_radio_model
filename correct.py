import os
import random
import binascii
from bitarray import bitarray
import jamspell
import time
from autocorrect import Speller
from collections import Counter
from array import array
from symbol_correction import correct_symbol

def load_model(model_lang='', model_v=''):
    spell = Speller(lang='en')
    jsp = jamspell.TSpellCorrector()
    jsp.LoadLangModel('en_model.bin')
    return 'eng_model loaded', spell, jsp


def correct(input_path='', output_path='', spaces_file_path=''):
    spell = Speller(lang='en')
    jsp = jamspell.TSpellCorrector()
    jsp.LoadLangModel('en_model.bin')
    good_symbols_en = " %abcd-efghijklmnopqrstuvwxyz!,:.0123456789?'ABCDEFGHIJKLMNOPQRSTUVWXYZ" + '"'
    # bad_mid_symbols_en = "!,.0123456789?%:;+=-()/?[]|"
    # bad_start_symbols_en = "!,.?%:;+=-()/?[]|"
    # bad_end_symbols_en = "!0123456789?%:;+=-()/?[]|"
    # num_symbols = "0123456789"
    # letters_symbols_en = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    # extra_symbols_en = "'"
    f = open(input_path, 'r')
    input_str = f.read().rstrip()
    print(input_str)
    f.close()
    input_str = input_str.replace(" ", ".")
    list_str1 = list(input_str)
    with open(spaces_file_path, "r") as file:
        for line in file:
            # print(line)
            list_str1[int(line)] = ' '
    f = open(input_path, 'w+')
    f.write((''.join(list_str1)))
    print(list_str1)
    f.close()
    file.close()

    in_lines = []
    with open(input_path, 'r') as file:
        for line in file:
            in_lines.append(line)
    print(in_lines)
    file.close()

    start = time.time()

    my_file = open(output_path, "w+")
    for in_line in in_lines:
        input_str = in_line
        #print(jsp.FixFragment(input_str))
        list_str1 = list(input_str)
        for i in range(0, len(list_str1) - 1):
            if list_str1[i] not in good_symbols_en:
                list_str1[i]=correct_symbol(in_line, i)[0]
        print("после бинарной классификации:")
        # if list_str1[i] in num_symbols:
        #  if i>=1 and i<len(list_str1):
        #    if (list_str1[i-1] in letters_symbols_en) or (list_str1[i+1] in letters_symbols_en):
        #      list_str1[i]='/'
        # if list_str1[i] in bad_mid_symbols_en:
        #  if i>=1 and i<len(list_str1):
        #    if (list_str1[i-1] != ' ') or (list_str1[i+1] != ' '):
        #      list_str1[i]='/'
        new_str1 = ''.join(list_str1)
        print(new_str1)
        str_txt1 = jsp.FixFragment(spell(new_str1))
        print(str_txt1)
        new_txt1 = ''
        isNewW = True
        isFirstUpper = False
        for i in str_txt1:
            if (isNewW):
                isFirstUpper = i.isupper()
                isNewW = False
            elif (i.isupper() and (not isNewW) and (not isFirstUpper)):
                i = i.lower()
            if (i == ' '):
                isNewW = True
            new_txt1 += i

        str_txt1 = new_txt1
        str_final = spell(new_txt1).replace('/', '')
        print(str_final)
        my_file.write(str_final)
    my_file.close()

    end = time.time()
    return "jamspell обработал за : " + str((end - start) * 10 ** 3) + "ms", str_final
