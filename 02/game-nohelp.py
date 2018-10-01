#!python3
# Code Challenge 02 - Word Values Part II - a simple game
# http://pybit.es/codechallenge02.html

import random
import numpy as np

from data import DICTIONARY, LETTER_SCORES, POUCH

NUM_LETTERS = 7


# re-use from challenge 01
def calc_word_value(word):
    """Calculate a given word value based on Scrabble LETTER_SCORES mapping."""
    return sum(LETTER_SCORES.get(character, 0) for character in word.upper())

# re-use from challenge 01
def max_word_value(words):
    """Calculate the max value of a collection of words."""
    return max(words, key=calc_word_value)

def draw_letters():
    """Return a list of 7 letters drawn randomly from POUCH."""
    return [POUCH[l] for l in np.random.randint(0, len(POUCH), size=7)]

def input_word(letters):
    """Ask user for a word given set of letters and return score for valid word."""
    valid_word = False
    while not valid_word:
        word = input('Use the letters {} to make a word: '.format(letters)).upper()
        valid_word = _validate_word(word, letters)
    word_value = calc_word_value(word)
    print('{} has a score of {}!'.format(word, word_value))

def _validate_word(word, letters):
    """Check that all word is in dictionary and contains only valid letters."""



def main():
    letters = draw_letters()
    input_word(letters)


if __name__ == "__main__":
    main()
