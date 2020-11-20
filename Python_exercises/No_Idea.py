def count_happy(Q, A, B):
    happiness = 0

    A = set(A)
    B = set(B)

    for i in Q:
        if i in A:
            happiness += 1
        elif i in B:
            happiness -= 1 
    return happiness



if __name__ == '__main__':
    nm = input().strip().split()    
    n = nm[0]
    m = nm[1]
    compare = list(map(int, input().strip().split()))
    A = list(map(int, input().strip().split()))
    B = list(map(int, input().strip().split()))
    print(count_happy(compare, A, B))
    






            