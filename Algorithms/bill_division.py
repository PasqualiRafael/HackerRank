def solve(bill, k, b):
    del bill[k]
    anna = sum(bill) / 2
    result = int(b - anna)
    if result == 0:
        result = f"Bon Appetit"
    return result


if __name__ == "__main__":
    nk = input().rstrip().split()
    n = int(nk[0])
    k = int(nk[1])
    bill = list(map(int, input().rstrip().split()))
    b = int(input().strip())
    print(solve(bill, k, b))