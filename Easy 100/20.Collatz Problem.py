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


s = inp()

A = []

while s not in A:
    A.append(int(s))
    if s % 2 == 0:
        s = int(s/2)
    else:
        s = int(3*s + 1)
print(len(A)+1)
