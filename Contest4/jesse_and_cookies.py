#!/bin/python3

import math
import os
import random
import re
import sys
import heapq as hq

#
# Complete the 'cookies' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER k
#  2. INTEGER_ARRAY A
#

def cookies(k, A):
    # Write your code here        
    q = []
    res = 0
    
    for el in A:
        hq.heappush(q, el)
    
    while any(c < k for c in q) and len(q) > 1:
        last = hq.heappop(q)
        prelast = hq.heappop(q)
        
        new = last + 2*prelast
        
        hq.heappush(q, new)
        res += 1
        
    if all(c >= k for c in q):
        return res
    else:
        return -1
        
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    k = int(first_multiple_input[1])

    A = list(map(int, input().rstrip().split()))

    result = cookies(k, A)

    fptr.write(str(result) + '\n')

    fptr.close()
