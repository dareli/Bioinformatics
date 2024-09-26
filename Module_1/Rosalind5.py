#!/usr/bin/env python3
# -*- coding: utf-8 -*-

with open ("/Users/darleneeligado/.spyder-py3/R5.txt", "r") as data:
    line = data.read()

dictionary = {}

for word in line.split():
    if word in dictionary:
        dictionary[word]=dictionary[word]+1
    else:
        dictionary[word] = 1 
        
for key, value in dictionary.items():
    print(key, value)