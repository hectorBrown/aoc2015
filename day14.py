#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Dec  4 13:52:57 2020

@author: Hector
"""
class RD:
    def __init__(self, speed, f_t, r_t):
        self.speed = speed
        self.f_t = f_t
        self.r_t = r_t
        self.d = 0
        self.resting = False
        self.counter = 0
    def __repr__(self):
        return "{Reindeer: (Speed: " + str(self.speed) + ", Fly Time: " + str(self.f_t) + ", Rest Time: " + str(self.r_t) + ")}"
    def propagate(self):
        if not self.resting:
            self.d += self.speed
            self.counter = (self.counter + 1) if self.counter != self.f_t - 1 else 0
            self.resting = not self.counter
        else:
            self.counter = (self.counter + 1) if self.counter != self.r_t - 1 else 0
            self.resting = bool(self.counter)
dat = [x.split(' ') for x in open("data/day14.txt").readlines()]
T = int(dat[-1][0])
reindeers = {}
for line in dat[:-1]:
    reindeers[line[0]] = RD(int(line[3]), int(line[6]), int(line[-2]))
for i in range(T):
    for name in reindeers:
        reindeers[name].propagate()
print(max([reindeers[name].d for name in reindeers]))
#%%
class RD:
    def __init__(self, speed, f_t, r_t):
        self.speed = speed
        self.f_t = f_t
        self.r_t = r_t
        self.d = 0
        self.resting = False
        self.counter = 0
        self.points = 0
    def __repr__(self):
        return "{Reindeer: (Speed: " + str(self.speed) + ", Fly Time: " + str(self.f_t) + ", Rest Time: " + str(self.r_t) + ")}"
    def propagate(self):
        if not self.resting:
            self.d += self.speed
            self.counter = (self.counter + 1) if self.counter != self.f_t - 1 else 0
            self.resting = not self.counter
        else:
            self.counter = (self.counter + 1) if self.counter != self.r_t - 1 else 0
            self.resting = bool(self.counter)
dat = [x.split(' ') for x in open("data/day14.txt").readlines()]
T = int(dat[-1][0])
reindeers = {}
for line in dat[:-1]:
    reindeers[line[0]] = RD(int(line[3]), int(line[6]), int(line[-2]))
for i in range(T):
    for name in reindeers:
        reindeers[name].propagate()
    for name in reindeers:
        if reindeers[name].d == max([reindeers[name].d for name in reindeers]):
            reindeers[name].points += 1
print(max([reindeers[name].points for name in reindeers]))
