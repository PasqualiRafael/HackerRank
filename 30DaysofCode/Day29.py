def solve(n, k):        
    n_max = 0
    for a in range(n - 1, 1, -1):
        for b in range(n, a, -1):
            ab = a&b
            if ab < k and ab > n_max:
                n_max = ab
            if n_max == k-1:
                break
        if n_max == k-1:
            break            
    print(n_max)

def ask(t):
    for _ in range(t):
        n, k = map(int, input().split())
        solve(n, k)
    
if __name__ == '__main__':
    test_case = int(input())
    ask(test_case)    
    
  
  