d = {}
col = []


def check_collision(curPos, i, step):
    if curPos in d:
        if d[curPos][0] != i:
            col.append(step + d[curPos][1])
    else:
        d[curPos] = (i, step)


with open("input.txt") as file:
    lines = file.readlines()
i = 0
for line in lines:
    l = line.split(",")
    curPos = (0, 0)
    step = 0
    for x in l:
        char = x[0]
        value = int(x[1:])
        if char == "R":
            for j in range(curPos[0] + 1, curPos[0] + value + 1):
                curPos = (j, curPos[1])
                step = step + 1
                check_collision(curPos, i, step)
        elif char == "L":
            for j in range(curPos[0] - 1, curPos[0] - value - 1, -1):
                curPos = (j, curPos[1])
                step = step + 1
                check_collision(curPos, i, step)
        elif char == "U":
            for j in range(curPos[1] + 1, curPos[1] + value + 1):
                curPos = (curPos[0], j)
                step = step + 1
                check_collision(curPos, i, step)
        elif char == "D":
            for j in range(curPos[1] - 1, curPos[1] - value - 1, -1):
                curPos = (curPos[0], j)
                step = step + 1
                check_collision(curPos, i, step)
        else:
            raise Exception("Illegal direction")
    print(curPos)
    i = i + 1
print(min(col))
