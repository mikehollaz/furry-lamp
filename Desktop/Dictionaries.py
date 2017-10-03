# import various text constants from `constants`
from constants import *

def freq_threshold(text, n):
    char_dict = {}
    for char in text:
        if char in char_dict:
            char_dict[char] += 1
        else:
            char_dict[char] = 1

    total = 0
    for count in char_dict.values():
        if count > n:
            total += 1

    return total
