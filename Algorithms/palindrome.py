def solve(a, b):
    if len(a + b) <= 8:
        s = (a + b)
        n = 0
        k = -1        
        palindromic = True
        for _ in range(int(len(s))//2):
            if s[n] == s[k]:
                n += 1
                k -= 1
            else:
                palindromic = False
                break
        if palindromic == True:
            return s
        else:
            return -1
    else:
        return None     
        


if __name__ == '__main__':
    test_case = int(input())
    for _ in range(test_case):
        a = str(input().lower())
        b = str(input().lower())
        print(solve(a, b))