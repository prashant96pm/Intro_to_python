#Geometric Sum
#Given k, find the geometric sum i.e.
#1 + 1/2 + 1/4 + 1/8 + ... + 1/(2^k) 
#using recursion.
#Input format :
#Integer k
#Output format :
#Geometric sum (upto 5 decimal places)

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


def geometricSum(k):
    if k == 0:
        return 1
    small = (1/(2**k) + geometricSum(k-1))
    return small


k = int(input())
print('%.5f' % geometricSum(k))
