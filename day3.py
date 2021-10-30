#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec  3 14:04:37 2020

@author: Hector
"""

data = list(open("data/day3.txt",'r').readline())
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
#%%
data = list(open("data/day3.txt",'r').readline())
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
