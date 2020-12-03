# -*- coding: utf-8 -*-
"""
Created on Thu Dec  3 23:19:55 2020

@author: Hector
"""

def runlength(s):
    res = ""
    curr = s[0]
    counter = 0
    for c in s:
        if c == curr:
            counter += 1
        else:
            res += (str(counter) + str(curr))
            curr = c
            counter = 1
    res += (str(counter) + str(curr))
    return res
dat = [x[:-1] for x in open("Data\day10.txt",'r').readlines()]
out = dat[0]
for i in range(int(dat[1])):
    out = runlength(out)
print(len(out))
#%%
def runlength(s):
    res = ""
    curr = s[0]
    counter = 0
    for c in s:
        if c == curr:
            counter += 1
        else:
            res += (str(counter) + str(curr))
            curr = c
            counter = 1
    res += (str(counter) + str(curr))
    return res
dat = [x[:-1] for x in open("Data\day10.txt",'r').readlines()]
out = dat[0]
for i in range(int(dat[1]) + 10):
    out = runlength(out)
print(len(out))