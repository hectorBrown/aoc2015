PATH = "19/data.txt"
def transform_all(transform, molecule):
    res = []
    for occurence in get_inds_of(transform[0], molecule):
        res.append(molecule[:occurence] + transform[1] + molecule[occurence + len(transform[0]):])
    return res
def get_inds_of(target, s):
    res = []
    for i in range(len(s) - len(target) + 1):
        if s[i:i + len(target)] == target:
            res.append(i)
    return res
def uniqueify(li):
    res = []
    for i in li:
        if not i in res:
            res.append(i)
    return res
transforms = [x[:-1].split(" => ") for x in open(PATH).readlines()[:-2]]
molecule = open(PATH).readlines()[-1][:-1]
transformed = []
for transform in transforms:
    transformed.extend(transform_all(transform, molecule))
print(len(uniqueify(transformed)))
