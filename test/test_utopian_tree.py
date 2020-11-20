from HackerRank.Algorithms.utopian_tree import solve


def test_caso_n_igual_zero():
    n = 0

    assert solve(n) == 1

def test_caso_n_maior_que_zero():
    n = 5

    assert solve(n) == 14
