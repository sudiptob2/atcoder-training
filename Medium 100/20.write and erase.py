import re
import sys
from bisect import bisect, bisect_left, insort, insort_left
from collections import Counter, defaultdict, deque
from copy import deepcopy
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


count = dict()

n = inp()

for _ in range(n):
    a = inp()
    if a in count:
        count[a] += 1
    else:
        count[a] = 1

c = 0

for key in count:
    c += count[key] % 2
print(c)
