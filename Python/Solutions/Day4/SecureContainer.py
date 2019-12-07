passwords = 0
for i in range(109165, 576723):
    adjacent = False
    decreasing = False
    l = list(map(int, str(i)))
    for j in range(0, len(l)-1):
        if l[j] == l[j + 1]:
            if j == len(l)-2 and  l[j-1] != l[j]:
                adjacent = True
            if j == 0 and l[j+1] != l[j+2]:
                adjacent = True
            if j != len(l)-2 and j != 0 and l[j+1] != l[j+2] and l[j-1] != l[j]:
                adjacent = True
        if l[j] > l[j+1]:
            decreasing = True
            break
    if adjacent and not decreasing:
        passwords = passwords + 1
print(passwords)
