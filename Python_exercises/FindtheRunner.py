def second_max(arr):    
    return max([x for x in arr if x != max(arr)])
    
#     arr.sort(reverse=True)
#     x = arr.count(max(arr))
#     for i in range(x):
#         arr.remove(max(arr)) 
#     return arr[0]

if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    print(second_max(arr))    


