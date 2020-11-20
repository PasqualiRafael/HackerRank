#!/bin/python3

import math
import os
import random
import re
import sys


if __name__ == '__main__':
    N = int(input())


if N % 2 == 1:
    print(f'Weird')
else:
    if N in range(2, 6):
        print(f'Not Weird')
    elif N in range(6, 21):
        print(f'Weird')
    else:
        print(f'Not Weird')    
