PATH = "day5/data.txt"
def nice(s):
    rule1 = False
    for i,c in enumerate(s[:-2]):
        pair = s[i:i + 2]
        if pair in s[i + 2:]:
            rule1 = True
    rule2 = False
    for i,c in enumerate(s[:-2]):
        triple = s[i:i + 3]
        if triple[0] == triple[-1:]:
            rule2 = True
    return rule2 and rule1
data = [x[:-1] for x in open(PATH).readlines()]
print(sum([int(nice(x)) for x in data]))
