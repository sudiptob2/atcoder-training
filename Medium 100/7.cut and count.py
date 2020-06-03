# For taking integer inputs.
import math


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


def coutDiffL(a1, a2):
    a1 = set(a1)
    a2 = set(a2)
    a3 = a1.intersection(a2)
    return len(a3)


n = inp()

s = input()
res = 0
for i in range(1, n-1):
    m1 = coutDiffL(s[:i], s[i:])
    if m1 > res:
        res = m1


print(res)
