#  beautiful days at the movies
def solve(i, j, k):
    count = 0
    for x in range(i, j + 1):
        invert_x = int(str(x)[::-1])
        sum_x = abs(x - invert_x)
        if sum_x % k == 0:
            count += 1
    return count


if __name__ == "__main__":
    ijk = input().rstrip().split()
    i = int(ijk[0])
    j = int(ijk[1])
    k = int(ijk[2])
    # i = 20
    # j = 23
    # k = 6
    print(solve(i, j, k))