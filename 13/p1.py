PATH = "13/data.txt"
def combo(li, fixed=[]):
    res = []
    if len(li) == 1:
        temp = fixed.copy()
        temp.extend(li)
        return temp
    for i, item in enumerate(li):
        temp = fixed.copy()
        temp.append(item)
        if len(li) == 2:
            res.append(combo([elem for a, elem in enumerate(li) if a != i], temp))
        else:
            res.extend(combo([elem for a, elem in enumerate(li) if a != i], temp))
    return res
dat = [x[:-2].split(' ') for x in open(PATH).readlines()]
pref = {}
for line in dat:
    if not line[0] in pref:
        pref[line[0]] = {}
    pref[line[0]][line[-1]] = (-1 if line[2] == "lose" else 1) * int(line[3])

happiness_s = []
for arrangement in combo(pref.keys()):
    happiness = 0
    for i,person in enumerate(arrangement):
        left = arrangement[(i - 1) if i - 1 >= 0 else len(arrangement) - 1]
        right = arrangement[(i + 1) if i + 1 < len(arrangement) else 0]
        happiness += pref[person][left] + pref[person][right]
    happiness_s.append(happiness)
print(max(happiness_s))
