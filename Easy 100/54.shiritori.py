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
S = []
f = "Yes"
for i in range(N):
    s = input()
    if i > 0:
        prev = S[i-1]
        if s in S or s[0] != prev[-1]:
            f = "No"
    S.append(s)
print(f)
