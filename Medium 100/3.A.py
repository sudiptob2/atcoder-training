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
n = len(a)
coutn1 = [0] * (n+1)
coutn2 = [0] * (n+1)

for i in range(n):
    if a[i] == "<":
        coutn1[i+1] = coutn1[i] + 1
for i in range(n-1, -1, -1):
    if a[i] == ">":
        coutn2[i] = coutn2[i+1] + 1

total = 0

for i in range(n+1):
    total += max(coutn1[i], coutn2[i])
print(total)
