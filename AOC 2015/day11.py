# -*- coding: utf-8 -*-
"""
Created on Thu Dec  3 23:29:11 2020

@author: Hector
"""
banned = ['i','o','l']
def incr(s):
    col = len(s) - 1
    wrap = True
    while wrap:
        wrap = False
        s = ''.join([(chr(ord(elem) + 1) if ord(elem) < 122 else 'a') if i == col else elem for i,elem in enumerate(s)])
        wrap = s[col] == 'a'
        col -= 1
    return s
def valid(pswd):
    rule1 = False
    for i,c in enumerate(pswd[:-2]):
        if c == chr(ord(pswd[i + 1]) - 1) and c == chr(ord(pswd[i + 2]) - 2):
            rule1 = True
    rule2 = all([not c in banned for c in pswd])
    paired = []
    for i,c in enumerate(pswd[:-1]):
        if c == pswd[i + 1] and not c in paired:
            paired.append(c)
    rule3 = len(paired) >= 2
    return rule1 and rule2 and rule3
    
dat = open("Data\day11.txt",'r').readline()
curr = dat
while not valid(curr):
    curr = incr(curr)
print(curr)
#%%
banned = ['i','o','l']
def incr(s):
    col = len(s) - 1
    wrap = True
    while wrap:
        wrap = False
        s = ''.join([(chr(ord(elem) + 1) if ord(elem) < 122 else 'a') if i == col else elem for i,elem in enumerate(s)])
        wrap = s[col] == 'a'
        col -= 1
    return s
def valid(pswd):
    rule1 = False
    for i,c in enumerate(pswd[:-2]):
        if c == chr(ord(pswd[i + 1]) - 1) and c == chr(ord(pswd[i + 2]) - 2):
            rule1 = True
    rule2 = all([not c in banned for c in pswd])
    paired = []
    for i,c in enumerate(pswd[:-1]):
        if c == pswd[i + 1] and not c in paired:
            paired.append(c)
    rule3 = len(paired) >= 2
    return rule1 and rule2 and rule3
    
dat = open("Data\day11.txt",'r').readline()
curr = dat
while not valid(curr):
    curr = incr(curr)
curr = incr(curr)
while not valid(curr):
    curr = incr(curr)
print(curr)