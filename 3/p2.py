PATH = "3/data.txt"
data = list(open(PATH).readline())
pos_s = [[0,0],[0,0]]
visited = [[0,0]]
counter = 1
for i,c in enumerate(data):
    ind = i % 2
    if c == '^':
        pos_s[ind][1] += 1
    elif c == 'v':
        pos_s[ind][1] -= 1
    elif c == '<':
        pos_s[ind][0] -= 1
    else:
        pos_s[ind][0] += 1
    if not any([pos_s[ind][0] == x and pos_s[ind][1] == y for x,y in visited]):
        visited.append(pos_s[ind].copy())
        counter += 1
print(counter)
