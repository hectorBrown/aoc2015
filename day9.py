#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec  3 21:35:19 2020

@author: Hector
"""
def combo(li, fixed=[]):
    res = []
    if len(li) == 1:
        temp = fixed.copy()
        temp.extend(li)
        return temp
    for i, item in enumerate(li):
        temp = fixed.copy()
        temp.append(item)
        if len(li) == 2:
            res.append(combo([elem for a, elem in enumerate(li) if a != i], temp))
        else:
            res.extend(combo([elem for a, elem in enumerate(li) if a != i], temp))
    return res
data = [x[:-1].split(' ') for x in open("data/day9.txt",'r').readlines()]
distances = {}
for line in data:
    distances[line[0]] = {}
distances[data[-1][2]] = {}
for line in data:
    distances[line[0]][line[2]] = int(line[-1])
    distances[line[2]][line[0]] = int(line[-1])
places = distances.keys()
routes = combo(places)
route_d = []
for route in routes:
    distance = 0
    for i, place in enumerate(route[:-1]):
        distance += distances[place][route[i + 1]]
    route_d.append(distance)
print(min(route_d))
#%%
def combo(li, fixed=[]):
    res = []
    if len(li) == 1:
        temp = fixed.copy()
        temp.extend(li)
        return temp
    for i, item in enumerate(li):
        temp = fixed.copy()
        temp.append(item)
        if len(li) == 2:
            res.append(combo([elem for a, elem in enumerate(li) if a != i], temp))
        else:
            res.extend(combo([elem for a, elem in enumerate(li) if a != i], temp))
    return res
data = [x[:-1].split(' ') for x in open("data/day9.txt",'r').readlines()]
distances = {}
for line in data:
    distances[line[0]] = {}
distances[data[-1][2]] = {}
for line in data:
    distances[line[0]][line[2]] = int(line[-1])
    distances[line[2]][line[0]] = int(line[-1])
places = distances.keys()
routes = combo(places)
route_d = []
for route in routes:
    distance = 0
    for i, place in enumerate(route[:-1]):
        distance += distances[place][route[i + 1]]
    route_d.append(distance)
print(max(route_d))
