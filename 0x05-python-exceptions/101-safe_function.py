#!/usr/bin/python3
def safe_function(fct, *args):
    try:
        result = fct(*args)
    except Exception as err:
        from sys import stderr
        stderr.write("Exception: {}\n".format(err))
        result = None
    return result
