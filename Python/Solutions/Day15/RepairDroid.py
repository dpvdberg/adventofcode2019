import sys

from Solutions.Day9.Intcode import IntCode
import math
from collections import defaultdict
from operator import add


def print_grid(grid):
    max_x = max(grid)
    min_x = min(grid)
    max_y = max([max(value) for key, value in grid.items()])
    min_y = min([min(value) for key, value in grid.items()])
    for y in range(min_y, max_y + 1):
        for x in range(min_x, max_x + 1):
            print(grid[x][y], end="")
        print("")


class FeedbackAmplifier2(IntCode):
    pending_input = None
    pending_output = None

    def __init__(self, file_name="input.txt"):
        IntCode.__init__(self, file_name)

    def provide_input(self):
        if self.pending_input:
            return self.pending_input.pop()

        raise Exception("No input...")

    def provide_output(self, o):
        self.pending_output = o

    def input_to_output(self, feedback_input):
        self.pending_input = feedback_input
        self.pending_output = None

        while self.IP < len(self.lst):
            if self.instruction_step():
                return None

            if self.pending_output is not None:
                return self.pending_output


directions = {1: 2, 2: 1, 3: 4, 4: 3}
vector = {1: (0, 1), 2: (0, -1), 3: (-1, 0), 4: (1, 0)}


def dfs(droid, visited, i=0, pos=(0, 0)):
    visited[pos[0]][pos[1]] = 1
    path_lengths = [sys.maxsize]
    for d in directions:
        changed = tuple(map(sum, zip(pos, vector[d])))
        if visited[changed[0]][changed[1]] != -1:
            continue
        status = droid.input_to_output([d])
        if status == 2:
            answer = dfs_max(droid, defaultdict(lambda: defaultdict(lambda: -1)))
            print("answer", answer)
            exit()
        elif status == 0:
            visited[changed[0]][changed[1]] = 0
        elif status == 1:
            path_lengths.append(dfs(droid, visited, i + 1, changed))
            droid.input_to_output([directions[d]])
        else:
            raise Exception("Illegal output")
    visited[pos[0]][pos[1]] = -1
    return min(path_lengths)


def dfs_max(droid, visited, i=0, pos=(0, 0)):
    visited[pos[0]][pos[1]] = 1
    path_lengths = [i]
    for d in directions:
        changed = tuple(map(sum, zip(pos, vector[d])))
        if visited[changed[0]][changed[1]] != -1:
            continue
        status = droid.input_to_output([d])
        if status == 0:
            visited[changed[0]][changed[1]] = 0
        else:
            path_lengths.append(dfs_max(droid, visited, i + 1, changed))
            droid.input_to_output([directions[d]])
    return max(path_lengths)


def part1():
    visited = defaultdict(lambda: defaultdict(lambda: -1))
    droid = FeedbackAmplifier2()
    i = dfs(droid, visited)
    print(i)


part1()
