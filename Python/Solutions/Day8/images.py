import sys

with open("input.txt") as file:
    lst = list(map(int, file.readline()))
    n = 150
    chunks = [lst[i:i + n] for i in range(0, len(lst), n)]

    max_count = [sys.maxsize]*3
    for chunk in chunks:
        count = [0] * 3
        for i in range(0, 3):
            count[i] = len(list(filter(lambda x: x == i, chunk)))
        max_count = count if count[0] < max_count[0] else max_count
    print(max_count[1] * max_count[2])