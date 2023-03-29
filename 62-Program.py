# There will be two arrays of integers. Determine all integers that satisfy the following two conditions:

# The elements of the first array are all factors of the integer being considered
# The integer being considered is a factor of all elements of the second array
# These numbers are referred to as being between the two arrays. Determine how many such numbers exist.

import math
import os
import random
import re
import sys

def getTotalX(a, b):
    lcm = get_lcm(a)
    gcd = get_gcd(b)
    count = 0
    for i in range(1, gcd // lcm + 1):
        if gcd % (lcm * i) == 0:
            count += 1
    return count

def get_lcm(l):
    lcm = l[0]
    for i in range(1, len(l)):
        lcm = lcm * l[i] // math.gcd(lcm, l[i])
    return lcm

def get_gcd(l):
    gcd = l[0]
    for i in range(1, len(l)):
        gcd = math.gcd(gcd, l[i])
    return gcd

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    m = int(first_multiple_input[1])

    arr = list(map(int, input().rstrip().split()))

    brr = list(map(int, input().rstrip().split()))

    total = getTotalX(arr, brr)

    fptr.write(str(total) + '\n')

    fptr.close()
