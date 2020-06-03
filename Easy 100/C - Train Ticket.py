# For taking integer inputs.
import math
from decimal import Decimal
from itertools import permutations


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


a = instr()
res = ""
for i in range(8):
    s = '{0:03b}'.format(i)
    temp = a[0]
    total = int(a[0])
    j = 0
    for i in range(1, 4):

        if s[j] == '0':
            total += int(a[i])
            temp += "+" + a[i]
        else:
            total -= int(a[i])
            temp += "-" + a[i]

        j += 1

    if total == 7:
        res = temp
        break
print(res+"=7")
