def instr():
    s = input()
    return(list(s[:len(s)]))


c = "abcdefghijklmnopqrstuvwxyz"
s = instr()

res = "None"
for i in c:
    if i not in s:
        res = i
        break

print(res)
