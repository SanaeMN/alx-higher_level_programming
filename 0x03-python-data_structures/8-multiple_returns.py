#!/usr/bin/python3
def multiple_returns(sentence):
    str = len(sentence)
    if str == 0:
        return 0, None
    return str, sentence[0]
