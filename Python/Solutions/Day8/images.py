import sys

with open("input.txt") as file:
    lst = list(map(int, file.readline()))
    n = 150
    chunks = [lst[i:i + n] for i in range(0, len(lst), n)]

    width = 25
    height = 6
    final_image = [[2 for x in range (0, width)] for x in range (0, height)]
    for chunk in chunks:
        width = width
        rows = [chunk[i:i + width] for i in range(0, len(chunk), width)]
        for p in range(0, height):
            for q in range(0, width):
                if final_image[p][q] == 2:
                    final_image[p][q] = rows[p][q]
    for p in range(0, height):
        for q in range(0, width):
            print(final_image[p][q], end='')
        print()
