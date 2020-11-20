    #!/bin/python3

import math
import os
import random
import re
import sys

# Complete the countApplesAndOranges function below.
def countApplesAndOranges(house_left, house_right, apple_tree, orange_tree, apples, oranges):
    apples_count = 0
    oranges_count = 0
    for p in range(len(apples)):        
        apples[p] = apples[p] + apple_tree
        if house_left <= apples[p] and apples[p] <= house_right:
            apples_count += 1

    for p in range(len(oranges)):        
        oranges[p] = oranges[p] + orange_tree    
        if house_left <= oranges[p] and oranges[p] <= house_right:
            oranges_count += 1        
     
    print(apples_count)
    print(oranges_count)

    

if __name__ == '__main__':
    house_lr = input().split()

    house_left = int(house_lr[0])

    house_right = int(house_lr[1])    

    tree_ao = input().split()

    apple_tree = int(tree_ao[0])

    orange_tree = int(tree_ao[1])

    quant_fruit = input().split()

    quant_apple = int(quant_fruit[0])

    quant_orange = int(quant_fruit[1])

    apples = list(map(int, input().strip().split()))

    oranges = list(map(int, input().strip().split()))

    countApplesAndOranges(house_left, house_right, apple_tree, orange_tree, apples, oranges)