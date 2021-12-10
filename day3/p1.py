PATH = "day3/data.txt"

data = list(open(PATH).readline())
pos = [0,0]
visited = [[0,0]]
counter = 1
for c in data:
    if c == '^':
        pos[1] += 1
    elif c == 'v':
        pos[1] -= 1
    elif c == '<':
        pos[0] -= 1
    else:
        pos[0] += 1
    if not any([pos[0] == x and pos[1] == y for x,y in visited]):
        visited.append(pos.copy())
        counter += 1
print(counter)
