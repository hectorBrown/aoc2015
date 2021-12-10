PATH = "day7/data.txt"
import numpy as np
dat = [x[:-1].split(' ') for x in open(PATH).readlines()]
wires = {"b": np.uint16(16076)}
while len(dat) > 0:
    topop = []
    for i, command in enumerate(dat):
        if command[0] == "NOT":
            if command[1].isalpha():
                if command[1] in wires:
                    res = ~wires[command[1]]
                else:
                    continue
            else:
                res = ~np.uint16(command[1])
        elif command[1] == "->":
            if command[0].isalpha():
                if command[0] in wires:
                    res = wires[command[0]]
                else:
                    continue
            else:
                res = np.uint16(command[0])
        else:
            if command[0].isalpha():
                if command[0] in wires:
                    arg1 = wires[command[0]]
                else:
                    continue
            else:
                arg1 = np.uint16(command[0])
            if command[2].isalpha():
                if command[2] in wires:
                    arg2 = wires[command[2]]
                else:
                    continue
            else:
                arg2 = np.uint16(command[2])
            if command[1] == "AND":
                res = arg1 & arg2
            elif command[1] == "OR":
                res = arg1 | arg2
            elif command[1] == "LSHIFT":
                res = arg1 << arg2
            elif command[1] == "RSHIFT":
                res = arg1 >> arg2
        if not command[-1] == "b":
            wires[command[-1]] = res
        topop.append(i)
    temp = dat.copy()
    for i in topop:
        temp.remove(dat[i])
    dat = temp
print(wires["a"])
