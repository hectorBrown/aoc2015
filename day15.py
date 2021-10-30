#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec  8 23:12:13 2020

@author: hex
"""
class Ingredient:
    def __init__(self, args, name):
        self.props = args; self.name = name
    def __repr__(self):
        return ("{" + self.name + ": [" + ', '.join([str(x) for x in self.props]) + "]}")
def get_all_distributions(buckets, n):
    if buckets == 1:
        return [[n]]
    res = []
    for i in range(n + 1):
        for x in get_all_distributions(buckets - 1, n - i):
            res.append([i] + x)
    return res
ingreds = [Ingredient(args, name) for args, name in zip([[int(y.split(' ')[-1]) for y in x[:-1].split(',')] for x in open("data/day15.txt",'r').readlines()],[x.split(':')[0] for x in open("data/day15.txt",'r').readlines()])]
tsps = 100
prods = []
for recipe in get_all_distributions(len(ingreds),tsps):
    props = [0] * 4
    for i, ingred in enumerate(ingreds):
        for j, prop in enumerate(props):
            props[j] += recipe[i] * ingred.props[j]
    prod = 1
    for i in props:
        prod *= i if i > 0 else 0
    prods.append(prod)
print(max(prods))
#%%
class Ingredient:
    def __init__(self, args, name):
        self.props = args; self.name = name
    def __repr__(self):
        return ("{" + self.name + ": [" + ', '.join([str(x) for x in self.props]) + "]}")
def get_all_distributions(buckets, n):
    if buckets == 1:
        return [[n]]
    res = []
    for i in range(n + 1):
        for x in get_all_distributions(buckets - 1, n - i):
            res.append([i] + x)
    return res
ingreds = [Ingredient(args, name) for args, name in zip([[int(y.split(' ')[-1]) for y in x[:-1].split(',')] for x in open("data/day15.txt",'r').readlines()],[x.split(':')[0] for x in open("data/day15.txt",'r').readlines()])]
tsps = 100
prods = []
for recipe in get_all_distributions(len(ingreds),tsps):
    props = [0] * 5
    for i, ingred in enumerate(ingreds):
        for j, prop in enumerate(props):
            props[j] += recipe[i] * ingred.props[j]
    prod = 1
    for i in props[:-1]:
        prod *= i if i > 0 and props[-1] == 500 else 0
    prods.append(prod)
print(max(prods))
