from HackerRank.Algorithms.beautiful_days_atthe_movies import solve


def test_case_eight_hackerank():
    i = 20
    j = 23
    k = 6

    assert solve(i, j, k) == 2


def test_case_nine_hackerank():
    i = 13
    j = 45
    k = 3

    assert solve(i, j, k) == 33