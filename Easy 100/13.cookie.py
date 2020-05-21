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


a, b, c = invr()
res = 0

while a % 2 == 0 and b % 2 == 0 and c % 2 == 0:
    if a == b == c:
        res = -1
        break
    ra = a/2
    rb = b/2
    rc = c/2

    a = ra + rc
    b = rb + ra
    c = rc + rb
    res += 1
print(res)
