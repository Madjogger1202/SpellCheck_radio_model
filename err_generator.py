import os
import random
import binascii
from bitarray import bitarray
def generate_noice(input = '', output_file_path='', err_percent=0.0):
    err_percent=int(err_percent*10)
    f = open(input,'r')
    start_txt = f.read()
    print(start_txt)
    f.close()
    recieved_str = ''
    for i in start_txt:
        out_char = (bin(ord(i))[2:].zfill(8))
        str_bin_ch = ''
        for j in range(0, 8):
            if (random.randint(0, 1000) <= err_percent):
                if (out_char[j] == '1'):
                    str_bin_ch += '0'
                else:
                    str_bin_ch += '1'
            else:
                str_bin_ch += out_char[j]
                # set_bit(out_char, j, 0)
        bts = bitarray(str_bin_ch)
        recieved_str += bts.tobytes().decode('cp1251')
        # print(str_bin_ch)
        # print(recieved_str)

    print(recieved_str)
    f = open(output_file_path, 'w+')
    f.write(recieved_str)
    f.close()
    return recieved_str, start_txt
def generate_spaces(input = '', space_file_path=''):
    f = open(input, 'r')
    start_txt = f.read()
    print(start_txt)
    f.close()
    space_count = start_txt.count(' ')
    print(space_count)
    f = open(space_file_path, 'w+')
    out_txt = ''
    curr_pos = 0
    for i in start_txt:
        if (i == ' '):
            # print(curr_pos)
            f.write(str(curr_pos) + '\n')
        curr_pos += 1
    f.close()


def generate_noice_ch(input='a', err_percent=0.0):
    err_percent*=10
    out_char = (bin(ord(input))[2:].zfill(8))
    str_bin_ch = ''
    for j in range(0, 8):
        if (random.randint(0, 1000) <= err_percent):
            if (out_char[j] == '1'):
                str_bin_ch += '0'
            else:
                str_bin_ch += '1'
        else:
            str_bin_ch += out_char[j]
            # set_bit(out_char, j, 0)
    bts = bitarray(str_bin_ch)
    if(ord(bts.tobytes()) <0x97):
        recieved_str = bts.tobytes().decode('cp1251')
    else:
        recieved_str = chr(0x97)
    return recieved_str