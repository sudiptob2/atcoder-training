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


N, M, X = invr()

A = inlist()

l = 0
r = N
lef_gates = 0
right_gates = 0

for a in A:
    if a > X:
        right_gates += 1
    else:
        lef_gates += 1

print(min(lef_gates, right_gates))
