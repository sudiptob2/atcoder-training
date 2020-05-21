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


N = inp()
A = inlist()

s = sum(A)
c = 0
f = True
while f:
    for i in range(N):
        if A[i] % 2 != 0:
            f = False
            break
        A[i] = A[i] // 2
    if not f:
        break
    c += 1
print(c)
