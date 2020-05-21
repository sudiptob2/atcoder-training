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


N, M = invr()
K = []
for i in range(N):

    temp = inlist()
    temp = temp[1:]
    K.append(set(temp))
res = K[0]
for i in range(1, N):
    res = res.intersection(K[i])
print(len(res))
