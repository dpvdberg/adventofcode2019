from Solutions.Day5.Intcode import IntCode


class AmplifierIntCode(IntCode):
    l = []
    curr_index = 0
    first = True

    def provide_input(self):
        input = self.l[self.curr_index + (0 if self.first else 1)]
        self.first = not self.first
        return input

    def provide_output(self, output):
        self.l[self.curr_index + 3] = output

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
        for i in range(0, 3125):
            convert = self.number_to_base(i, 5)
            while len(convert) < 5:
                convert.insert(0, 0)
            convert.append(0)
            for j in range(1, (len(convert)) * 2, 2):
                convert.insert(j, 0)
            self.l = convert
            print(convert)
            self.curr_index = 0
            for j in range(0, 5):
                self.start_amplifier()
                output = self.l[11]
                if output > maximum:
                    maximum = output
                self.curr_index = self.curr_index + 2
        print(maximum)


i = AmplifierIntCode()
i.max_amplifier_output()
