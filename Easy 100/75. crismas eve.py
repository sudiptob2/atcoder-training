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


N, K = invr()
A = []
for i in range(N):
    A.append(inp())
A = sorted(A)
res = A[N-1] - A[0]
for i in range(N-K+1):
    d = A[i+K-1] - A[i]
    res = min(d, res)
print(res)
