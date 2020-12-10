#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec  9 23:25:28 2020

@author: hex
"""
def transform_all(transform, molecule):
    res = []
    for occurence in get_inds_of(transform[0], molecule):
        res.append(molecule[:occurence] + transform[1] + molecule[occurence + len(transform[0]):])
    return res
def get_inds_of(target, s):
    res = []
    for i in range(len(s) - len(target) + 1):
        if s[i:i + len(target)] == target:
            res.append(i)
    return res
def uniqueify(li):
    res = []
    for i in li:
        if not i in res:
            res.append(i)
    return res
transforms = [x[:-1].split(" => ") for x in open("Data/day19.txt",'r').readlines()[:-2]]
molecule = open("Data/day19.txt",'r').readlines()[-1][:-1]
transformed = []
for transform in transforms:
    transformed.extend(transform_all(transform, molecule))
print(len(uniqueify(transformed)))
#%%
def get_inds_of(target, s):
    res = []
    for i in range(len(s) - len(target) + 1):
        if s[i:i + len(target)] == target:
            res.append(i)
    return res
transforms = [x[:-1].split(" => ") for x in open("Data/day19.txt",'r').readlines()[:-2]]
transforms = [[x,y] for y,x in transforms]
molecule = open("Data/day19.txt",'r').readlines()[-1][:-1]
count = 0
while molecule != "e":
    for transform in transforms:
        if (len(get_inds_of(transform[0], molecule))):
            for i in get_inds_of(transform[0], molecule):
                new = molecule[:i] + transform[1] + molecule[i + len(transform[0]):]
                if not('e' in new and len(new) > 1):
                    molecule = new
                    count += 1
                    break
print(count)