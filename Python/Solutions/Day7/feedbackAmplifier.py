import itertools

from Solutions.Day5.Intcode import IntCode


class FeedbackAmplifier(IntCode):
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


m = -1

for z in itertools.permutations(range(5, 10)):
    outputs = [0] * 5
    amplifiers = [FeedbackAmplifier("amplifierCode.txt") for count in range(0, 5)]
    is_done = False
    fst = True

    while not is_done:
        for amp_index in range(0, 5):
            current_input = [outputs[amp_index - 1]]
            if fst:
                current_input.append(z[amp_index])

            output = amplifiers[amp_index].input_to_output(current_input)

            if output is not None:
                outputs[amp_index] = output
            else:
                if amp_index >= 4:
                    is_done = True

        fst = False

    m = max(m, outputs[len(outputs) - 1])

print(m)
