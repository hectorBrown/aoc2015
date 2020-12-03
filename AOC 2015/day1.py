# -*- coding: utf-8 -*-
"""
Created on Thu Dec  3 13:50:01 2020

@author: Hector
"""

f = open("Data\day1.txt")
data = f.readline()
floor = 0
for c in data:
    floor += 1 if c == '(' else -1
print(floor)
#%%
f = open("Data\day1.txt")
data = f.readline()
floor = 0
for i,c in enumerate(data):
    floor += 1 if c == '(' else -1
    if floor < 0:
        print(i + 1)
        break