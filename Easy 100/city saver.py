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
B = inlist()
res = 0
b = 0
prev = 0
for i in range(N):

    b = B[i]
    s = A[i] + A[i+1]

    if b + prev < s:
        res += b + prev

        if b + prev > A[i]:

            b -= A[i]
            A[i] = 0
        else:
            A[i] -= b
            b = 0

        if A[i+1] < b:
            b -= A[i+1]
            A[i+1] = 0
        else:
            A[i+1] -= b
            b = 0
    else:
        # b sum er theke boro
        res += s
        b = b - s
        A[i] = A[i+1] = 0

print(res)
