#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Sep 21 08:43:09 2024

@author: darleneeligado
"""

with open ("/Users/darleneeligado/.spyder-py3/R4.txt","r") as data:
    list_of_lines = data.readlines()
    
print("".join(list_of_lines[1::2]))
