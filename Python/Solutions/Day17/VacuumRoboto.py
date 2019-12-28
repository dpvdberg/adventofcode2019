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
            return self.pending_input.pop()

        raise Exception("No input...")

    def provide_output(self, o):
        self.pending_output = o

    def input_to_output(self, feedback_input):
        self.pending_input = feedback_input
        if feedback_input:
            self.pending_input.reverse()
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
    while not output == 10 and output is not None:
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


def define_function(robot, function):
    print(chr(robot.input_to_output(function)), end='')
    print_sentence(robot)


def part2():
    robot = FeedbackAmplifier2()
    parse_input(robot)
    print_sentence(robot)
    main = [65, 44, 66, 44, 65, 44, 67, 44, 65, 44, 66, 44, 67, 44, 65, 44, 66, 44, 67, 10]
    #func_a = [82, 44, 56, 44, 82, 44, 49, 48, 44, 82, 49, 48, 44, 82, 44, 52, 44, 82, 44, 56, 44, 82, 44, 49, 48, 10]
    func_a = [82, 44, 56, 44, 82, 44, 49, 48, 44, 82, 44, 49, 48, 10]
    func_b = [82, 44, 52, 44, 82, 44, 56, 44, 82, 44, 49, 48, 44, 82, 44, 49, 50, 10]
    func_c = [82, 44, 49, 50, 44, 82, 44, 52, 44, 76, 44, 49, 50, 44, 76, 44, 49, 50, 10]
    total = [main, func_a, func_b, func_c]
    for func in total:
        define_function(robot, func)
    video = [110, 10]
    define_function(robot, video)
    while True:ppppp
        print(robot.input_to_output(None))
    # prev = output
    # while not (output == '' and prev == ''):
    #     prev = output
    #     output = print_sentence(robot)


part2()
