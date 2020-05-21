import math


# For taking integer inputs.
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


N, x = invr()

a = inlist()
a = sorted(a)
c = 0
for i in a:
    if i <= x:
        c += 1
        x -= i
    else:
        x = 0

if x > 0 and c > 0:
    c -= 1
print(c)
