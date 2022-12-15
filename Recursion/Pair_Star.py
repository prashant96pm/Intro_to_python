#Pair Star
#Send Feedback
#Given a string S, compute recursively a new string where identical chars that are adjacent in the original string are separated from each other by a "*".
#Input format :
#String S
#Output format :
#Modified string
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

## Read input as specified in the question.
## Print output as specified in the question.
def PairStar(s,si):
    l = len(s)
    if si == l or si == l-1:
        return s[si]
    
    if s[si] == s[si+1]:
        return s[si]+ "*" + PairStar(s,si+1)
    else:
        return s[si] + PairStar(s,si+1)
s=input()
print(PairStar(s,0))
