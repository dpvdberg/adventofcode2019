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
    offset = int(''.join(map(str, signal[:7].copy())))
    signal_length = len(signal)
    pattern = list(map(lambda x: get_pattern(x, signal_length), range(0, 5)))

    for i in range(0, 100):
        signal = numpy.dot(signal, pattern)
        signal = numpy.mod(numpy.abs(signal), 10)
        print(i)
    signal = signal.tolist()
    signal = [item for sublist in signal for item in sublist]
    print(signal[offset:(offset + 8)])


def evolve_signal(signal, signal_sum, signal_length, iteration):
    sequence_length = iteration + 1
    prev_sequence_length = iteration
    prev_nr_sequences = math.ceil(signal_length / prev_sequence_length)
    nr_sequences = math.ceil(signal_length / sequence_length)


def part2_attempt2():
    signal = parse_input() * 10000
    offset = int(''.join(map(str, signal[:7].copy())))
    signal_length = len(signal)

    d = {0: {x[0]: x[1] for x in zip(range(0, signal_length), signal)}}
    for i in range(0, 8):
        print(get_value(100, offset + i, d, signal_length), end='')


pattern_map = {0: 0, 1: 1, 2: 0, 3: -1}


def part2_attempt3():
    signal = parse_input() * 10000
    print(get_phase_output(signal, 100))


def get_phase_output(input_data, num_phases):
    output = calculate(input_data, num_phases)
    print(output)
    message = ''.join([str(d) for d in output[:8]])
    return message


def calculate(input_data, num_phases):
    data = input_data
    for i in range(0, num_phases):
        sum = 0
        for j in range(len(data) - 1, -1, -1):
            sum += data[j]
            data[j] = sum % 10
    return data


def get_value(phase, index, value_dict, signal_length):
    if phase == 0:
        return value_dict[phase][index]

    print(phase)

    v = 0
    for i in range(index, signal_length):
        pattern_value = pattern_map[math.floor(((i + 1) % ((index + 1) * 4)) / (index + 1))]
        if pattern_value != 0:
            v = v + pattern_value * get_value(phase - 1, i, value_dict, signal_length)

    v = abs(v) % 10

    if phase not in value_dict:
        value_dict[phase] = {}

    value_dict[phase][index] = v
    return v


part2_attempt3()
