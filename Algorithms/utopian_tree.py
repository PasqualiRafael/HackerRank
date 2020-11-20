def solve(n_cycles):
    b = 1
    if n_cycles == 0:
        return b
    else:
        for i in range(1, n_cycles + 1):
            if i % 2 == 0:
                b += 1
            else:
                b = b * 2
        return b


if __name__ == "__main__":
    test_case = int(input())

    for _ in range(test_case):
        n_cycles = int(input())
        print(solve(n_cycles))
