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
WA = [0] * (N+1)
AC = [0] * (N+1)
penalty = 0
for i in range(M):
    p, s = map(str, input().split())
    p = int(p)
    if s == "AC" and AC[p] == 0:
        AC[p] = 1
        penalty += WA[p]
    elif s == "WA" and AC[p] == 0:
        WA[p] += 1

print(sum(AC), penalty)
