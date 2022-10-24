PATH = "1/data.txt"

f = open(PATH)
data = f.readline()
floor = 0
for c in data:
    floor += 1 if c == '(' else -1
print(floor)
