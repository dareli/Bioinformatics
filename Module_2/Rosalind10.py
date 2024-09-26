#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from All_Functions import pattern_count

with open('/Users/darleneeligado/.spyder-py3/R10.txt','r') as data:
    text = data.readline().rstrip()
    pattern = data.readline().rstrip()
    
print(pattern_count(text, pattern))