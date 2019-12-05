passwords = 0
for i in range(307237, 769059):
    adjacent = False
    decreasing = False
    l = list(map(int, str(i)))
    for j in range(0,len(l)-1):
        if l[j] == l[j + 1]:
            adjacent = True
        if l[j] > l[j+1]:
            decreasing = True
            break
    if adjacent and not decreasing:
        passwords = passwords + 1
print(passwords)
