import sys

from Solutions.Day9.Intcode import IntCode
import math
from collections import defaultdict
from operator import add


def print_grid(grid):
    for x in grid:
        print(x)


class FeedbackAmplifier2(IntCode):
    pending_input = None
    pending_output = None

    def __init__(self, file_name="input.txt"):
        IntCode.__init__(self, file_name)

    def provide_input(self):
        if self.pending_input:
            print('bla')
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


def parse_input(robot):
    ascii_grid = []
    output = robot.input_to_output(None)
    prev = output
    while not (prev == 10 and output == 10):
        prev = output
        ascii_grid.append(output)
        output = robot.input_to_output(None)
    grid = ''.join((map(chr, ascii_grid)))
    grid = grid.strip()
    print(grid)
    grid = grid.split('\n')
    return grid

def print_sentence(robot):
    ascii_grid = []
    output = robot.input_to_output(None)
    while not output == 10:
        ascii_grid.append(output)
        output = robot.input_to_output(None)
    grid = ''.join((map(chr, ascii_grid)))
    grid = grid.strip()
    print(grid)
    return grid


def detect_intersections(grid):
    intersections = []
    for y in range(1, len(grid) - 1):
        for x in range(1, len(grid[0]) - 1):
            if grid[y - 1][x] == '#' and grid[y + 1][x] == '#' and grid[y][x - 1] == '#' and grid[y][x + 1] == '#':
                intersections.append((x, y))
                print((x, y))
    return intersections


def part1():
    robot = FeedbackAmplifier2()
    grid = parse_input(robot)
    print_grid(grid)
    intersections = detect_intersections(grid)
    sum = 0
    for intersection in intersections:
        sum = sum + intersection[0] * intersection[1]
    print(sum)


def part2():
    robot = FeedbackAmplifier2()
    parse_input(robot)
    print_sentence(robot)
    main = [65, 44, 66, 44, 67, 10]
    func_a = [76, 10]
    func_b = [76, 10]
    func_c = [76, 10]
    print(robot.input_to_output(main))
    print_sentence(robot)
    print_sentence(robot)
    print_sentence(robot)


part2()
