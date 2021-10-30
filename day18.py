#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec  9 23:01:46 2020

@author: hex
"""
def count_neighbours(mat, i, j):
    count = 0
    for i_s in range(-1, 2):
        for j_s in range(-1, 2):
            if i + i_s >= 0 and i + i_s < len(mat) and j + j_s >= 0 and j + j_s < len(mat[i]) and not (i_s == 0 and j_s == 0):
                count += 1 if mat[i + i_s][j + j_s] == '#' else 0
    return count

steps = 100
dat = [[c for c in x[:-1]] for x in open("data/day18.txt",'r').readlines()]
for a in range(steps):
    new = [line.copy() for line in dat]
    for i,line in enumerate(dat):
        for j,c in enumerate(line):
            if c == '.' and count_neighbours(dat, i, j) == 3:
                new[i][j] = '#'
            elif c == '#' and not (count_neighbours(dat, i, j) == 3 or count_neighbours(dat, i, j) == 2):
                new[i][j] = '.'
    dat = [line.copy() for line in new]
# for line in dat:
#     print(''.join(line))
print(sum([len([elem for elem in x if elem == '#']) for x in dat]))
#%%
def count_neighbours(mat, i, j):
    count = 0
    for i_s in range(-1, 2):
        for j_s in range(-1, 2):
            if i + i_s >= 0 and i + i_s < len(mat) and j + j_s >= 0 and j + j_s < len(mat[i]) and not (i_s == 0 and j_s == 0):
                count += 1 if mat[i + i_s][j + j_s] == '#' else 0
    return count

steps = 100
dat = [[c for c in x[:-1]] for x in open("data/day18.txt",'r').readlines()]
for a in range(steps):
    new = [line.copy() for line in dat]
    for i,line in enumerate(dat):
        for j,c in enumerate(line):
            if c == '.' and count_neighbours(dat, i, j) == 3:
                new[i][j] = '#'
            elif c == '#' and not (count_neighbours(dat, i, j) == 3 or count_neighbours(dat, i, j) == 2):
                new[i][j] = '.'
    new[0][0] = '#'
    new[-1][0] = '#'
    new[0][-1] = '#'
    new[-1][-1] = '#'
    dat = [line.copy() for line in new]
# for line in dat:
#     print(''.join(line))
print(sum([len([elem for elem in x if elem == '#']) for x in dat]))
