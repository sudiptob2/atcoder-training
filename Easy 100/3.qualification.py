# For taking string inputs. Actually it returns a List of Characters, instead of a string, which is easier to use in Python, because in Python, Strings are Immutable.
def insr():
    s = input()
    return(list(s[:len(s)]))


def invr():
    return(map(int, input().split()))


n, a, b = invr()
S = insr()
os = 0
jp = 0
for s in S:
    if s == "a":
        if jp+os < a+b:
            jp += 1
            print("Yes")
        else:
            print("No")
    elif s == "b":
        if os+1 <= b and os+jp < a+b:
            os += 1
            print("Yes")
        else:
            print("No")
    else:
        print("No")
