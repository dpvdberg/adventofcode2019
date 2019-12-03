with open("input.txt") as file:
    og = list(map(int, file.readline().split(",")))

    for k in range(0, 100):
        for j in range(0, 100):
            L = og.copy()
            L[1] = k
            L[2] = j
            for i in range(0, len(L), 4):
                opc = L[i]
                if opc == 1:
                    pos1 = L[i + 1]
                    pos2 = L[i + 2]
                    L[L[i + 3]] = L[pos1] + L[pos2]
                elif opc == 2:
                    pos1 = L[i + 1]
                    pos2 = L[i + 2]
                    L[L[i + 3]] = L[pos1] * L[pos2]
                elif opc == 99:
                    if L[0] == 19690720:
                        print('done')
                        print(100*L[1] + L[2])
                        exit()
                else:
                    break
