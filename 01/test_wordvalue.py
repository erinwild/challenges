import pytest

from data import DICTIONARY, LETTER_SCORES
from wordvalue import load_words, calc_word_value, max_word_value

TEST_WORDS = ('bob', 'julian', 'pybites', 'quit', 'barbeque')

class TestWordValue(object):

    def test_load_words(self):
        words = load_words()
        assert len(words) == 235886
        assert words[0] == 'A'
        assert words[-1] == 'Zyzzogeton'
        assert ' ' not in ''.join(words)

    def test_calc_word_value(self):
        assert calc_word_value('bob') == 7
        assert calc_word_value('JuliaN') == 13
        assert calc_word_value('PyBites') == 14
        assert calc_word_value('benzalphenylhydrazone') == 56

    def test_max_word_value(self):
        assert max_word_value(TEST_WORDS) == 'barbeque'
        assert max_word_value() == 'benzalphenylhydrazone'

if __name__ == '__main__':
   pytest.main()
