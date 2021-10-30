#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec  3 13:54:32 2020

@author: Hector
"""


def SA(l,w,h):
    return 2 * l * w + 2 * w * h + 2 * h * l + min([l*w,w*h,h*l])
f = open("data/day2.txt")
data = [[int(i) for i in x[:-1].split('x')] for x in f.readlines()]
print(sum([SA(l,w,h) for l,w,h in data]))
#%%
def RIB(l,w,h):
    return min([2 * x + 2 * i for x, i in [[l,w],[w,h],[h,l]]]) + l * w * h
f = open("data/day2.txt")
data = [[int(i) for i in x[:-1].split('x')] for x in f.readlines()]
print(sum([RIB(l,w,h) for l,w,h in data]))
