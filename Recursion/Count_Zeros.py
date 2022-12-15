#Count Zeros
#Given an integer N, count and return the number of zeros that are present in the given integer using recursion.
#Input Format :
#Integer N
#Output Format :
#Number of zeros in N
#Constraints :
#0 <= N <= 10^9

from os import *
from sys import *
from collections import *
from math import *

## Read input as specified in the question.
## Print output as specified in the question.
def cz(n):
    if n==0:
        return 1
    if n<10:
        return 0
    if n%10==0:
        return 1+cz(n//10)
    else:
    	return cz(n//10)
n=int(input())
print(cz(n))