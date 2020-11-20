from HackerRank.Algorithms.palindrome import solve

def test_if_len_of_string_more_than_eight_stop():
    a = f'abcde'
    b = f'abcd'

    assert solve(a, b) == None

def test_if_not_palindromic_return_negative_one():
    a = f'abcd'
    b = f'abc'

    assert solve(a, b) == -1

def test_if_is_palindromic_return_string():
    a = f'abcd'
    b = f'cba'
    s = (a + b)

    assert solve(a, b) == s