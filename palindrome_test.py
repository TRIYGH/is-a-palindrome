from palindrome import is_palindrome, prep, main


def test_is_pal():
    assert is_palindrome('asdf', 'fdsa', False, 4) is False
    assert is_palindrome('asdf', 'asdf', False, 4) is True


def test_prep():
    assert prep('asdffdsa') is True
    assert prep('radar') is True
    assert prep('toot') is True
    assert prep('robot') is False

#
# def test_total():
#     assert main('asdfdsa') is True
#     assert main('asdffff') is False
# requires user input
