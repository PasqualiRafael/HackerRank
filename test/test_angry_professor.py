from HackerRank.Algorithms.angry_professor import solve


def test_class_cancelled():
    min_students = 3
    arrival_time = [-1, -3, 4, 2]

    assert solve(min_students, arrival_time) == f'YES'


def test_class_not_cancelled():
    min_students = 2
    arrival_time = [0, -1, 2, 1]

    assert solve(min_students, arrival_time) == f'NO'

