# -*- coding: utf-8 -*-
"""
Created on Thu Dec  3 14:35:01 2020

@author: Hector
"""
import hashlib
def valid(s):
    return s[:5] == ''.join(['0'] * 5)
key = open("Data\day4.txt").readline()
num = 1
while True:
    if valid(hashlib.md5((key + str(num)).encode()).hexdigest()):
        break
    num += 1
print(num)
#%%
import hashlib
def valid(s):
    return s[:6] == ''.join(['0'] * 6)
key = open("Data\day4.txt").readline()
num = 1
while True:
    if valid(hashlib.md5((key + str(num)).encode()).hexdigest()):
        break
    num += 1
print(num)