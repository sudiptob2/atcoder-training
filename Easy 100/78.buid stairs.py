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
a = inlist()
res = "Yes"
for i in range(N-1):
    if a[i] < a[i+1]:
        a[i+1] -= 1
for i in range(N-1):
    if a[i+1] < a[i]:
        res = "No"
        break
print(res)
