# test case
from palindrome import *


def test_is_pal():
    assert is_palindrome('asdf', 'fdsa', False, 8) == True


def test_prep():
    assert prep('asdffdsa') == True
    assert prep('radar') == True
    assert prep('toot') == True
    assert prep('robot') == False
