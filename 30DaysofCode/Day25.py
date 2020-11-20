from math import sqrt

def isPrime(n):
    for i in range(2, int(sqrt(n)+1)):
        if n % i == 0:
            return False
    return True

if __name__ == '__main__':  
    T = int(input())
    for _ in range(T):        
        n = int(input())
        if n >= 2 and isPrime(n):
            print("Prime")
        else:
            print("Not prime")      

