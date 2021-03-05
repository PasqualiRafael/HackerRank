#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the repeatedString function below.
# s abc n 10
def repeatedString(s, n):
    number_of_a_in_original = s.count("a")  # 1
    repetitions = n // len(s)  # 10 // 3 == 3
    remaining_string_position = n % len(s)  # 10 % 3 == 1
    number_of_a_in_remaining = s[:remaining_string_position].count("a")

    return number_of_a_in_original * repetitions + number_of_a_in_remaining


if __name__ == "__main__":
    fptr = open(os.environ["OUTPUT_PATH"], "w")

    s = input()

    n = int(input())

    result = repeatedString(s, n)

    fptr.write(str(result) + "\n")

    fptr.close()
