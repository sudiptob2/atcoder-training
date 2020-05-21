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


S = instr()

n = len(S)

acgt = "ACGT"
max_len = 0
for i in range(n):
    for j in range(i, n+1):
        s = S[i:j]
        flag = 1
        for ch in s:
            if ch not in acgt:
                flag = 0
                break
        if flag == 1:

            max_len = max(max_len, len(s))
print(max_len)
