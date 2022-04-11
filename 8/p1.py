PATH = "day8/data.txt"

dat = [x[:-1] for x in open(PATH).readlines()]
strings = []
for line in dat:
    _int = line[1:-1]
    offset = 0
    topop = []
    skip = False
    for i,c in enumerate(_int):
        if c == '\' and not skip:
            if _int[i + 1] == 'x':
                topop.extend([i, i + 2, i + 3])
            else:
                topop.append(i)
                if _int[i + 1] == '\':
                    skip = True
        else:
            skip = False
    _int = ''.join([x for i,x in enumerate(_int) if not i in topop])
    strings.append(_int)
print(sum([len(x) for x in dat]) - sum([len(x) for x in strings]))
