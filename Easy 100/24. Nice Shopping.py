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


A, B, M = invr()

a = inlist()  # all fridger cost list
b = inlist()  # all oven cost list

C = []
for i in range(M):
    C.append(inlist())

costs_of_using_tickets = [0] * M

for i in range(M):
    ci = C[i]
    costs_of_using_tickets[i] = a[ci[0]-1] + b[ci[1]-1] - ci[2]

cost_of_not_using_tickets = min(a) + min(b)

print(min(cost_of_not_using_tickets, min(costs_of_using_tickets)))
