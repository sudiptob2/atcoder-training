def instr():
    s = input()
    return(list(s[:len(s)]))
# For taking space seperated integer variable inputs.


def invr():
    return(map(int, input().split()))


a, b = invr()
s = instr()

check = "1234567890-"
res = "Yes"

n = len(s)
if n != a+b+1:
    res = "No"
if s[a] != "-":
    res = "No"
for i in range(n):
    if s[i] not in check:
        res = "No"
        break
    if i != a and s[i] == "-":
        res = "No"
        break
print(res)
