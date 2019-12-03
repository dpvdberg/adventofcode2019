d = {}
col = []


def check_collision(curPos, i):
    if curPos in d:
        if d[curPos] != i:
            col.append(curPos)
    d[curPos] = i


with open("input.txt") as file:
    lines = file.readlines()
i = 0
for line in lines:
    l = line.split(",")
    curPos = (0, 0)
    for x in l:
        char = x[0]
        value = int(x[1:])
        if char == "R":
            for j in range(curPos[0] + 1, curPos[0] + value + 1):
                curPos = (j, curPos[1])
                check_collision(curPos, i)
        elif char == "L":
            for j in range(curPos[0] - 1, curPos[0] - value - 1, -1):
                curPos = (j, curPos[1])
                check_collision(curPos, i)
        elif char == "U":
            for j in range(curPos[1] + 1, curPos[1] + value + 1):
                curPos = (curPos[0], j)
                check_collision(curPos, i)
        elif char == "D":
            for j in range(curPos[1] - 1, curPos[1] - value - 1, -1):
                curPos = (curPos[0], j)
                check_collision(curPos, i)
        else:
            raise Exception("Illegal direction")
    print(curPos)
    i = i + 1
print(min(list(map(lambda y: abs(y[0]) + abs(y[1]), col))))
