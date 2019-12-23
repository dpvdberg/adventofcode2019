import math
import numpy


def parse_input(file="input.txt"):
    with open(file) as f:
        parsed = list(map(int, f.readline()))
        return parsed


def get_pattern(index, length):
    base = [0, 1, 0, -1]
    rep_base = list(map(lambda x: [x] * (index + 1), base))
    rep_base = [item for sublist in rep_base for item in sublist]
    rep_count = math.ceil(length / len(rep_base)) + 1

    total = rep_base * rep_count
    total.pop(0)
    del total[length:]
    print(index)

    return total


def part1():
    signal = parse_input()
    signal_length = len(signal)
    pattern = list(map(lambda x: get_pattern(x, signal_length), range(0, signal_length)))
    for i in range(0, 100):
        new_signal = signal.copy()
        for j in range(0, signal_length):
            signal_sum = sum(map(lambda x: x[0] * x[1], zip(signal, pattern[j])))
            new_signal[j] = int(str(signal_sum)[-1])
        signal = new_signal
        print(i)
    print(signal)


def part2():
    signal = parse_input() * 1000
    offset = int(''.join(map(str, signal[:7].copy()))) #?????
    signal_length = len(signal)
    pattern = list(map(lambda x: get_pattern(x, signal_length), range(0, signal_length)))
    for i in range(0, 100):
        signal = numpy.dot(signal, pattern)
        signal = numpy.mod(numpy.abs(signal), 10)
        print(i)
    signal = signal.tolist()
    signal = [item for sublist in signal for item in sublist]
    print(signal[offset:(offset + 8)])


part2()
