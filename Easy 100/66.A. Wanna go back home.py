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


S = instr()
r = "Yes"
e, w, n, s = 0, 0, 0, 0
for i in S:
    if i in "N":
        n += 1
    elif i == "S":
        s += 1
    elif i == "E":
        e += 1
    else:
        w += 1
if (n > 0 and s > 0) or (n == 0 and s == 0):
    pass
else:
    r = "No"
if (e > 0 and w > 0) or (e == 0 and w == 0):
    pass
else:
    r = "No"
print(r)
