#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the miniMaxSum function below.
def miniMaxSum(arr):
    arr.sort()
    sum_min = sum(arr[:-1])
    sum_max = sum(arr[1::])
    print(sum_min, end=' ')
    print(sum_max)


if __name__ == '__main__':
    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)

