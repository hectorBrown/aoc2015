PATH = "2/data.txt"


def SA(l,w,h):
    return 2 * l * w + 2 * w * h + 2 * h * l + min([l*w,w*h,h*l])
f = open(PATH)
data = [[int(i) for i in x[:-1].split('x')] for x in f.readlines()]
print(sum([SA(l,w,h) for l,w,h in data]))
