def solve(t, score):
    max_score = score[0]
    min_score = score[0]
    max_break = 0
    min_break = 0
    for n in range(1, t):    
        if score[n] > max_score:
            max_score = score[n]
            max_break += 1
        if score[n] < min_score:
            min_score = score[n]
            min_break += 1
    print(max_break, min_break)   

if __name__ == '__main__':
    t = int(input())
    score = list(map(int, input().strip().split()))

    solve(t, score)