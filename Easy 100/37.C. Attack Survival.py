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


N, K, Q = invr()
S = [K] * (N+1)
t = 0
for i in range(1, Q+1):
    a = inp()
    S[a] += 1
    t += 1

for i in range(1, N+1):
    if S[i] - t > 0:
        print("Yes")
    else:
        print("No")
