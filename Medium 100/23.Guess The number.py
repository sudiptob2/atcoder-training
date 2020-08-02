import re
import sys
from bisect import bisect, bisect_left, insort, insort_left
from collections import Counter, defaultdict, deque
from copy import deepcopy
from decimal import Decimal
from fractions import gcd
from itertools import (
    accumulate, combinations, combinations_with_replacement, groupby,
    permutations, product)
from math import (
    acos, asin, atan, ceil, cos, degrees, factorial, hypot, log2, pi, radians,
    sin, sqrt, tan)
from operator import itemgetter, mul
from string import ascii_lowercase, ascii_uppercase, digits


def inp():
    return(int(input()))


def inlist():
    return(list(map(int, input().split())))


def instr():
    s = input()
    return(list(s[:len(s)]))


def invr():
    return(map(int, input().split()))


n, m = invr()
res = []
if n == 1:
    res = [0]
elif n == 2:
    res = [1, 0]
elif n == 3:
    res = [1, 0, 0]

f = [0, 0, 0]
out = 1
for _ in range(m):
    si, ci = invr()
    if si == 1 and n > 1 and ci == 0:
        out = -1
        break
    if f[si-1] == 0 or res[si-1] == ci:
        res[si-1] = ci
        f[si-1] = 1
    else:
        out = -1
        break
if out == -1:
    print(-1)

elif res[0] == 0 and len(res) > 1:
    print(-1)
else:
    for i in res:
        print(i, end="")
