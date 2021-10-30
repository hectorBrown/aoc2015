#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec  3 14:50:03 2020

@author: Hector
"""
vowels = ['a', 'e', 'i', 'o', 'u']
banned = ["ab", "cd", "pq", "xy"]
def nice(s):
    if not sum([int(c in vowels) for c in s]) >= 3:
        return False
    double = False
    last = s[0]
    for c in s[1:]:
        if c == last:
            double = True
        last = c
    if not double:
        return False
    if any([b in s for b in banned]):
        return False
    return True
data = [x[:-1] for x in open("data/day5.txt", 'r').readlines()]
print(sum([int(nice(x)) for x in data]))
#%%
def nice(s):
    rule1 = False
    for i,c in enumerate(s[:-2]):
        pair = s[i:i + 2]
        if pair in s[i + 2:]:
            rule1 = True
    rule2 = False
    for i,c in enumerate(s[:-2]):
        triple = s[i:i + 3]
        if triple[0] == triple[-1:]:
            rule2 = True
    return rule2 and rule1
data = [x[:-1] for x in open("data/day5.txt", 'r').readlines()]
print(sum([int(nice(x)) for x in data]))
