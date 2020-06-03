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


n = inp()
a = inlist()
pref = [0] * (n)
suf = [0] * n
pref[0] = a[0]
suf[n-1] = a[n-1]
j = n - 2
for i in range(1, n):
    pref[i] = a[i] + pref[i-1]
    suf[j] = a[j] + suf[j+1]
    j -= 1

D = 10000000000000000
for i in range(0, n-1):

    s1 = pref[i]
    s2 = suf[i+1]
    d = abs(s1 - s2)
    if d < D:

        D = d

print(D)
