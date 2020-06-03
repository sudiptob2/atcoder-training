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
if X == 1:
    print(1)
else:
    res = 1
    for b in range(2, X):
        for p in range(2, X):
            a = b**p
            if a <= X:
                res = max(a, res)
            else:
                break
    print(res)
