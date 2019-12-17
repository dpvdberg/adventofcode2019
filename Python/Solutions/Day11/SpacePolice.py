from Solutions.Day9.Intcode import IntCode
import math
from collections import defaultdict
from operator import add


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


def step(pos, direction):
    if direction == 0:
        return tuple(map(add, pos, (0, 1)))
    elif direction == 1:
        return tuple(map(add, pos, (1, 0)))
    elif direction == 2:
        return tuple(map(add, pos, (0, -1)))
    elif direction == 3:
        return tuple(map(add, pos, (-1, 0)))
    else:
        raise Exception("Illegal direction!")


def turn(direction, turn):
    if turn == 0:
        return (direction - 1) % 4
    elif turn == 1:
        return (direction + 1) % 4
    else:
        raise Exception("Illegal turn")


def main():
    grid = defaultdict(lambda: defaultdict(lambda: 0))
    pos = (0, 0)
    direction = 0
    visited = set()

    comp = FeedbackAmplifier2()

    while True:
        color = comp.input_to_output([grid[pos[0]][pos[1]]])
        if color is None:
            break
        t = comp.input_to_output(None)

        grid[pos[0]][pos[1]] = color
        visited.add(pos)

        direction = turn(direction, t)
        pos = step(pos, direction)

    print(len(visited))


main()
