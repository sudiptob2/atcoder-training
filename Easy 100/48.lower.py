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
move = 0
m = 0
current = A[0]
for i in range(1, N):

    if A[i] <= current:
        m += 1
    else:
        m = 0
    if move < m:
        move = m
    # print(current, A[i], m, move)
    current = A[i]


print(move)
