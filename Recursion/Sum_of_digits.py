#Sum of digits (recursive)
#Send Feedback
#Write a recursive function that returns the sum of the digits of a given integer.
#Input format :
#Integer N
#Output format :
#Sum of digits of N
#Constraints :
#0 <= N <= 10^9

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

## Read input as specified in the question.
## Print output as specified in the question.
def Sumdigit(n):
    if n <10:
        return n
    return (n%10) + Sumdigit(n//10)

n=int(input())
print(Sumdigit(n))