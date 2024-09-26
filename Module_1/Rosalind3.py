#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Sep 21 08:17:48 2024

@author: darleneeligado
"""

a = 4465 
b = 9092 

total = 0 

for number in range(a, b+1):
    if number % 2 != 0:
        total += number 
        
print(total) 