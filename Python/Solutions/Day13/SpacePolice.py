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


def main():
    comp = FeedbackAmplifier2()
    game = []
    count = 0
    score = 0
    while True:
        x = comp.input_to_output([0])
        #print(x)
        if x is None:
            break
        y = comp.input_to_output(None)
        title_id = comp.input_to_output(None)
        if x == -1 and y == 0:
            print(score)
        elif title_id == 4:
            print((x, y, title_id))


main()
