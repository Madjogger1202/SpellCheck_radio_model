#создаём датасет, который содежит входные данные
#колонки/входной текст/процент ошибок/выходной текст

import numpy as np
from err_generator import generate_noice_ch
import pandas as pd
import time
import numpy as np
import pandas as pd


def process_character(char, prev_char, next_char):
    has_digit_nearby = any(c.isdigit() for c in (prev_char, next_char))   
    has_space_nearby = ' ' in (prev_char, next_char)
    nearby_chars = f"{prev_char}{char}{next_char}"

    return f"Символ: {char}, В радиусе 2 символов есть число: {has_digit_nearby}, Рядом с символом пробел: {has_space_nearby}, Ближайшие 2 символа: {nearby_chars}\n"


input_file_path = "eng_news_2005_10K-sentences.txt"  # Укажите путь к вашему входному файлу
output_file_path = "output_prop.csv"  # Укажите путь к вашему выходному файлу
good_symbols_en = " abcd-efghijklmnopqrstuvwxyz!,:.0123456789?'ABCDEFGHIJKLMNOPQRSTUVWXYZ"+'"'
a = np.arange(12)
a.shape=(1, 12)

line_num=1;
start = time.time()
for line in open(input_file_path, 'r', encoding='UTF8'):
    for i, char in enumerate(line):
      if(char in good_symbols_en):
        prev_char = line[i - 1] if i > 0 else ' '
        if(prev_char not in good_symbols_en):
          prev_char='-'
        next_char = line[i + 1] if i < len(line) - 1 else ' '
        if(next_char not in good_symbols_en):
          next_char='-'
        has_digit_nearby = any(c.isdigit() for c in (prev_char, next_char))
        has_space_nearby = ' ' in (prev_char, next_char)
        nearby_chars = f"{prev_char}{next_char}"
        for perc in ([0.5, 0.7, 0.8]):
          symb=generate_noice_ch(char, perc)
          if(symb not in good_symbols_en):
              symb="0"*(8-len(bin(ord(symb))[2:]))+str(bin(ord(symb))[2:])
              a=np.vstack([a, [symb[0], symb[1], symb[2], symb[3], symb[4], symb[5], symb[6], symb[7], 1*has_digit_nearby, 1*has_space_nearby, nearby_chars, char]])
        #print(a[-1])
        #print(str(float(line_num)/10000.0)+"%")
    t_elapced = (time.time()-start)#/1000000.0
    print(str(float(line_num)/100.0)+"% Прошло времени: " + str(t_elapced) +"c")
    line_num+=1;
df = pd.DataFrame(a)
df.to_csv('symbols_data.csv', index=False)