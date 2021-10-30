#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec  3 19:23:49 2020

@author: Hector
"""

dat = [x[:-1] for x in open("data/day8.txt",'r').readlines()]
strings = []
for line in dat:
    _int = line[1:-1]
    offset = 0
    topop = []
    skip = False
    for i,c in enumerate(_int):
        if c == '\' and not skip:
            if _int[i + 1] == 'x':
                topop.extend([i, i + 2, i + 3])
            else:
                topop.append(i)
                if _int[i + 1] == '\':
                    skip = True
        else:
            skip = False
    _int = ''.join([x for i,x in enumerate(_int) if not i in topop])
    strings.append(_int)
print(sum([len(x) for x in dat]) - sum([len(x) for x in strings]))
#%%
dat = [x[:-1] for x in open("data/day8.txt",'r').readlines()]
strings = []
for line in dat:
    encoded = line
    toescape = []
    for i,c in enumerate(encoded):
        if c in ['\','"']:
            toescape.append(i)
    encoded = "\"" + ''.join([x if not i in toescape else "\" + x for i,x in enumerate(encoded)]) + "\""
    strings.append(encoded)
print(sum([len(x) for x in strings]) - sum([len(x) for x in dat]))
