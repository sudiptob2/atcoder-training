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


X = inp()
res = 0
for i in range(100, 106):
    d = X % i
    # print(d)
    for i in range(100, 106):
        if d % i == 0:
            res = 1
            break
print(res)
