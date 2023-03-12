#!/usr/bin/python3

def multiple_returns(sentence):
    if len(sentence) == 0:
	first_char = None
        new_tuple = (0, first_char)
        return new_tuple
    else:
	first_char = sentence[0]
        new_tuple = (len(sentence), first_char)
        return new_tuple
