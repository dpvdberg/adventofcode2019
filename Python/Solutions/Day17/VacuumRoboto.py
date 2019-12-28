import sys

from Solutions.Day9.Intcode import IntCode
import math
from collections import defaultdict
from operator import add, itemgetter


def print_grid(grid):
    for x in grid:
        print(x)


class FeedbackAmplifier2(IntCode):
    pending_input = None
    pending_output = None

    def __init__(self, file_name="input.txt"):
        IntCode.__init__(self, file_name)

    def provide_input(self):
        print("input")
        return int(input())
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


directions = ['<', '>', '^', 'v']

opp_directions = {'<': '>', '>': '<', '^': 'v', 'v': '^'}

direction_switch = {'<': {'^': 'R', 'v': 'L'},
                    '>': {'^': 'L', 'v': 'R'},
                    '^': {'<': 'L', '>': 'R'},
                    'v': {'<': 'R', '>': 'L'}}


def line_has_robot(line):
    return any(d in line for d in directions)


def find_robot(grid):
    line = next(x for x in grid if line_has_robot(x))
    y = grid.index(line)
    x = line.index(next(x for x in line if x != '.' and x != '#'))
    return x, y


def is_blocked_spot(grid, x, y):
    return x >= len(grid[0]) or x < 0 or y < 0 or y >= len(grid) or grid[y][x] != '#'


def max_walk(grid, x, y, direction):
    if direction == '>':
        if is_blocked_spot(grid, x + 1, y):
            return 0
        return 1 + max_walk(grid, x + 1, y, direction)
    elif direction == '<':
        if is_blocked_spot(grid, x - 1, y):
            return 0
        return 1 + max_walk(grid, x - 1, y, direction)
    elif direction == '^':
        if is_blocked_spot(grid, x, y - 1):
            return 0
        return 1 + max_walk(grid, x, y - 1, direction)
    elif direction == 'v':
        if is_blocked_spot(grid, x, y + 1):
            return 0
        return 1 + max_walk(grid, x, y + 1, direction)


def step(x, y, direction, distance):
    if direction == '>':
        return x + distance, y
    elif direction == '<':
        return x - distance, y
    elif direction == '^':
        return x, y - distance
    elif direction == 'v':
        return x, y + distance


def get_path(grid):
    robot_x, robot_y = find_robot(grid)
    current_dir = grid[robot_y][robot_x]
    l = []

    m = -1
    while m != 0:
        allowed_directions = [x for x in directions if x != current_dir and x != opp_directions[current_dir]]
        d, m = max(zip(allowed_directions, [max_walk(grid, robot_x, robot_y, d) for d in
                                            allowed_directions
                                            ]), key=itemgetter(1))

        dir_switch = direction_switch[current_dir][d]
        if m != 0:
            l.append(dir_switch)
            l.append(str(m))

        current_dir = d
        robot_x, robot_y = step(robot_x, robot_y, current_dir, m)

    return l


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
    grid = parse_input(robot)
    print(find_robot(grid))
    path = get_path(grid)
    print(path)
    l = [[char for char in word] for word in path]
    l = [item for sublist in l for item in sublist]
    l = [ord(x) for x in l]
    print(len(l))
    print_sentence(robot)
    main = [65, 44, 66, 44, 67, 10]
    func_a = [76, 10]
    func_b = [76, 10]
    func_c = [76, 10]
    print(robot.input_to_output(main))


part2()
