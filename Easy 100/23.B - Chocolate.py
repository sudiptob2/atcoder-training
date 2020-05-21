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
D, X = inlist()
A = []
K = [0] * N
for i in range(N):
    A.append(inp())


for i in range(N):
    for d in range(D):
        eaten_at = d*A[i] + 1
        if eaten_at <= D:
            K[i] += 1
print(sum(K)+X)
