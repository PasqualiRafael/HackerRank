import math
import os
import random
import re
import sys


def consecutive(x):
    makestr = str(bin(x)[2::])
    createlist = makestr.split('0')
    count_max = max(createlist)
    return len(count_max)

if __name__ == '__main__':
    n = int(input())
    print(consecutive(n))    
    
