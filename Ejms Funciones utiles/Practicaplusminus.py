#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'plusMinus' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def plusMinus(arr):
    # Write your code here
    Numberlist= list(arr)
    n=len(arr)
    positivo=0
    negativo=0
    Zero=0
    for i in Numberlist:
        if i>0:
            positivo= positivo+1
        elif i<0:
            negativo= negativo+1
        elif i==0:
            Zero= Zero+1
            
    ProPlus= float(positivo/n)
    ProNeg= negativo/n
    ProZero= Zero/n
    print ("{:.6f}".format(ProPlus))
    print ("{:.6f}".format(ProNeg))
    print ("{:.6f}".format(ProZero))
    
    return 
        

if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)