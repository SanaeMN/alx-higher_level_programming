#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    return {key: 2 * a_dictionary[key] for key in a_dictionary.keys()}
