PATH = "16/data.txt"
PATH2 = "day16/ad.txt"
dat = [{y.split(':')[0]:int(y.split(':')[1]) for y in ''.join(x[:-1].split(' ')[2:]).split(',')} for x in open(PATH).readlines()]
target = {x[:-1].split(':')[0]: int(x[:-1].split(':')[1]) for x in open(PATH2).readlines()}
for i,sue in enumerate(dat):
    valid = True
    for prop in sue:
        valid = valid and sue[prop] == target[prop]
    if valid:
        print(i + 1)
