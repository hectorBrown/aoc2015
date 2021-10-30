#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec  3 23:54:04 2020

@author: Hector
"""    
import json
def flatten(li):
    res = []
    for elem in li:
        if type(elem) == list or type(elem) == dict:
            res.extend(flatten(elem))
        else:
            res.append(elem)
            if type(li) == dict:
                if type(li[elem]) == list or type(li[elem]) == dict:
                    res.extend(flatten(li[elem]))
                else:
                    res.append(li[elem])
    return res
dat = open("data/day12.txt",'r').readline()
dat = json.loads(dat)
total = 0
for value in flatten(dat):
    if type(value) == int:
        total += value
print(total)
#%%
import json
def flatten(li):
    res = []
    if type(li) == dict:
        if "red" in li or "red" in [li[x] for x in li]:
            return []
    for elem in li:
        if type(elem) == list or type(elem) == dict:
            res.extend(flatten(elem))
        else:
            res.append(elem)
            if type(li) == dict:
                if type(li[elem]) == list or type(li[elem]) == dict:
                    res.extend(flatten(li[elem]))
                else:
                    res.append(li[elem])
    return res
dat = open("data/day12.txt",'r').readline()
dat = json.loads(dat)
total = 0
for value in flatten(dat):
    if type(value) == int:
        total += value
print(total)
