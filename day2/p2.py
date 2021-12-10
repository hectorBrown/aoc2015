PATH = "day2/data.txt"
def RIB(l,w,h):
    return min([2 * x + 2 * i for x, i in [[l,w],[w,h],[h,l]]]) + l * w * h
f = open(PATH)
data = [[int(i) for i in x[:-1].split('x')] for x in f.readlines()]
print(sum([RIB(l,w,h) for l,w,h in data]))
