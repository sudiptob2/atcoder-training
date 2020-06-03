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


def which(a, b, x, y):
    if x < y:
        return b
    return a


a, b, c, x, y = invr()

cost1 = a * x + b * y
cost2 = 1000000000000
cost3 = 1000000000000

if x > y:
    temp1 = 2 * x * c
    temp2 = 2 * y * c + (x-y)*a  # baki a damer pizza
    cost2 = min(temp1, temp2)
else:
    temp1 = 2 * y * c
    temp2 = 2 * x * c + (y-x) * b  # baki je koyta y pizza lagbe tar dam
    cost2 = min(temp1, temp2)


print(min(cost1, cost2))
