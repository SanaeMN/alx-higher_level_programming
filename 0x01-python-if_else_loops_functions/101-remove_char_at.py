#!/usr/bin/python3
def remove_char_at(str, nbr):
    ss = ''
    for i in range(len(str)):
        if i == nbr:
            continue
        ss += str[i]
    return ss
