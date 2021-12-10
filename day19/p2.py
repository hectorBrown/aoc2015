PATH = "day19/data.txt"
def get_inds_of(target, s):
    res = []
    for i in range(len(s) - len(target) + 1):
        if s[i:i + len(target)] == target:
            res.append(i)
    return res
transforms = [x[:-1].split(" => ") for x in open(PATH).readlines()[:-2]]
transforms = [[x,y] for y,x in transforms]
molecule = open(PATH).readlines()[-1][:-1]
count = 0
while molecule != "e":
    for transform in transforms:
        if (len(get_inds_of(transform[0], molecule))):
            for i in get_inds_of(transform[0], molecule):
                new = molecule[:i] + transform[1] + molecule[i + len(transform[0]):]
                if not('e' in new and len(new) > 1):
                    molecule = new
                    count += 1
                    break
print(count)
