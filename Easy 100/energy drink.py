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


n, m = invr()
A = []
for i in range(n):
    A.append(inlist())

A = sorted(A, key=lambda d: d[0])
res = 0
for a in A:
    if m == 0:
        break
    if a[1] >= m:
        res += a[0] * m
        m = 0
    else:
        res += a[0] * a[1]
        m -= a[1]
print(res)
