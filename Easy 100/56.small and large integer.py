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


A, B, K = invr()
r1 = []
r2 = []
k = K
for i in range(A, B+1):
    if k > 0:
        r1.append(i)
        print(i)
    else:
        break
    k -= 1
k = K
for i in range(B, A-1, -1):
    if k > 0:
        if i not in r1:
            r2.append(i)
    else:
        break
    k -= 1
r2 = sorted(r2)
for i in r2:
    print(i)
