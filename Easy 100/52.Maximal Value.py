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
B = inlist()
A = [0] * N
A[0] = B[0]
for i in range(N-2):
    A[i+1] = min(B[i], B[i+1])

A[N-1] = B[N-2]
print(sum(A))
