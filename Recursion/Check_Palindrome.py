#Check Palindrome (recursive)
#Send Feedback
#Check whether a given String S is a palindrome using recursion. Return true or false.
#Input Format :
#String S
#Output Format :
#'true' or 'false'
#Constraints :
#0 <= |S| <= 1000
#where |S| represents length of string S.

from os import *
from sys import *
from collections import *
from math import *

from os import *
from sys import *
from collections import *
from math import *

from os import *
from sys import *
from collections import *
from math import *

from os import *
from sys import *
from collections import *
from math import *

from os import *
from sys import *
from collections import *
from math import *

def check(s,start,end):
    # base case is if end-start
    if(end-start<=0):
        return True
    if(s[start]!=s[end]):
        return False
    return check(s,start+1,end-1)
    
    
    # taking a string input 
s=str(input())
# calculating the length
l=len(s)-1
# calling the function check with arguments s,0,l whre 0 is starting index and l is last index of the string
if(check(s,0,l)==True):
    print("true")
else:
    print("false")
# print(check(s,0,l))