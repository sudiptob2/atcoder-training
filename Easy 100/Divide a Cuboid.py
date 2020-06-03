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


a = inlist()
a = sorted(a, reverse=True)

big = a[0]

if big % 2 == 0:
    print(0)
else:
    d1 = a[1] * a[2] * (big // 2)
    d2 = a[1] * a[2] * ((big // 2) + 1)
    print(d2 - d1)
