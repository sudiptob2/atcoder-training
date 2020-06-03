# For taking integer inputs.
import math
from decimal import Decimal
from itertools import permutations


def inp():
    return(int(input()))


# For taking List inputs.
def inlist():
    return(list(map(int, input().split())))


# For taking string inputs. Actually it returns a List of Characters, instead of a string, which is easier to use in Python, because in Python, Strings are Immutable.
def instr():
    s = input()
    return(list(s[:len(s)]))


# For taking space seperated integer variable inputs.
def invr():
    return(map(int, input().split()))


s = input()
r = b = 0
for i in s:
    if i == '1':
        b += 1
    else:
        r += 1
print(min(r, b)*2)
