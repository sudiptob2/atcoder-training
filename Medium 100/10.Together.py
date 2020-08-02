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


n = inp()

a = inlist()
count = [0] * (100001)

for i in a:

    count[i] += 1
    if i > 0:
        count[i-1] += 1
    count[i+1] += 1

m = 0
ind = 0
print(max(count))
