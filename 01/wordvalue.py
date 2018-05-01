from data import DICTIONARY, LETTER_SCORES
import numpy as np

def load_words():
    """Load dictionary into a list and return list"""
    return np.loadtxt(DICTIONARY, dtype=str).tolist()

def calc_word_value(word):
    """Calculate the value of the word entered into function
    using imported constant mapping LETTER_SCORES"""
    return sum(LETTER_SCORES.get(character, 0) for character in word.upper())

def max_word_value(words=load_words()):
    """Calculate the word with the max value, can receive a list
    of words as arg, if none provided uses default DICTIONARY"""
    return max(words, key=calc_word_value)

if __name__ == '__main__':
    pass # run unit tests to validate
