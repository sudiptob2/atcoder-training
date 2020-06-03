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


H, W = invr()
C = []
for i in range(H):
    temp = instr()
    C.append(temp)

for i in range(2*H):
    temp = ""
    for j in range(W):
        temp += C[i//2][j]
    print(temp)
