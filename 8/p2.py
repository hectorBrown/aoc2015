PATH = "day8/data.txt"
dat = [x[:-1] for x in open(PATH).readlines()]
strings = []
for line in dat:
    encoded = line
    toescape = []
    for i,c in enumerate(encoded):
        if c in ['\','"']:
            toescape.append(i)
    encoded = "\"" + ''.join([x if not i in toescape else "\" + x for i,x in enumerate(encoded)]) + "\""
    strings.append(encoded)
print(sum([len(x) for x in strings]) - sum([len(x) for x in dat]))
