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


def getn(n):
    c = 0
    while n % 2 == 0:
        n = n // 2
        c += 1
    return c


N = inp()
a = inlist()
c = 0
for i in a:
    c += getn(i)

print(c)
