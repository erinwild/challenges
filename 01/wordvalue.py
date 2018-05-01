from data import DICTIONARY, LETTER_SCORES
import numpy as np

def load_words():
    """Load dictionary into a list and return list"""
    return np.loadtxt(DICTIONARY, dtype=str).tolist()

def calc_word_value(word):
    """Calculate the value of the word entered into function
    using imported constant mapping LETTER_SCORES"""
    word_value = 0
    for character in word.upper():
        if character in LETTER_SCORES:
            word_value += LETTER_SCORES[character]
    return word_value

def max_word_value(word_list=None):
    """Calculate the word with the max value, can receive a list
    of words as arg, if none provided uses default DICTIONARY"""
    if word_list is None:
        word_list = load_words()

    word_with_max_value = ''
    max_value = 0
    for word in word_list:
        word_value = calc_word_value(word)
        if word_value > max_value:
            word_with_max_value = word
            max_value = word_value

    return word_with_max_value

if __name__ == '__main__':
    pass # run unittests to validate
