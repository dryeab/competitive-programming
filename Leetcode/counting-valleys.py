
# link - https://www.hackerrank.com/challenges/counting-valleys/problem

#!/bin/python3

import math
import os
import random
import re
import sys

def countingValleys(steps, path):
    height = 0
    result = 0
    for i in path:
        if i == "D":
            height -= 1
        else: height += 1
        
        if height == 0 and i=="U": result += 1
    
    return result
        
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    steps = int(input().strip())

    path = input()

    result = countingValleys(steps, path)

    fptr.write(str(result) + '\n')

    fptr.close()

