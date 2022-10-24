PATH = "17/data.txt"
class Cont:
    def __init__(self, _id, cap):
        self.id = _id; self.cap = cap
    def __repr__(self):
        return ("{Container " + str(self.id) + ": " + str(self.cap) + "}")
    def __lt__(self, other):
        return self.cap < other.cap if self.cap != other.cap else self.id < other.id
def get_all_combos(lit, conts, base=True):
    res = []
    for i, cont in enumerate(conts):
        if base:
            print(str(int((i/len(conts)) * 100)) + "%")
        rem_lit = lit - cont.cap
        rem_cont = conts.copy()
        rem_cont.pop(i)
        if rem_lit == 0:
            res.append([cont])
        elif rem_lit > 0:
            for x in get_all_combos(rem_lit, rem_cont, base=False):
                to_app = [cont] + x 
                to_app.sort()
                res.append(to_app)
    return uniqueify(res)
def uniqueify(li):
    res = []
    for i in li:
        if not i in res:
            res.append(i)
    return res

lit = 150
dat = [Cont(i, int(x[:-1])) for i,x in enumerate(open(PATH).readlines())]
combos = get_all_combos(lit, dat)
print(len([x for x in combos if len(x) == min([len(y) for y in combos])]))
