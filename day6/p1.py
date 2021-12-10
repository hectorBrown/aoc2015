PATH = "day6/data.txt"

data = [x[:-1].split(' ') for x in open(PATH).readlines()]
mat = []
for i in range(1000):
    mat.append([-1] * 1000)
for command in data:
    xrange = [int(command[-3].split(',')[0]), int(command[-1].split(',')[0]) + 1]
    yrange = [int(command[-3].split(',')[1]), int(command[-1].split(',')[1]) + 1]
    for col in range(*xrange):
        for row in range(*yrange):
            if command[0] == "turn":
                if command[1] == "on":
                    mat[row][col] = 1
                else:
                    mat[row][col] = -1
            else:
                mat[row][col] *= -1

print(sum([sum([(x + abs(x))/2 for x in row]) for row in mat]))
