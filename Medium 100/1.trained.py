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
a = [0]

for i in range(n):
    a.append(inp())

i = 1
c = 1

while a[i] != 2:
    if a[i] == -1:
        c = -1
        break
    c += 1
    temp = i
    i = a[i]
    a[temp] = -1
print(c)
