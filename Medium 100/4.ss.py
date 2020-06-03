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


s = input()

end = len(s)-1
res = 2
while end > 1:
    if end % 2 == 0:
        mid = end // 2
        left = s[:mid]
        right = s[mid:end]
        if left == right:
            res = len(left)
            break
        else:
            end -= 1
    else:
        end -= 1
print(res+res)
