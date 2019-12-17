import math
from collections import defaultdict


class IntCode:
    lst = {}
    IP = 0
    relative_base = 0

    def __init__(self, file_name="input.txt"):
        with open(file_name) as file:
            split = list(map(int, file.readline().split(",")))
            self.lst = defaultdict(lambda: 0)
            self.lst.update({x: split[x] for x in range(0, len(split))})

    def provide_input(self):
        return int(input())

    def provide_output(self, output):
        print(output)

    def get_parameter(self, l, i, instr, n):
        par_mode = self.get_par_mode(instr, n)
        if par_mode == 2:
            return l[self.relative_base + l[i + n]]
        elif par_mode == 1:
            return l[i + n]
        elif par_mode == 0:
            return l[l[i + n]]
        else:
            raise Exception("Illegal parameter mode for output")

    def get_par_mode(self, inst, n=0):
        if n == 0:
            return inst % 100
        if n == 1:
            return math.floor(inst / 100) % 10
        elif n == 2:
            return math.floor(inst / 1000) % 10
        elif n == 3:
            return math.floor(inst / 10000)
        else:
            raise Exception("Illegal input parameter mode")

    def get_store_location(self, instruction, par_nr):
        if self.get_par_mode(instruction, par_nr) == 0:
            return self.lst[self.IP + par_nr]
        elif self.get_par_mode(instruction, par_nr) == 2:
            return self.relative_base + self.lst[self.IP + par_nr]
        else:
            raise Exception("Illegal parameter mode for store")

    def instruction_step(self):
        instruction = self.lst[self.IP]
        opc = self.get_par_mode(instruction)
        if opc == 1:
            self.lst[self.get_store_location(instruction, 3)] = self.get_parameter(self.lst, self.IP, instruction,
                                                                                   1) + self.get_parameter(self.lst,
                                                                                                           self.IP,
                                                                                                           instruction,
                                                                                                           2)
            self.IP = self.IP + 4
        elif opc == 2:
            self.lst[self.get_store_location(instruction, 3)] = self.get_parameter(self.lst, self.IP, instruction,
                                                                                   1) * self.get_parameter(
                self.lst, self.IP,
                instruction,
                2)
            self.IP = self.IP + 4
        elif opc == 3:
            self.lst[self.get_store_location(instruction, 1)] = self.provide_input()
            self.IP = self.IP + 2
        elif opc == 4:
            self.provide_output(self.get_parameter(self.lst, self.IP, instruction, 1))
            self.IP = self.IP + 2
        elif opc == 5:
            if self.get_parameter(self.lst, self.IP, instruction, 1) != 0:
                self.IP = self.get_parameter(self.lst, self.IP, instruction, 2)
            else:
                self.IP = self.IP + 3
        elif opc == 6:
            if self.get_parameter(self.lst, self.IP, instruction, 1) == 0:
                self.IP = self.get_parameter(self.lst, self.IP, instruction, 2)
            else:
                self.IP = self.IP + 3
        elif opc == 7:
            if self.get_parameter(self.lst, self.IP, instruction, 1) < self.get_parameter(self.lst, self.IP,
                                                                                          instruction, 2):
                self.lst[self.get_store_location(instruction, 3)] = 1
            else:
                self.lst[self.get_store_location(instruction, 3)] = 0
            self.IP = self.IP + 4
        elif opc == 8:
            if self.get_parameter(self.lst, self.IP, instruction, 1) == self.get_parameter(self.lst, self.IP,
                                                                                           instruction, 2):
                self.lst[self.get_store_location(instruction, 3)] = 1
            else:
                self.lst[self.get_store_location(instruction, 3)] = 0
            self.IP = self.IP + 4
        elif opc == 9:
            self.relative_base = self.relative_base + self.get_parameter(self.lst, self.IP, instruction, 1)
            self.IP = self.IP + 2
        elif opc == 99:
            print('done')
            return True
        else:
            raise Exception("Illegal opcode!")

        return False

    def main(self):
        while not self.instruction_step():
            continue


#i = IntCode()
#i.main()
