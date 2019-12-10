from Solutions.Day5.Intcode import IntCode
import itertools




class AmplifierIntCode(IntCode):
    input = []
    output = []
    curr_index = 0
    first = True

    def provide_input(self):
        input = self.input[self.curr_index] if self.first else self.output[self.curr_index - 1]
        self.first = not self.first

        return input

    def provide_output(self, output):
        self.output[self.curr_index] = output

    def number_to_base(self, n, b):
        if n == 0:
            return [0]
        digits = []
        while n:
            digits.append(int(n % b))
            n //= b
        return digits[::-1]

    def start_amplifier(self):
        self.main("amplifierCode.txt")

    def max_amplifier_output(self):
        maximum = 0

        for z in itertools.permutations(range(0, 5)):

            self.input = z
            self.output = [0] * 5
            self.curr_index = 0
            self.first = True

            print(z)
            for j in range(0, 5):
                self.start_amplifier()
                self.curr_index = self.curr_index + 1

            output = self.output[-1]

            if output > maximum:
                maximum = output

        print(maximum)


i = AmplifierIntCode()
i.max_amplifier_output()
