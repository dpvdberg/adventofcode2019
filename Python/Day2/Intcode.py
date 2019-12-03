with open("input.txt") as file:
    L = list(map(int, file.readline().split(",")))
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
            print(L[0])
            exit()
        else:
            raise Exception("unknown opcode")
