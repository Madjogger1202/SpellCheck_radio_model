
import numpy as np
from err_generator import generate_noice_ch
import pandas as pd
import time
import numpy as np
import pandas as pd
from catboost import CatBoostClassifier

good_symbols_en = " abcd-efghijklmnopqrstuvwxyz!,:.0123456789?'ABCDEFGHIJKLMNOPQRSTUVWXYZ"+'"'



def correct_symbol(line, symbol_index):
    a = np.arange(12)
    a.shape = (1, 12)
    line_num = 1
    start = time.time()
    symbol_correct = CatBoostClassifier()
    symbol_correct.load_model("symbol_correct.cbm")
    for i, char in enumerate(line):
        prev_char = line[i - 1] if i > 0 else ' '
        if (prev_char not in good_symbols_en):
            prev_char = '-'
        next_char = line[i + 1] if i < len(line) - 1 else ' '
        if (next_char not in good_symbols_en):
            next_char = '-'
        has_digit_nearby = any(c.isdigit() for c in (prev_char, next_char))
        has_space_nearby = ' ' in (prev_char, next_char)
        nearby_chars = f"{prev_char}{next_char}"
        symb=char
        symb = "0" * (8 - len(bin(ord(symb))[2:])) + str(bin(ord(symb))[2:])
        a = np.vstack([a, [symb[0], symb[1], symb[2], symb[3], symb[4], symb[5], symb[6], symb[7],
                                   1 * has_digit_nearby, 1 * has_space_nearby, nearby_chars, char]])
    t_elapced = (time.time() - start)  # /1000000.0
    df = pd.DataFrame(a)
    df.to_csv('symbols_data.csv', index=False)
    df_final = pd.read_csv('C:/Users/1/PycharmProjects/SpellCheckV2.0/symbols_data.csv')
    df_final = df_final[1:]
    #print(df_final)
    #df_final["11"][df_final["11"] == " "] = np.NaN
    df_final.fillna("space", inplace=True)

    X_data = df_final.drop('11', axis=1)
    y_predict=(symbol_correct.predict(X_data)).astype(str)
    if(y_predict[symbol_index][0]=='space'):
        return str(line[symbol_index])
    else:
        return str(y_predict[symbol_index][0])