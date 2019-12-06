import math


def get_parameter(l, i, instr, n):
    par_mode = get_par_mode(instr, n)
    if par_mode == 1:
        return l[i + n]
    elif par_mode == 0:
        return l[l[i + n]]
    else:
        raise Exception("Illegal parameter mode for output")


def get_par_mode(inst, n=0):
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


def main(file_name="input.txt"):
    with open(file_name) as file:
        lst = list(map(int, file.readline().split(",")))
        i = 0
        while i < len(lst):
            instruction = lst[i]
            opc = get_par_mode(instruction)
            if opc == 1:
                if get_par_mode(instruction, 3) == 0:
                    lst[lst[i + 3]] = get_parameter(lst, i, instruction, 1) + get_parameter(lst, i, instruction, 2)
                else:
                    raise Exception("Illegal parameter mode for output")
                i = i + 4
            elif opc == 2:
                if get_par_mode(instruction, 3) == 0:
                    lst[lst[i + 3]] = get_parameter(lst, i, instruction, 1) * get_parameter(lst, i, instruction, 2)
                else:
                    raise Exception("Illegal parameter mode for output")
                i = i + 4
            elif opc == 3:
                if get_par_mode(instruction, 1) == 0:
                    lst[lst[i + 1]] = int(input())
                else:
                    raise Exception("Illegal parameter mode for save location")
                i = i + 2
            elif opc == 4:
                print(get_parameter(lst, i, instruction, 1))
                i = i + 2
            elif opc == 99:
                print('done')
                break
            else:
                raise Exception("Illegal opcode!")


main()
