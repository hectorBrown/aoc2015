PATH = "1/data.txt"
f = open(PATH)
data = f.readline()
floor = 0
for i,c in enumerate(data):
    floor += 1 if c == '(' else -1
    if floor < 0:
        print(i + 1)
        break
