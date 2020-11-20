def divisibleSumPairs(n, k, ar):
    count = 0
    for i in range(n):
        for j in range(i+1, n):
            if (ar[i] + ar[j]) % k == 0:
                count += 1

    return count




if __name__ == '__main__':
    n = int(6)
    k = int(3)
    ar = list([1, 3, 2, 6, 1, 2])
    print(divisibleSumPairs(n, k, ar))
    

