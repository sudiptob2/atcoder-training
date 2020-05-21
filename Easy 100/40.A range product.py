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


a, b = invr()
res = "Negative"

if 0 < a and a <= b:
    res = "Positive"
if a <= b and b < 0:
    temp = (b-a)+1
    if temp % 2 == 0:
        res = "Positive"
    else:
        res = "Negative"
if a <= 0 and b >= 0:
    res = "Zero"

print(res)
