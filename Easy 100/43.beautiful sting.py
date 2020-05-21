s = input()

C = [0]*26

for i in s:
    C[ord(i)-ord('a')] += 1
res = "Yes"
for i in C:
    if i % 2 != 0:
        res = "No"
print(res)
