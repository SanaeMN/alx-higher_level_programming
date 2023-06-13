#!/usr/bin/python3
def no_c(my_string):
    ch = ''
    for c in my_string:
        if c in 'cC':
            continue
        ch += c
    return ch
