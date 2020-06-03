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


N = inp()

a = inlist()

look = 1
removed = 0
for i in range(N):
    if a[i] != look and removed < N-1:
        removed += 1
    else:
        if a[i] == look:
            look += 1
if look == 1:
    print(-1)
else:
    print(removed)
