# -*- coding: utf-8 -*-
"""
Created on Thu Dec  3 15:20:31 2020

@author: Hector
"""
# from PIL import Image

data = [x[:-1].split(' ') for x in open("Data\day6.txt",'r').readlines()]
mat = []
for i in range(1000):
    mat.append([-1] * 1000)
# img = Image.new(mode="RGB", size=(1000,1000), color="red")
# pixels = img.load()
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

# for i,row in enumerate(mat):
#     for j,x in enumerate(row):
#         if x == 1:
#             pixels[j,i] = (0,255,0)
#         else:
#             pixels[j,i] = (255,0,0)
print(sum([sum([(x + abs(x))/2 for x in row]) for row in mat]))
# img.show()
#%%
data = [x[:-1].split(' ') for x in open("Data\day6.txt",'r').readlines()]
mat = []
for i in range(1000):
    mat.append([0] * 1000)
for command in data:
    xrange = [int(command[-3].split(',')[0]), int(command[-1].split(',')[0]) + 1]
    yrange = [int(command[-3].split(',')[1]), int(command[-1].split(',')[1]) + 1]
    for col in range(*xrange):
        for row in range(*yrange):
            if command[0] == "turn":
                if command[1] == "on":
                    mat[row][col] += 1
                else:
                    mat[row][col] -= 1 if mat[row][col] > 0 else 0
            else:
                mat[row][col] += 2
print(sum([sum(row) for row in mat]))