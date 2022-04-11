PATH = "day10/data.txt"

def runlength(s):
    res = ""
    curr = s[0]
    counter = 0
    for c in s:
        if c == curr:
            counter += 1
        else:
            res += (str(counter) + str(curr))
            curr = c
            counter = 1
    res += (str(counter) + str(curr))
    return res
dat = [x[:-1] for x in open(PATH).readlines()]
out = dat[0]
for i in range(int(dat[1])):
    out = runlength(out)
print(len(out))
