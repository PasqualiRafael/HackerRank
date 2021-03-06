#!/bin/python3

import sys

n = int(input().strip())
a = list(map(int, input().strip().split(' ')))
# Write Your Code Here
num_swaps = 0
for i in range(n):
    for j in range(n - 1):
        if a[j] > a[j + 1]:
            tmp = a[j]
            a[j] = a[j + 1]
            a[j + 1] = tmp
            num_swaps += 1
    if num_swaps == 0:
        break
print(f'Array is sorted in {num_swaps} swaps.')
print(f'First Element: {a[0]}')
print(f'Last Element: {a[-1]}')