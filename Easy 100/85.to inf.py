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


a = input()
k = inp()
i = 0
while i < len(a) and a[i] == '1':
    i += 1

if i >= k:
    print(1)
elif len(a) == i:
    print(1)
else:
    print(a[i])
