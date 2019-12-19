from Solutions.Day9.Intcode import IntCode
import math
from collections import defaultdict
from operator import add

grid = defaultdict(lambda: defaultdict(lambda: ' '))


def print_grid():
    max_x = max(grid)
    min_x = min(grid)
    max_y = max([max(value) for key, value in grid.items()])
    min_y = min([min(value) for key, value in grid.items()])
    for y in range(min_y, max_y + 1):
        for x in range(min_x, max_x + 1):
            print(grid[x][y], end="")
        print("")


def remove_element(element):
    for x, column in grid.items():
        for y, value in column.items():
            if value == element:
                grid[x][y] = ' '


class FeedbackAmplifier2(IntCode):
    pending_input = None
    pending_output = None

    def __init__(self, file_name="input.txt"):
        IntCode.__init__(self, file_name)

    def provide_input(self):
        print_grid()
        return int(input())

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


def main():
    comp = FeedbackAmplifier2()
    game = []
    count = 0
    score = 0
    while True:
        x = comp.input_to_output(None)
        if x is None:
            break
        y = comp.input_to_output(None)
        title_id = comp.input_to_output(None)
        if x == -1 and y == 0:
            print(score)
        elif title_id == 1:
            grid[x][y] = 'X'
        elif title_id == 2:
            grid[x][y] = '#'
        elif title_id == 3:
            remove_element('=')
            grid[x][y] = '='
        elif title_id == 4:
            remove_element('O')
            grid[x][y] = 'O'
            print_grid()


main()
