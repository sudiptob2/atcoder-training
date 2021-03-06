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


D = []

for i in range(5):
    D.append(inp())

D = sorted(D, key=lambda d: 0 if d % 10 == 0 else ((d//10)+1)*10-d)

res = 0
for d in D[:4]:
    if d % 10 != 0:
        res += d + (((d//10)+1)*10-d)
    else:
        res += d
print(res+D[4])
