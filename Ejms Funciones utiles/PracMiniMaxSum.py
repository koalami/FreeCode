#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'miniMaxSum' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def miniMaxSum(arr):
    # Write your code here
    Menor=0
    Mayor=0
    Numberlist= list(arr)
    Numberlist.sort()
    for i in Numberlist[0:4]:
        Menor= Menor+i
    for j in Numberlist[1:]:
        Mayor= Mayor+j
    print (Menor, Mayor)
        
if __name__ == '__main__':

    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)
