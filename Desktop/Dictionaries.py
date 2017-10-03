# import various text constants from `constants`
from constants import *
'''
Import quotes used in the function below
'''

def freq_threshold(text, n):
    # break the text into individual characters and count the occurence of each
    char_dict = {}
    for char in text:
        if char in char_dict:
            char_dict[char] += 1
        else:
            char_dict[char] = 1
    
    # calculate the characters which occur more than the user defined int n
    total = 0
    for count in char_dict.values():
        if count > n:
            total += 1
    
    #indenting should be fixed here
    return total
    #looks good
