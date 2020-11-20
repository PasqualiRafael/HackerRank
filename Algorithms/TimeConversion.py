#!/bin/python3

import os
import sys

#
# Complete the timeConversion function below.
#
def timeConversion(time):
    if 'PM' in time:
        if time[:2] != '12':
            converter = time.split(':')
            converter[0] = int(converter[0]) + 12
            converter[0] = str(converter[0])
            converter = ':'.join(converter)            
            return converter[:-2]
        else:
            return time[:-2]
    elif 'AM' in time:
        if time[:2] == '12':
            time = time.replace('12', '00')            
        return time[:-2]
    
if __name__ == '__main__':
    f = open(os.environ['OUTPUT_PATH'], 'w')

    time = input()

    result = timeConversion(time)

    f.write(result + '\n')

    f.close()
